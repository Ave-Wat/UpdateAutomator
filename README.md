# UpdateAutomator
### About
This project was created by a team of System Administrator interns at Carleton College. This set of scripts pulls application updates to all of the lab machines from a server. This script checks for new updates daily. If new application updates are found, the script runs the update on the local machine.

## How to Use
### Requirements
- The files fetch_updates.py, crontab.sh, write_history.sh, and read_history.sh all have filepaths hardcoded in. If changing where the files are ran, will need to edit all filepaths. The filepaths start at the root home directory.
- Must give [cron full-disk access](https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/). 

### Execution
- To schedule the code to run daily, execute `bash crontab.sh`.
- To run the code, execute `python3 fetch_updates.py`.

