from bs4 import BeautifulSoup
import urllib2
from termcolor import colored

import time, sys

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(progress):
    barLength = 30 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rComputing: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()





opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
print colored('#####################################','red')
print colored(' This Program will give you in_words','yellow')
print colored(' -------------By Ojas---------------','green')
print colored('#####################################','red')



a=int(raw_input('Starting From :'))
b=int(raw_input('To  :'))
textss=''
for x in range(a,b+1):
    r = opener.open('https://www.google.co.in/search?q='+str(x)+'+in+words&ie=utf-8&oe=utf-8&gws_rd=cr&ei=8HdeWOWnO4vovASVmZrgCQ').read()
    soup = BeautifulSoup(r, "lxml")
    letters = soup.find_all("h2", class_="r")
    update_progress(float(x-a)/float(b-a))
    #print letters[0].text
    textss=textss+'  '+str(letters[0].text)
file=open('F.txt','w')
file.write(textss)
print colored('Saved TO F.txt','green')
