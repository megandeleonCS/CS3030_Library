#TOPICS COVERED
1. Process Management & Python Automation
Execution & Outputs: Command execution with subprocess.run(), capturing stdout/stderr as text (text=True).
Error Handling: Trapping exit codes and process errors via subprocess.CalledProcessError.
Process Piping: Chaining processes programmatically using subprocess.Popen() without shell=True.
Timeouts & Safety: Managing process execution limits with TimeoutExpired and catching hanging tasks.

2. POSIX Shell Scripting (Bash)
Argument & Flag Parsing: Processing CLI options (-h, -v) using getopts.
Input Validation: Checking directory existence (-d), file types, and routing errors to stderr (>&2).
Exit Codes: Returning standard exit statuses (exit 0, exit 1, exit 2) for graceful control flow.
System Utilities: Aggregating file statistics and disk usage using native Linux commands (find, du, wc, ls).

3. Advanced Python System Utilities & Administration
Modern Path Operations: Using object-oriented paths with pathlib (Path.rglob(), Path.mkdir()).
High-Level File Operations: Copying trees and packaging .zip archives with shutil (copy2, make_archive).
Runtime & Environment Checks: Reading os.environ and verifying interpreter environment state (sys.executable, sys.prefix).
CLI Design: Building professional command-line interfaces with flag validation using argparse.
Signal Handling: Catching termination signals (signal.SIGINT / Ctrl+C) to clean up temporary resources before exit.
