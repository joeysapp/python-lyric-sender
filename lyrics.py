import random
import subprocess
import time
import sys
import os
import urllib2
import json
from PyLyrics import *
from bs4 import BeautifulSoup
import string

def lastfm():
    response = urllib2.urlopen('key here')
    data = json.load(response)
    song = data['recenttracks']['track'][0]
    song_name = song['name']
    artist = song['artist']['#text']
    return song_name, artist

def songname():
    response = urllib2.urlopen('key here')
    data = json.load(response)
    song = data['recenttracks']['track'][0]
    song_name = song['name']
    artist = song['artist']['#text']
    return "I am currently listening to " + song_name + " by " + artist + "."


def lyricschoice(num):
    lyrics = PyLyrics.getLyrics(str(lastfm()[1]), str(lastfm()[0]))
    lyrics.strip("\n")
    gerp = lyrics.split('\n')
    gerp = filter(None, gerp)
    choices = []
    for i in range(0, num):
        new_pick = random.choice(gerp)
        gerp.remove(new_pick)
        new_pick.lower()
        choices.append(new_pick.lower())
    return choices

def lyricsrand():
    lyrics = PyLyrics.getLyrics(str(lastfm()[1]), str(lastfm()[0]))
    lyrics.strip("\n")
    gerp = lyrics.split('\n')
    gerp = filter(None, gerp)
    pick = random.choice(gerp).lower()
    for c in string.punctuation:
        pick = pick.replace(c, "")
    return pick

def lyrics():
    lyrics = PyLyrics.getLyrics(str(lastfm()[1]), str(lastfm()[0]))
    lyrics.strip("\n")
    gerp = lyrics.split('\n')
    gerp = filter(None, gerp)
    allg = []
    for line in gerp:
        for c in string.punctuation:
            line = line.replace(c, "")
        allg.append(line.lower())
    return allg

def lyricsGUI():
    stat = True
    ly = lyrics()
    #for p in ly: print p
    for i in range(0, len(ly)):
        print i, ly[i]
    while(stat == True):
        foo = int(raw_input('> '))
        sendtext(ly[foo].replace("'", "'\\''"))

def sendtext(grep):
        cmdSend = """osascript -e 'tell application "Adium" to send the active chat message "%s"'""" % grep
        subprocess.Popen(cmdSend, shell=True).wait()
