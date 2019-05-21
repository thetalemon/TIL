#!/usr/bin/env python
# -*- coding: utf-8 -*-

from login import api
from slacklogin import post2slack
import os

def create_twitter_url(id_str, screen_name):
    return 'https://twitter.com/' + str(screen_name) + '/status/' + str(id_str)

def ouputFile(outputData):
    f = open('./number.txt','w')
    f.write(outputData)
    f.close()

def readFile():
    f = open('./number.txt','r')
    text=""
    for row in f:
        text =  row.strip()
    f.close()
    return text

def main():
    tl = api.list_timeline('lemontheta', 'list', count=10)
    lastNumber=""
    if(os.path.exists("./number.txt")):
        lastNumber = readFile()
    ouputFile(str(tl[0].id))

    for status in tl:
        if str(status.id) == lastNumber :
            print("reach to last processing")
            break
        try :
            url=status.extended_entities['media'][0]['media_url']
        except:
            print("no image")
            pass #画像がないときはなにもしない
        post2slack(create_twitter_url(status.id, status.user.id))

if __name__ == "__main__":
    main()
