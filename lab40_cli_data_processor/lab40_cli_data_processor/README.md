# Lab 40: Final Mini-Project - CLI Data Processor

## Overview
This lab implements a Command-Line Interface (CLI) Data Processor in Python.  
It fetches data from an API, validates JSON, logs progress, and saves results to a file.

## Key Features
- Fetch data from API (`requests`)
- Save JSON to file (`json`)
- CLI arguments for `--api_url` and `--file_path` (`argparse`)
- Logging for progress & error tracking (`logging`)
- Exception handling and validation

## Steps
1. Install requirements:
   ```bash
   python3 -m pip install requests --break-system-packages
   ```
2. Run the program:
   ```bash
   python3 data_processor.py --api_url https://jsonplaceholder.typicode.com/posts --file_path output.json
   ```

## Errors & Fixes
- **`ModuleNotFoundError: No module named 'requests'`** → Install with pip.
- **Permission denied** → Use `--break-system-packages` or virtualenv.

## Conclusion
This project shows how to integrate Python modules to build a robust CLI tool with logging, argument parsing, and JSON validation.
