from  selenium import webdriver
from time import sleep
import random
#browser = webdriver.Chrome(r"C:\webdrivers\operadriver.exe")
# browser.get("http://www.baidu.com")
pwd = "1015Ty360"
post_links = ['https://www.instagram.com/p/BzOiHcPJtc6/',
		'https://www.instagram.com/p/BzF4uHgJI4z/',
		'https://www.instagram.com/p/By51dbdDh37/']

# Extract phrases from the phrases txt file
f = open("1-FRASES TXT - CDEXDITAL DO TESTE.txt","r")
phrases = f.read().encode("cp1252").decode()
# print("Number of character in the text file: ", len(phrases))
phrase_list = phrases.split("\n")
# remove empty string from list
while("" in phrase_list):
	phrase_list.remove("")


# Extract user profiles frome the user_profile txt file
f = open("user_profiles.txt","r")
user_login = f.read()
user_login_list = user_login.split("\n")
while("" in user_login_list):
	user_login_list.remove("")

for i in range(len(user_login_list)):
	user_login_list[i]=user_login_list[i].replace(" ","")

# print(user_login_list[0])
# user_login_splt = user_login_list[0].split(",")
# print(user_login_splt)
# print("username: ", user_login_splt[0])
# print("password: ", user_login_splt[1])
# print(www)


class InstaBot:
	rand_int_list = []
	def __init__(self,username,pwd,phrase_list,post_links):

		self.phrase_list = phrase_list
		self.post_links = post_links

		self.driver = webdriver.Chrome(r"C:\webdrivers\operadriver.exe")
		self.driver.get("https://instagram.com")
		sleep(2)

		# Enter username and password then click the login button
		self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
			.send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
			.send_keys(pwd)
		self.driver.find_element_by_xpath('//button[@type="submit"]')\
			.click()
		sleep(4)

		# Click "Not Now" for the notifications dialog box
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
			.click()
		sleep(4)

		self.postInstaComment()
		self.driver.quit()

	def postInstaComment(self):
		# Post a comment to the most recent post
		for i in range(len(self.post_links)):
			self.driver.get(self.post_links[i])
			sleep(5)
			self.driver.find_element_by_xpath("//textarea[@placeholder=\"Add a comment…\"]")\
				.click()
			sleep(2)

			for j in range(len(phrase_list)):
				rand_int = random.randint(0,len(self.phrase_list)-1)
				if rand_int not in self.rand_int_list:
					self.rand_int_list.append(rand_int)
					comment = self.phrase_list[rand_int]
					break

			self.driver.find_element_by_xpath("//textarea[@placeholder=\"Add a comment…\"]")\
				.send_keys(comment)
			self.driver.find_element_by_xpath('//button[@type="submit"]')\
				.click()
			sleep(5)

InstaBot("saeedfalowo",pwd,phrase_list,post_links)