from instabot import Bot
import argparse
import os
import tkinter as tk
from tkinter import messagebox
logged_in = False
class Instabot:
	def __init__(self):
		os.system('del /Q config')
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


class GUI:
	def LoginPage():
		def get_entries():
			global USERNAME
			global PASSWORD
			USERNAME = username.get()
			PASSWORD = password.get()
			if USERNAME == '' or PASSWORD == '':
				messagebox.showerror('Error', 'Invalid Credentials')
				username.delete(0, tk.END)
				password.delete(0, tk.END)
			else:
				global logged_in
				logged_in = True
				login.destroy()
		login = tk.Tk()
		login.title('Login')
		login.geometry("200x200")
		login.resizable(0, 0)
		tk.Label(login, text="Enter instagram login credentials").pack()
		tk.Label(login, text="").pack()
		tk.Label(login, text="Username").pack()
		username = tk.Entry(login, textvariable="username")
		username.pack()
		tk.Label(login, text="").pack()
		tk.Label(login, text="Password").pack()
		password = tk.Entry(login, textvariable="password", show='*')
		password.pack()
		tk.Label(login, text="").pack()
		tk.Button(login, text="Login", width=10, height=1, command=get_entries).pack()
		login.mainloop()
	def main():
		root = tk.Tk()
		root.title('Instarr')
		root.geometry('1000x600')
		root.resizable(0, 0)
		tk.Frame(root, bg='lightgrey').place(x=0, y=0, height=1000, width=250)
		tk.Frame(root, bg='red').place(x=250, y=0, height=1000, width=250)
		tk.Frame(root, bg='blue').place(x=500, y=0, height=1000, width=250)
		tk.Frame(root, bg='yellow').place(x=750, y=0, height=1000, width=250)
		tk.Button(root, text='Get unfollowers', command=instabot.print_unfollowers).place(x=100, y=50)
		root.mainloop()
if __name__ == '__main__':
	#instabot.print_unfollowers()
	#instabot.print_unfollowed_followers()
	GUI.LoginPage()
	if logged_in:
		instabot = Instabot()
		GUI.main()
