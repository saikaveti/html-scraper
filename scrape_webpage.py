import urllib.request
import webbrowser
import os

import sys

new = 2

url = sys.argv[1]
file_name = sys.argv[2]

fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf-8")
fp.close()

file = open(file_name, "w")
file.write(mystr)
file.close()

new_html_url = "file://" + os.getcwd() + "/" + file_name
print(new_html_url)
webbrowser.open(new_html_url, new=new)
