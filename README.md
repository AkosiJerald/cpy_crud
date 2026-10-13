# CRUD Names Web App

A beginner-friendly Create, Read, Update, Delete (CRUD) web app using Python, Flask, HTML, and CSS.

## Project structure

```text
crud_names/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    └── css/
        └── style.css
```

## Setup

1. Install Python 3 from https://www.python.org/downloads/. During installation on Windows, select **Add Python to PATH**.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:

   ```bash
   py -m venv .venv
   ```

5. Activate it on Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run:

   ```bat
   .venv\Scripts\activate.bat
   ```

6. Install Flask:

   ```bash
   python -m pip install -r requirements.txt
   ```

7. Start the app:

   ```bash
   python app.py
   ```

8. Open http://127.0.0.1:5000 in your browser.
9. To stop the server, click the terminal and press `Ctrl+C`.

## Features

- View all names
- Add a name
- Edit an existing name
- Delete a name with confirmation
- Basic validation for blank and duplicate names
- Responsive HTML/CSS interface

## Note

This starter project stores names in a Python list in memory, not a database. Entries reset when the app restarts. Use a database such as SQLite if permanent storage is required.
