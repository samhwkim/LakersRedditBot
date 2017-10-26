import praw
import config
import time
import os
import string
import scraper
import tablemaker

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
def run_bot(r, replied_comments, lakersRoster):
    """
    The subreddit function determines which subreddit to reply to using the bot.
    The comments function determines the amount of recent comments to look through.
    """
    for comment in r.subreddit('lakers').stream.comments():
        #Prevents spamming multiply replies to the same comment.
        if comment.id not in replied_comments:
            #Splits a comment body word by word.
            for word in comment.body.split():
                #Looks for a call to the bot ('!')
                if word[0] == '!':
                    player = word[1:]
                    #Checks that the call to bot was intentional and not a grammatical error
                    if player in lakersRoster:
                        URL = get_player_url(player)
                    elif player == "LarryNance" or "LarryNanceJr":
                        URL = "https://www.basketball-reference.com/players/n/nancela02.html"
                    elif player == "KCP":
                        URL = "https://www.basketball-reference.com/players/c/caldwke01.html"
                    playerStats = scraper.get_scraped_stats(URL)
                    table = tablemaker.get_stats_table(playerStats)
                    while(True):
                        try:
                            comment.reply(table)
                            print("Replied to comment " + comment.id)
                            #Adds to the replied-to-comments text file
                            replied_comments.add(comment.id)
                            with open ("rpldcmmnts.txt", "a") as txt:
                                txt.write(comment.id + "\n")
                            break
                        except APIException:
                            time.sleep(5)

#Takes in the ! command with the player name and converts it into a basketball reference URL.
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

    URL = "https://www.basketball-reference.com/players/" + playerInitial + "/" + playerIDL + playerIDF + "01.html"

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

#Returns the Lakers roster
def get_roster():
    if not os.path.isfile("roster.txt"):
        roster = set()
    else:
        with open("roster.txt", "r") as txt:
            roster = set()
            for player in txt.readlines():
                roster.add(player.strip())

    return roster

#Main testing code post in /r/test to test the bot
r = bot_login()
repliedComments = get_saved_comments()
lakersRoster = get_roster()

#Runs until keyboard interrupts
while(True):
    run_bot(r, repliedComments, lakersRoster)
