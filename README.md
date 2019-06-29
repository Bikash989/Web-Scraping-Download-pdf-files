# pdfScraper
Download pdf files from a webpage.
We use urllib to read the webpage.
It scrapes the webpage and searches all the anchor tag with .pdf extension using BeautifulSoup library.
It stores all the pdf links in the file and the relative path is fixed as well.
We then create a folder and open the file and read the links line by line and download the pdf and store it in the folder.

Library Used:
BeautifulSoup: pip3 install BeautifulSoup4

requests: pip3 install requests

ssl: for any certification error

os: to create a folder
