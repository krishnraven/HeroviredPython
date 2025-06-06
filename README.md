 Q1: Password Strength Checker

**Script:** `Pwd.py`

 Description:
Validates the strength of a user-provided password based on the following criteria:
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (e.g., !, @, #, $)

How to Run:

python Pwd.py
Q2: CPU Usage Monitor
Description:
Monitors the system's CPU usage and displays an alert when it exceeds a specified threshold (default: 80%).

Prerequisite:
pip install psutil

How to Run:
python cpu.py

Q3: Configuration File Parser & API

Script: config.py

Configuration File: config.ini

Description:
Reads and parses a .ini configuration file, converts it to JSON, and serves it via a REST API using Flask

How to Run:
python config.py

View Config Output
http://127.0.0.1:5000/config

Q4: File Backup Script
Description:
Backs up files from a source directory to a destination directory. If a file already exists in the destination, appends a timestamp to avoid overwriting.

mkdir D:\CoursePyHerovired\Source
mkdir D:\CoursePyHerovired\Backup
echo Hello > D:\CoursePyHerovired\Source\file1.txt in linux 
create txt if it is windows

How to Run:
python backup.py
