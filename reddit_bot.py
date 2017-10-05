import praw
import config
import time
import os

#Logs the bot in
def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "lakersk19's Lakers bot v0.1")
    print("Logged in!")
    return r

#Runs bot using the saved comments text file
def run_bot(r, replied_comments):
     """
        The subreddit function determines which subreddit to reply to using the bot.
        The comments function determines the amount of recent comments to look through.
     """
    for comment in r.subreddit('test').comments(limit=25):
        #Looks for target keyword
        if "24" in comment.body and comment.id not in replied_comments:
            print("String with \"24\" found!")
            comment.reply("8")
            print("Replied to comment " + comment.id)

            #Adds to the replied-to-comments text file
            replied_comments.add(comment.id)
            with open ("rpldcmmnts.txt", "a") as txt:
                txt.write(comment.id + "\n")
    #Sleeps for a set amount of time every run through
    print("Sleeping for 8 seconds...")
    time.sleep(8)

#Returns the replied-to-comments text file
def get_saved_comments():
    if not os.path.isfile("rpldcmmnts.txt"):
        replied_comments = set()
    else:
        with open("rpldcmmnts.txt", "r") as txt:
            replied_comments = set()
            for comment_id in txt.readlines():
                replied_comments.add(comment_id.strip())

    return replied_comments

#Tester, post in /r/test to test the bot
r = bot_login()
replied_comments = get_saved_comments()
print(replied_comments)

#Runs until keyboard interrupts
while(True):
    run_bot(r, replied_comments)
