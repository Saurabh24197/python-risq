# From this tutorial : https://www.youtube.com/watch?v=XmOA1k4RTrc

import praw

reddit = praw.Reddit(client_id = '',
 client_secret = '',
   password = '',
    user_agent = '',
     username = '')

subreddit = reddit.subreddit('news')

for comment in subreddit.stream.comments():
    try:
        parent_id = str(comment.parent())
        origin = reddit.comment(parent_id)
        print('Parent:')
        print(origin.body)

        print('Reply:')
        print(comment.body)
    except praw.exceptions.PRAWException as e:
        pass

# for submission in subreddit.stream.submissions():
#     try:
#         print(submission.body)
#     except Exception as e:
#         print(str(e))