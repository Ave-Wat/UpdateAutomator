#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import subprocess

#note: grant cron full-disk access (https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/) 
#note: make sure all files have full directory paths (both read_history.sh and write_history.sh have paths in them)

base_url = 'https://cs.carleton.edu/faculty/mtie/lab-updates-2021/'
headers = requests.utils.default_headers()
headers.update({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",})

def get_file_num():
	url = base_url + "descriptions.txt"
	descriptions_file = requests.get(url, headers=headers)
	content = descriptions_file.content
	items = content.splitlines()
	return len(items)

def read_automator_history():
	file_list = []	
	read_history = subprocess.Popen(['bash', "/usr/local/admin/UpdateAutomator/read_history.sh"], stdout=subprocess.PIPE)
	for line in read_history.stdout:
		file_list.append(line.strip().decode('utf8'))
	return file_list       

def get_files(file_num):
	prev_run_files = read_automator_history()	

	for i in range(1, file_num + 1):
		filename = "{}.tar.Z".format(i)
		already_run = False
		if(filename in prev_run_files):
			already_run = True
        
		if already_run == False:
			"""download file"""
			url = "{}{}.tar.Z".format(base_url, i)
			tar_file = requests.get(url, allow_redirects = True)
			open('/usr/local/admin/UpdateAutomator/{}'.format(filename), 'wb').write(tar_file.content)
			extract = subprocess.Popen(['tar', '-xvzf', filename])
			run = subprocess.Popen(['bash', "./{}/{}.script".format(i, i)])
			write = subprocess.Popen(['bash', "/usr/local/admin/UpdateAutomator/write_history.sh", filename])
			remove = subprocess.Popen(['bash', "/usr/local/admin/UpdateAutomator/remove_files.sh", filename])    
def main():
	get_files(get_file_num())


if __name__ == "__main__":
	main()
