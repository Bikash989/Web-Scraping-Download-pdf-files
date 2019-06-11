# program that accepts a url address from the user and prints the links
# import networking library to open connections to the webpage and load file
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
#before using BeautifulSoup library, install: pip3 install BeautifulSoup
from bs4 import BeautifulSoup
# disable secure socket layer certification error, if any
import ssl
import requests
import re
import os #to delete the empty file, if no links found


try:
    #ignore SSL certification errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    url = input("Enter full url(eg: http://www.jmlr.org/papers/v20/): ")
    if url == '':
        print("Invalid Url")
    else:

        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        #retrieve anchor tags
        tags = soup('a')
        print("Connection established")
        #here we will create a folder and store in downloads later
        temp = url.split('/')
        if(len(temp) == 3):
            filename = temp[2].split('.')[1]
        elif(len(temp) == 4):
            filename = temp[2].split('.')[1] + '-' + temp[ len(temp)-1]
        else:
            filename = temp[len(temp)-2] + '-' + temp[len(temp)-1]
        # filename = input('Enter file name to store the links : ')
        fh = open(filename,'w')
        link = 0 #to indicate if copied any links
        for tag in tags:
            line = tag.get('href', None)

            if(line != None and line.endswith('.pdf')):
                #resolve relative path
                line = urljoin(url,line)
                line = line + "\n"  #add a new line
                fh.write(line)
                link += 1

    fh.close() # release resource
    # opens the link file and downloads
    if link > 0:
        print(link , " links present!")
        fh = open(filename, 'r')
        for line in fh:
            link = line.strip()
            # print('link: ',link)
            r = requests.get(link, stream=True)
            chunk_size = 2000

            #file name
            words = link.split('/')
            fname = words[len(words)-1]
            print('Downloading file from ', link)
            with open(fname,'wb') as fd:
                for chunk in r.iter_content(chunk_size):
                    fd.write(chunk)
            # print("Done.")
        print('\nDownloaded')
        os.remove(filename)
        fh.close()
    else:
        os.remove(filename)
        print('No pdf links found at ' +url)

except Exception as e:
    print()
    print(e)
    print("please enter http:// followed by the www dot example dot com")
