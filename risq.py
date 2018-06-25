# Reddit Imgur Squasher - risq.py
# A commandline python script to grab images from subreddit/submissions (even if imgur links are attached to the post)

# python3 risq.py [subreddit (without "r/")] [limit (number < 100 preferable)]
# Created by r/nogtx aka Saurabh K : 26-06-2018

import praw
import requests
import sys
import os.path

from praw_creds import client_id, client_secret, password, user_agent, username


try:
    reddit = praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            password=password,
                            user_agent=user_agent,
                            username=username)

    subr_name = sys.argv[1]
    thr_limit = int(sys.argv[2])
    
    if thr_limit < 10:
        print('Limit should be greater than 10. Look out for stickied posts!')
        print('Setting default limit (10)')
        thr_limit = 10

    subreddit=reddit.subreddit(subr_name)
    submissions = subreddit.hot(limit=thr_limit)

    dir_name = 'r_' + subr_name
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    os.chdir(dir_name)

    img_count = 0
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
                img_count += 1
                print('[{0}]'.format(post.url), filename, 'saved!')
    
    print('Images saved ({0}) in {1}'.format(img_count, dir_name))
    
except Exception as e:
    print('An error occurred!')
    print('python3 risq.py [subreddit (without "r/")] [limit (number < 100 preferable)]')
