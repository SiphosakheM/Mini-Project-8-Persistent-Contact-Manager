# Mini-Project-8-Persistent-Contact-Manager

# Project 08: Persistent Contact Manager

## Overview
This project introduces Data Persistence. It addresses the issue of "volatile memory" by allowing the application to save its state to a physical file on disk. This step is essential for building software ready for production.

## Key Features
- **JSON Integration:** Uses the JSON format to store structured object data.
- **Persistent Storage:** Data remains even after the script is closed or the computer restarts.
- **Initialization Logic:** Automatically loads previous data when starting up.
- **Robustness:** Handles `FileNotFoundError` to keep the app from crashing on its first run.

## Technical Specs
- **Module:** `import json` or `import csv`
- **File I/O:** Uses `with open('data.json', 'w') as f:` for safe file handling.
- **Object Mapping:** Converts Class instances to Dictionaries and back again.

## How to Use
1. Run the script:
   ```bash
   python persistent_contacts.py
   ```
