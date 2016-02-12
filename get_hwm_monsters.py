# -*- coding: utf-8 -*-
import re, urllib, urllib2
from urllib import FancyURLopener
class MyOpener(FancyURLopener):
    version = "Baka/0.1"
myopener = MyOpener()
url = myopener.open('http://www.heroeswm.ru/plstats_hunters.php').read()
f = re.findall('army_info.php\?name\=([a-zA-Z0-9]+)*', url)
print f
