from bs4 import BeautifulSoup
import urllib2
from termcolor import colored

import time, sys

import re




opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
print colored('############################################################################','red')
print colored(' This Program will Search given name in IISER website for There RollNumber','yellow')
print colored(' ------------------------------By Ojas-------------------------------------','green')
print colored('#############################################################################','red')



N=str(raw_input('Student Name:'))
f=[]
for x in range(16,7,-1):
    s=''
    if x<10:
        s='0'+str(x)
    else:
        s=str(x)
    r = opener.open('http://www.iisermohali.ac.in/students/studentsms20'+s+'.html').read()
    soup = BeautifulSoup(r, "lxml")


    tr = soup.findAll('tr',  attrs = {'valign' : 'TOP'})
    for d in tr:
        if d.find(text=re.compile(N)):
            f.append(d)

for j in f:
    r=j.findAll('span',class_='textfont')
    print r[1].text
