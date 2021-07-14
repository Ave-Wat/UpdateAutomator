#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import subprocess

#note: grant cron full-disk access (https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/) 
#note: make sure all files have full directory paths (both read_history.sh and write_history.sh have paths in them)

base_url = 'https://cs.carleton.edu/faculty/mtie/lab-updates-2021/'
headers = requests.utils.default_headers()
headers.update({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",})
path = '/usr/local/admin/UpdateAutomator'
updates_path = path + "/updates"

def get_file_num():
	url = base_url + "descriptions.txt"
	descriptions_file = requests.get(url, headers=headers)
	content = descriptions_file.content
	items = content.splitlines()
	return len(items)

def read_automator_history():
	file_list = []	
	read_history = subprocess.Popen(['bash', "{}/read_history.sh".format(path), path], stdout=subprocess.PIPE)
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
			make_updates_dir = subprocess.Popen(['mkdir', '-p',  updates_path])
			open('{}/{}'.format(updates_path, filename), 'w+')
			print(tar_file.content)
			with open('{}/{}'.format(updates_path, filename), 'wb') as file:
				file.write(tar_file.raw.read())
				print("print" + str(i))
				file.close
			extract = subprocess.Popen(['tar', '-xvzf', "{}/{}".format(updates_path, filename), '-C', updates_path])
			run_downloaded_script = subprocess.Popen(['bash', "{}/{}/{}.script".format(updates_path, i, i)])
			write_history = subprocess.Popen(['bash', "{}/write_history.sh".format(path), filename, path])

def main():
	get_files(get_file_num())
	#remove_updates = subprocess.Popen(['rm', '-rf', updates_path])

if __name__ == "__main__":
	main()
