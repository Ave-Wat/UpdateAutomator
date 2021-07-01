# UpdateAutomator
### About
This project was created by a team of System Administrator interns at Carleton College. This set of scripts pulls application updates to all of the lab machines from a server. This script checks for new updates daily. If new application updates are found, the script runs the update on the local machine.

### How to Use
To schedule the code to run daily, execute `bash crontab.sh`.

To run the code, execute `python3 fetch_updates.py`.

