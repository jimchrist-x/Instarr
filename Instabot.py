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
		pass
	def follow_followers(self):
		pass

if __name__ == '__main__':
	instabot = Instabot()