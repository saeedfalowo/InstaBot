from  selenium import webdriver
from time import sleep
import random
# browser = webdriver.Chrome(r"C:\webdrivers\operadriver.exe")
# browser.get("http://www.baidu.com")
# sleep(10)

# post_links = ['https://www.instagram.com/p/BzOiHcPJtc6/',
# 		'https://www.instagram.com/p/BzF4uHgJI4z/',
# 		'https://www.instagram.com/p/By51dbdDh37/']

f = open("filepaths.txt","r")
filepaths = f.read()
filepaths_list = filepaths.split("\n")

phrases_filename_split = filepaths_list[0].split(",")
phrases_filename = phrases_filename_split[1]

userprof_filename_split = filepaths_list[1].split(",")
userprof_filename = userprof_filename_split[1]

posts_filename_split = filepaths_list[2].split(",")
posts_filename = posts_filename_split[1]

print("phrases file path: ", phrases_filename)
print("userprof file path: ", userprof_filename)
print("ig_posts file path: ", posts_filename)

# Extract phrases from the phrases txt file
f = open(phrases_filename,"r")
phrases = f.read().encode("cp1252").decode()
# print("Number of character in the text file: ", len(phrases))
phrase_list = phrases.split("\n")
# remove empty string from list
while("" in phrase_list):
	phrase_list.remove("")


# Extract user profiles frome the user_profile txt file
f = open(userprof_filename,"r")
user_login = f.read()
user_login_list = user_login.split("\n")
while("" in user_login_list):
	user_login_list.remove("")

for i in range(len(user_login_list)):
	user_login_list[i]=user_login_list[i].replace(" ","")


# Extract user posts frome the user_profile txt file
f = open(posts_filename,"r")
ig_posts = f.read()
ig_posts_list = ig_posts.split("\n")
while("" in ig_posts_list):
	ig_posts_list.remove("")

for i in range(len(ig_posts_list)):
	ig_posts_list[i]=ig_posts_list[i].replace(" ","")
post_links = ig_posts_list
print(post_links)

print("\n\n\n")
print("##################################################")
print("##					 STARTING				   ##")
print("##################################################")



# print(user_login_list)
# # print(user_login_splt[0], user_login_splt[1])



# exit()


########################################
rand_int_list = []

class InstaBot:
	def __init__(self,username,pwd,comment,post_link):

		self.comment = comment
		self.post_link = post_link

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
		self.driver.get(self.post_link)
		sleep(5)
		self.driver.find_element_by_xpath("//textarea[@placeholder=\"Add a comment…\"]")\
			.click()
		sleep(2)

		self.driver.find_element_by_xpath("//textarea[@placeholder=\"Add a comment…\"]")\
			.send_keys(self.comment)
		self.driver.find_element_by_xpath('//button[@type="submit"]')\
			.click()
		sleep(5)

for h in range(len(post_links)):
	# for i in range(len(user_login_list)):
	for i in range(2):
		user_login_splt = user_login_list[i].split(",")

		for j in range(len(phrase_list)):
			rand_int = random.randint(0,len(phrase_list)-1)
			if rand_int not in rand_int_list:
				rand_int_list.append(rand_int)
				comment = phrase_list[rand_int]
				break

		print("Username: %s \nPassword: %s" %(user_login_splt[0], user_login_splt[1]))
		exit()
		InstaBot(user_login_splt[0], user_login_splt[1], comment, post_links[h])
		sleep(10)