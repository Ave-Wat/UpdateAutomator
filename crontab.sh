#!/bin/bash
(crontab -l 2>/dev/null; echo "0 7 * * * /usr/bin/python3 /usr/local/admin/UpdateAutomator/fetch_updates.py") | crontab -
