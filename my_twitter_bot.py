import tweepy
import time
print("this is twitter bot")

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file_name = 'last_seen_id.txt'

def retrieve_last_seen_id(filename):
        fread = open(file_name,'r')
        last_seen_id = int(fread.read().strip())
        fread.close()
        return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
        fwrite = open(file_name, 'w')
        fwrite.write(str(last_seen_id))
        fwrite.close()
        return

mentions = api.mentions_timeline(last_seen_id,tweet_mode = 'extend')
last_seen_id = retrieve _last_seen_id(file_name)

for mention in reversed(mentions):
	print(str(mention.id) + '-' + mention.text)
	last_seen_id = mention.id
	store_last_seen_id(last_seen_id,file_name)
	if '#hello' in mention.fulltext.lower():
		print("found #hello, responding back...")
