# WiFi Password Retriever

A simple Python script to retrieve all saved WiFi passwords from your local Windows system.

**Note:** This tool only works on Windows and requires administrator privileges to retrieve passwords.

## Features

- Retrieve all saved WiFi network names
- Display passwords for each network
- Export passwords to a text file
- Clean, formatted output
- No external dependencies (uses only Python standard library)

## Requirements

- Windows OS
- Python 3.6 or higher
- Administrator privileges (to access saved passwords)

## Installation

1. Clone or download this repository
2. No additional packages needed - uses only Python standard library

## Usage

### Display passwords in console

Run the script with administrator privileges:

```bash
python wifi_password.py
```

### Export to file

To export all WiFi passwords to a text file:

```bash
python wifi_password.py --export
```

This will create a `wifi_passwords.txt` file in the same directory.

## Legal & Ethical Use

This tool is intended for legitimate purposes only:
- Retrieving your own forgotten WiFi passwords
- System administration tasks
- Personal device management

## Disclaimer

This tool is provided as-is for educational and personal use. Users are responsible for ensuring they comply with all applicable laws and regulations when using this tool.
