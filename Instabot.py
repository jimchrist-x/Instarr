from instabot import Bot
import argparse
from creds import *
class Instabot:
	def __init__(self):
		self.username = USERNAME
		self.password = PASSWORD
		self.bot = Bot()
		self.bot.login(username=self.username, password=self.password)
	def print_unfollowers(self):
		followers = self.bot.get_user_followers(USERNAME)
		following = self.bot.get_user_following(USERNAME)
		for elem in following:
			if elem in followers:
				pass
			else:
				user_name = self.bot.get_username_from_user_id(elem)
				print(user_name)
	def print_unfollowed_followers(self):
		pass
	def unfollow_unfollowers(self):
		pass
	def follow_followers(self):
		pass

if __name__ == '__main__':
	instabot = Instabot()
	instabot.print_unfollowers()