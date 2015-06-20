#! /usr/bin/python
#encoding: utf-8

__author__ = "Dj_System"
__date__ = "$30/05/2015 09:00:00 PM$"

from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
from utilities import *
import os
import urllib2
  
def download():
    url = "http://www.chia-anime.tv/watch/one-piece-episode-"+episode+"/"
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    iFrames = []
    for iframe in soup("iframe"):
        iFrames.append(iframe.extract()["src"])
    url = iFrames[2]
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    params = []
    for param in soup("param"):
        params.append(param.extract()["value"])
    video = params[1][182:237]
    os.system('PyAxel ' + video)
    if os.name == "posix":
        os.system("mv " + video[34:] + " op" + episode + ".mp4")
    elif os.name == "nt":
        os.system("move " + video[34:] + " op" + episode + ".mp4")

def main():
    clrscr()
    episode = raw_input("Ingrese el episodio de One Piece a descargar: ")
    url = "https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_%28season_17%29"
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    th = soup.findAll("th", {"id":"ep"+episode})
    for tr in soup("tr"):
        tag = tr.findAll("th")
        if tag == th:
            td = tr.findChildren("td")        
    fecha = str(td[1])[4:-5]
    today = date.today() + timedelta(days=1)
    today = today.strftime("%B %d, %Y")
    if fecha == today:
        if int(str(datetime.today().time())[:2]) >= 21:
             download()
        else:
            print "Intente despues de las 9:00 p.m."
    else:
        print "El episodio se estrenara en la fecha: " + fecha

if __name__ == "__main__":
    main()
