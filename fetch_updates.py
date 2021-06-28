import requests
from bs4 import BeautifulSoup
import subprocess

#make sure to go in and edit your chrontab by typing vi chrontab -e then once you get in there changing it to visual mode before adding the line 08*** python3 /path/to/test_script.py filling in the path there

base_url = 'https://cs.carleton.edu/faculty/mtie/lab-updates-2021/'
headers = requests.utils.default_headers()
headers.update({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",})

def get_file_num():
    url = base_url + "descriptions.txt" 
    descriptions_file = requests.get(url, headers=headers)
    content = descriptions_file.content
    items = content.splitlines()
    print(items)
    return len(items)

def get_files(file_num):
    for i in range(1, file_num + 1):
	"""download file"""
	url = base_url + i
	tar_file = requests.get(url, allow_redirects = True
	filename = i + '.tar.Z'
	open(filename, 'wb').write(tar_file.content)
    
def un_tar_files():
    


get_files(get_file_num())
