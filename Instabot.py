from instabot import Bot
import argparse
import os
from creds import *



class Instabot:
	def __init__(self):
		self.username = USERNAME
		self.password = PASSWORD
		self.bot = Bot()
		self.bot.login(username=self.username, password=self.password)
		self.followers = self.bot.get_user_followers(USERNAME)
		self.following = self.bot.get_user_following(USERNAME)
	def print_unfollowers(self):
		for elem in self.following:
			if elem in self.followers:
				pass
			else:
				user_name = self.bot.get_username_from_user_id(elem)
				print(user_name)

	def print_unfollowed_followers(self):
		for elem in self.followers:
			if elem in self.following:
				pass
			else:
				user_name = self.bot.get_username_from_user_id(elem)
				print(user_name)

	def unfollow_unfollowers(self):
		for elem in self.following:
			if elem in self.followers:
				pass
			else:
				user_name = self.bot.get_username_from_user_id(elem)
				self.bot.unfollow(str(user_name))

	def follow_followers(self):
		for elem in self.followers:
			if elem in self.following:
				pass
			else:
				user_name = self.bot.get_username_from_user_id(elem)
				self.bot.follow(str(user_name))
	def upload_photo(self, path, caption):
		self.bot.upload_photo(path, caption=str(caption))
if __name__ == '__main__':
	instabot = Instabot()
	instabot.print_unfollowers()
	instabot.print_unfollowed_followers()
	os.system('del /Q config')