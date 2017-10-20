import praw
import config
import time
import os
import string

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
        #The subreddit function determines which subreddit to reply to using the bot.
        #The comments function determines the amount of recent comments to look through.
    for comment in r.subreddit('lakers').stream.comments():
        if comment.id not in replied_comments:
            for word in comment.body.split():
                if word[0] == '!':
                    player = word[1:]
                    URL = get_player_url(player)
                    comment.reply(URL)
                    print("Replied to comment " + comment.id)

                    #Adds to the replied-to-comments text file
                    replied_comments.add(comment.id)
                    with open ("rpldcmmnts.txt", "a") as txt:
                        txt.write(comment.id + "\n")
    #Sleeps for a set amount of time every run through
    print("Sleeping for 8 seconds...")

def get_player_url(name):
    second = False
    iterator = 0
    lastNameIndex = 0
    playerInitial = ''
    playerIDF = name[0:2].lower()
    for c in name:
        if c in string.ascii_uppercase:
            second = True
        if c in string.ascii_uppercase and second == True:
            lastNameIndex = iterator
            playerInitial = c.lower()

        iterator += 1

    lastName = name[lastNameIndex:]

    if len(lastName) > 4:
        playerIDL = lastName[:5].lower()
    else:
        playerIDL = lastName.lower()

    playerID = playerIDL + playerIDF

    URL = "https://www.basketball-reference.com/players/" + playerInitial + "/" + playerIDL + playerIDF + "/gamelog/2018"

    return URL

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
