import praw
import config

def bot_login():
	print("logging in")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "let's REALLY make America great agan")
	print("logged in")
	return r

def run_bot(r):
	obtainingnumber = 0
	for comment in r.subreddit("impeachtrump").comments(limit=100):
		print("obtaining 100 comments" + str(obtainingnumber))
		obtainingnumber += 1
		if ("Trump") in comment.body:
			print("someone got told")
			comment.reply("what a [sad clown](https://www.pinterest.com/pin/531424824761032081/)")

r = bot_login()
while True:
	run_bot(r)