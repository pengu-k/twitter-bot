"""
A Twitter bot
>>  2020  <<
"""
import tweepy
import time

auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")
api = tweepy.API(auth)


FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode ='extended')
    for tweet in reversed(tweets):
        if 'help' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("hi, " + "@" + tweet.user.screen_name + " what can I help you with?", tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(15)














