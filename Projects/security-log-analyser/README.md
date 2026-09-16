# Security Log Analyser

## Overview
The Security Log Analyser is a Python program that takes a user provided log file and analyses it for suspicious authentication activity. It identifies IP addresses with three or more failed login attempts within a five-minute window and ultimetaley reports the relevant activity to the user.

## Features
- Accepts a user provided authentication log file
- Identifies IP addresses associated with failed login attempts
- Extracts timestamps to detect repeated attempts within a five-minute window 
- Provides command-line help and usage information
- Generates a readable security report
- Formats timestamps into a clear, readable format

## Detection Logic
The program detects a suspicious IP if its associated with three or more failed login attempts within a five minute window. It uses Python's 'timedelta' to compare the time between relevant login attempts against the five minute threshold.

```markdown
## Usage

To run the analyser, provide the path to an authentication log file as a command-line argument:

```bash
python3 analyser.py auth.log
```

`auth.log` is the sample authentication log included with the project

## Example Output
```
Suspicious IP: 192.168.1.20
Failed attempts: 09:17:03, 09:18:45, 09:21:33
Reason: 3 failed login attempts within 5 minutes

Suspicious IP: 10.0.0.10
Failed attempts: 10:00:00, 10:02:00, 10:05:00
Reason: 3 failed login attempts within 5 minutes
```

## Limitations & Future Improvements
- Currently supports a specific authentication log format
- Results are displayed in the terminal rather then exported to a structural format
- Future Improvements could include JSON/CSV export, configrable detection thresholds, and support for additional log formats
