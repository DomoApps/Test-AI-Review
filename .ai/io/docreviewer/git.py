# Apache License
# Version 2.0, January 2004
# Author: Eugene Tkachenko

import subprocess
from typing import List
from log import Log

class Git:

    @staticmethod
    def __run_subprocess(options):
        Log.print_green(options)
        result = subprocess.run(options, stdout=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            Log.print_red(options)
            raise Exception(f"Error running {options}: {result.stderr}")

    @staticmethod
    def get_remote_name() -> str:
        command = ["git", "remote", "-v"]
        result = Git.__run_subprocess(command)
        lines = result.strip().splitlines()
        return lines[0].split()[0]

    @staticmethod
    def get_last_commit_sha(file) -> str:
        command = ["git", "log", "-1", "--format=\"%H\"", "--", file]
        result = Git.__run_subprocess(command)
        lines = result.strip().splitlines()
        return lines[0].split()[0].replace('"', "")
        
    @staticmethod
    def get_diff_files(remote_name, head_ref, base_ref) -> List[str]:
        command = ["git", "diff", "--name-only", f"{remote_name}/{base_ref}", f"{remote_name}/{head_ref}"]
        result = Git.__run_subprocess(command)
        return result.strip().splitlines()
        
    @staticmethod
    def get_diff_in_file(remote_name, head_ref, base_ref, file_path) -> str:
        command = ["git", "diff", f"{remote_name}/{base_ref}", f"{remote_name}/{head_ref}", "--", file_path]
        return Git.__run_subprocess(command)

    @staticmethod
    def map_line_to_position(file_diffs: str, line_number: int) -> int:
        """
        Maps a line number from the AI's output to the correct position in the diff.

        Args:
            file_diffs (str): The diff content for the file.
            line_number (int): The line number from the AI's output.

        Returns:
            int: The position in the diff corresponding to the line number, or None if not found.
        """
        current_line = 0
        position = 0

        for diff_line in file_diffs.splitlines():
            if diff_line.startswith("@@"):
                # Extract the starting line number for the diff hunk
                hunk_info = diff_line.split(" ")[2]
                start_line = int(hunk_info.split(",")[0].lstrip("+"))
                current_line = start_line - 1
                position = 0  # Reset position for each hunk
            elif diff_line.startswith("+") and not diff_line.startswith("+++"):
                current_line += 1
                position += 1
                if current_line == line_number:
                    return position
            elif not diff_line.startswith("-"):
                current_line += 1

        return None