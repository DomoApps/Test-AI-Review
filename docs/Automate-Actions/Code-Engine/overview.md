# Code Engine Overview

**Code Engine** is a powerful platform that enables developers to build and deploy custom JavaScript and Python packages as serverless functions. Designed to extend the capabilities of existing workflows and applications, Code Engine provides a flexible, scalable, and efficient environment for custom code execution. These custom functions can be shared with users in your instnace, and are accessable via endpoint or in a workflow as an automated step.

## Things to keep in mind

- **Size Limits** - The maximum size of a function input and output is 1Mb
- **Strict Typing** - Function inputs and outputs are strongly typed. This helps to prevent errors when used in systems like Workflows
- **Execution Time** - Functions have a maximum execution time of 5 minutes
- **Logs** - When running a Code Engine function in a workflow, your logs will only show there if you `throw` in your function. If you `console.log` or `print`, the logs will only be available when running the function in Code Engine
- **Catching Errors** - If you catch your errors in your function, the workflow will not be able to catch them. Be sure to `throw` your errors to ensure they are caught by the workflow
