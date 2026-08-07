
Group Leader Responsibilities: Keep the team on schedule, organize task delegation, and coordinate the final submission.

# Step 1: Brainstorming and Planning

-Make a list of group needs and brainstorm a few manual tasks that can be automated with a script. Start small and plan to add one or two features to expand it.
-Narrow your ideas down to 2-3 options. Define what manual task each replaces, what inputs and outputs are needed, and how error handling will work.
-Remember the language split: use Python for complex logic and Bash for setup, orchestration, or system-level automation.
-Assign roles based on team strengths and self-advocacy.

Deliverable: Draw a 1-page architecture flowchart showing System Inputs, the Bash Component, the Data Handshake, the Python Component, and the Final Output.

# Step 2: Write Logic and System Orchestration

-Build a Minimum Viable Product (MVP) first, expanding functionality only if time permits.
-Develop the Python core logic (tool.py) to handle data parsing, file management, or complex calculations using standard libraries or lightweight third-party tools.
-Create the Bash entry script (run.sh) to parse at least one command-line flag or argument (--input ./data), log start and end timestamps, and launch the Python script.
-Set up your runtime environment using one of the following alternatives:
Option A: A standard Python venv with a requirements.txt file setup and activated via script.
Option B: Podman using a minimalist Containerfile (python:3.11-slim).
Option C: Conda/Miniconda defined by an environment.yml file.
Option D: Bypass environment tools and run directly using the system's global Python interpreter.

-Update your flowchart to illustrate actual script execution from start to finish.
-Add clear docstrings, inline comments, and a README.md file.

# Step 3: Practice and Test
-Write at least 2 simple pytest unit tests (test_tool.py) to verify core functions or handle edge cases.
-Run a linter (pylint or flake8) to ensure the code passes basic checks without syntax or execution errors.
-Test your scripts against edge cases (missing files, missing permissions) and optionally have an outside team member test your tool.

# Step 4: Presentation
-Prepare a short demonstration of your working automation,
-10-15 minute live presentation to the class where all members take turns speaking. Use minimal slides that only enhance your live run-through, focusing on showing how it works rather than telling.

Your presentation must cover:
Architecture Flowchart. Show your diagram and explain the data flow.
The Handshake Demo. Show the exact line of code, CLI flag, pipe, or temporary file format where Bash hands off data to Python.
Execution. Run the script live using different parameters or mock inputs.

Ideas:
