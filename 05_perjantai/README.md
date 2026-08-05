Make a team of 3-4. 
Come up with a script that one of you needs on their laptop.
Brainstorm: Draw a 1-page architecture flowchart on paper showing:

System Inputs
Bash Component
Data Handshake
Python Component
Final Output

Build the Minimum Viable Product (MVP) first!
Get Bash passing 1 basic string/file to Python within 30 minutes, then expand functionality.

Presentation
Each team will present their project live. 

Your presentation must include:
Architecture Flowchart: Show your diagram and explain the data flow.
The Handshake Demo: Show the exact line of code, CLI flag, pipe (|), or temporary file format where Bash hands off data to Python.

Execution: Run the script live using different parameters or mock inputs. 

Ideas:

Project TypeBash Student HandlesPython Student HandlesSystem Health & AlertingScrapes disk space / memory usage via system utilities and pipes alerts to Python.Parses the thresholds, formats a clean human-readable log, or sends a webhook notification.API & CLI ToolPrompts the CLI user for inputs, handles input flags (--json, --save), and streams payload to Python.Calls an API (e.g., weather or public data), parses the payload, and outputs filtered results.Log Analyzer & ReporterScans /var/log or custom project logs, filters relevant error codes using grep/sed, and dumps clean text. Calculates stats, counts top error frequencies, and formats a markdown or HTML report.