# Reddit Imgur Squasher - risq.py
# A commandline python script to grab images from subreddit/submissions (even if imgur links are attached to the post)

# python3 risq.py [subreddit-name (without "r/")] [threshold-limit (number < 100 preferable)]

# Created by r/nogtx aka Saurabh K

import praw
import requests
import sys
import os.path

from praw_creds import client_id, client_secret, password, user_agent, username

reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        password=password,
                        user_agent=user_agent,
                        username=username)


subr_name = sys.argv[1]
thr_limit = int(sys.argv[2])

try:
    subreddit=reddit.subreddit(subr_name)
    submissions = subreddit.hot(limit=thr_limit)

    for post in submissions:
        if not post.stickied:
            if not (('https://i.redd.it/' in post.url) or ('https://i.imgur.com/' in post.url)):
                print (post.url, ' is not a reddit/imgur image')
                continue;

            filename = post.url.replace('https://i.redd.it/', '')
            filename = filename.replace('https://i.imgur.com/','')

            if os.path.isfile(filename):
                print('[{0}]'.format(post.url), filename, 'already exists!')
                continue

            post_img = requests.get(post.url).content
            with open(filename, 'wb') as handler:
                handler.write(post_img)
                # post.mark_visited()
                print('[{0}]'.format(post.url), filename, 'saved!')
except Exception as e:
    print('python3 risq.py [subreddit-name (without "r/")] [threshold-limit (number < 100 preferable)]')
    print('Errors could occur \n1. if the sub-reddit doesn\'t exist')
    print('2. due to connection time-out')
