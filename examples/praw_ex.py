# From this tutorial : https://www.youtube.com/watch?v=XmOA1k4RTrc

import praw

# Insert your own credentials
reddit = praw.Reddit(client_id = '',
 client_secret = '',
   password = '',
    user_agent = '',
     username = '')

subreddit = reddit.subreddit('news')
hot_python = subreddit.hot(limit = 3);

for post in hot_python:
    if not post.stickied:
        # print('Title: {}, upvotes: {}, downvotes: {}, Visited: {}'.format(
        #     post.title,
        #  post.ups,
        #  post.downs,
        #  post.visited))

        post.comments.replace_more(limit = 0)
        for comment in post.comments.list():
            print(20*'+')
            print('\tParent ID:', comment.parent())
            print('\tComment ID:', comment.id)
            print(comment.body)

            # if len(comment.replies) > 0:
            #     for reply in comment.replies:
            #         print('\t[Reply]:', reply.body)


#subreddit.subscribe()