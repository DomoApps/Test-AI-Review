# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

import os
from git import Git 
from pathlib import Path
from ai.chat_gpt import ChatGPT
from openai import OpenAI
from ai.ai_bot import AiBot
from log import Log
from env_vars import EnvVars
from repository.github import GitHub
from repository.repository import RepositoryError

separator = "\n\n----------------------------------------------------------------------\n\n"

def main():
    with open('output.txt', 'a') as log_file:
        vars = EnvVars()
        vars.check_vars()
        model = OpenAI(api_key = vars.chat_gpt_token)
        ai = ChatGPT(model, vars.chat_gpt_model)
        github = GitHub(vars.token, vars.owner, vars.repo, vars.pull_number)

        remote_name = Git.get_remote_name()
        Log.print_green("Remote is", remote_name)
        changed_files = Git.get_diff_files(remote_name=remote_name, head_ref=vars.head_ref, base_ref=vars.base_ref)
        Log.print_green("Found changes in files", changed_files)
        if len(changed_files) == 0: 
            Log.print_red("No changes between branch")

        for file in changed_files:
            Log.print_green("Checking file", file)

            _, file_extension = os.path.splitext(file)
            file_extension = file_extension.lstrip('.')
            if file_extension not in vars.target_extensions:
                Log.print_yellow(f"Skipping, unsuported extension {file_extension} file {file}")
                continue

            try:
                with open(file, 'r') as file_opened:
                    file_content = file_opened.read()
            except FileNotFoundError:
                Log.print_yellow("File was removed. Continue.", file)
                continue

            if len(file_content) == 0: 
                Log.print_red("File is empty")
                continue

            file_diffs = Git.get_diff_in_file(remote_name=remote_name, head_ref=vars.head_ref, base_ref=vars.base_ref, file_path=file)
            if len(file_diffs) == 0: 
                Log.print_red("Diffs are empty")

            Log.print_green(f"Asking AI. Content Len:{len(file_content)} Diff Len: {len(file_diffs)}")
            response = ai.ai_request_diffs(code=file_content, diffs=file_diffs)

            log_file.write(f"{separator}{file_content}{separator}{file_diffs}{separator}{response}{separator}")

            Log.print_green("Fetching git diff...")
            Log.print_green(f"Git diff for file {file}:")
            Log.print_green(file_diffs)

            Log.print_green("AI response:")
            Log.print_green(response)

            if AiBot.is_no_issues_text(response):
                Log.print_green("File looks good. Continue", file)
            else:
                responses = AiBot.split_ai_response(response)
                if len(responses) == 0:
                    Log.print_red("Responses where not parsed:", responses)

                result = False
                for response in responses:
                    Log.print_green(f"Processing AI response: line={response.line}, text={response.text}")
                    if response.line:
                        # Map the AI's line number to the diff's position
                        diff_position = Git.map_line_to_position(file_diffs, response.line)
                        if diff_position is not None:
                            Log.print_green(f"Mapped AI line {response.line} to diff position {diff_position}")
                            result = post_line_comment(github=github, file=file, text=response.text, line=diff_position)
                        else:
                            Log.print_red(f"Could not map AI line {response.line} to a diff position. AI output: {response.text}")
                    if not result:
                        Log.print_yellow(f"Posting general comment for file {file}")
                        result = post_general_comment(github=github, file=file, text=response.text)
                    if not result:
                        Log.print_red("Failed to post any comments.")
                        raise RepositoryError("Failed to post any comments.")
                    
def post_line_comment(github: GitHub, file: str, text:str, line: int):
    Log.print_green("Posting line", file, line, text)
    try:
        git_response = github.post_comment_to_line(
            text=text, 
            commit_id=Git.get_last_commit_sha(file=file), 
            file_path=file, 
            position=line,
        )
        Log.print_yellow("Posted", git_response)
        return True
    except RepositoryError as e:
        Log.print_red("Failed line comment", e)
        return False

def post_general_comment(github: GitHub, file: str, text:str) -> bool:
    Log.print_green("Posting general", file, text)
    try:
        message = f"{file}\n{text}"
        git_response = github.post_comment_general(message)
        Log.print_yellow("Posted general", git_response)
        return True
    except RepositoryError:
        Log.print_red("Failed general comment")
        return False

if __name__ == "__main__":
    main()