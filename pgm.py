import glob
import socket
from re import sub
import urllib2
from bs4 import BeautifulSoup
import os
import urllib

### Get the directory
directory = raw_input("Enter the directory name:")
directory = sub('["]',"",directory)

directory1 = directory +"/*.txt"
directory2 = directory +"\\counter.txt"



lists = glob.glob(directory1)    #"C:\\Users\\gsudan\\Desktop\\Project\\*.txt"   C:\Users\gsudan\Desktop\Project http://www.mangareader.net/naruto/691
if len(lists) == 0:
        url = raw_input("Enter the URL: ")
        count = 1
        file_counter = open(directory2,"a")
        input_to_file = url + " " + str(count)
        file_counter.write(input_to_file)
        file_counter.close()

lists = []
lists = glob.glob(directory1)

file_counter = open(lists[0])

split = file_counter.read().split(" ")
url = split[0]
count = int(split[1])

print url
url_split = url.split("/")
url_source = url_split[0] + "//"
url_source += url_split[2]

print url_split
split = directory.split("\\")
print split
match = split[len(split) - 1].lower()
print count

file_counter.close()

while True:
        try:
                timeout = 900
                socket.setdefaulttimeout(timeout)
                resp = urllib2.urlopen(url)
                html_source = resp.read()

                soup = BeautifulSoup(html_source)

                for div_content in soup.findChildren('div',{'id':'imgholder'}):
                        os.chdir(directory)
                        try:
                                next_src = div_content.find('a')['href']
                                image_url = div_content.find('a').find('img')['src']
                                if next_src.find(match) == -1:
                                        raise IOError
                                print "(Downloading ---->" + str(count) + ".jpg)" +"-- The file is in URL: " + url
                                print next_src, image_url
                                image = urllib.URLopener()
                                test = image.retrieve(image_url,str(count)+".jpg")
                                print test
                                count = int(count) + 1
                                url = url_source + next_src
                        except 'Navigable String':
                                pass
        except IOError:
                file_counter = open(directory2,"w")
                count = int(count)
                input_to_file = url + " " + str(count)
                file_counter.write(input_to_file)
                file_counter.close()
                break
        except KeyboardInterrupt:
                file_counter = open(directory2,"w")
                count = int(count) + 1
                input_to_file = url + " " + str(count)
                file_counter.write(input_to_file)
                file_counter.close()
                raise
"""else:
        file_counter = open(directory2,"w")
        count = int(count) + 1
        input_to_file = url + " " + str(count)
        file_counter.write(input_to_file)
        file_counter.close()"""  

print "----------------------------------------------------------------------"
