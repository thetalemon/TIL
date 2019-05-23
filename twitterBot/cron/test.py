#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import datetime
from slacklogin import post2slack

post2slack(datetime.now().strftime("%H") + '時だよ')
