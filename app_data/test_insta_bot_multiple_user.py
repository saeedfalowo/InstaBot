from  selenium import webdriver
from time import sleep
import random

# browser = webdriver.Chrome(r"C:\webdrivers\operadriver.exe")
# browser.get("http://www.baidu.com")
# sleep(10)

# post_links = ['https://www.instagram.com/p/BzOiHcPJtc6/',
# 		'https://www.instagram.com/p/BzF4uHgJI4z/',
# 		'https://www.instagram.com/p/By51dbdDh37/']


print("\n\n\n")
print("##################################################")
print("##					 STARTING				   ##")
print("##################################################")

# initialize list variables
rand_int_phrases_list 	= []
rand_int_users_list 	= []

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


class RunInstBot:
	def __init__(self):
		import GetData

		phrase_list 	= GetData.phrase_list
		user_login_list = GetData.user_login_list
		ig_posts_list 	= GetData.ig_posts_list
		users_indx_list	= GetData.users_indx_list
		# print(users_indx_list[0])
		# print(users_indx_list==[''])

		user_indx_file = open('users_indx.txt', 'a+')

		if (users_indx_list != [''] and len(users_indx_list) >= len(user_login_list)*10):
			open('users_indx.txt', 'w').close()
			users_indx_list = ['']

		# Find out how many users are registered for commenting
		num_users = len(user_login_list)
		num_comments = len(phrase_list)

		for h in range(len(ig_posts_list)): # loop through all the instagram posts

			for i in range(len(user_login_list)): # loop through all the users we have
			# for i in range(2):
				user_login_splt = user_login_list[i].split(",")
				# rand_int_users = random.randint(0,len(user_login_list)-1)
				nxt_com_wait = random.randint(10,120)

				# while rand_int_users not in rand_int_users_list:
				# 	rand_int_users = random.randint(0,len(user_login_list)-1)
				
				# rand_int_users_list.append(rand_int_users)

				if users_indx_list == ['']: # if the users_indx file is empty?
					# Select a user at random (random int index) 
					rand_int_users = random.randint(0,len(user_login_list)-1)
					users_indx_list[0] = str(rand_int_users)
					spacer = ''

				else:
					nxt_int = True
					spacer = '\n'

					while nxt_int == True:
						rand_int_users = random.randint(0,len(user_login_list)-1)
						print('lenght of users_indx_list: ', len(users_indx_list))
						print(users_indx_list)
						# print('rand_int_users: ', rand_int_users)

						if str(rand_int_users) in users_indx_list:
							cnt = 0
							for k in users_indx_list:
								if k==str(rand_int_users):
									cnt+=1

							# print('rand_int_users: ', rand_int_users)
							# print('number of %s in the users_indx_list: %s' %(str(rand_int_users), str(cnt)))
							# user_no_comments = len([j for j in users_indx_list if j==str(rand_int_users)])
							# user_no_comments = len([j for j in range(len(users_indx_list)) if users_indx_list[j]==str(rand_int_users)])
							# NameError: name 'rand_int_users' is not defined ----!!!! WHY !!!!----

							# if user_no_comments < 10:
							if cnt < 10:
								nxt_int = False
						else:
							nxt_int = False


					users_indx_list.append(str(rand_int_users))
					# if len(rand_int_users_list) == len(user_login_list):
					# 	rand_int_users_list = []

				for j in range(len(phrase_list)):
					rand_int_phrases = random.randint(0,len(phrase_list)-1)
					if rand_int_phrases not in rand_int_phrases_list:
						rand_int_phrases_list.append(rand_int_phrases)
						comment = phrase_list[rand_int_phrases]
						break

				print("Username:	%s \nPassword:	%s \nComment:	%s" %(
					user_login_splt[0], user_login_splt[1], comment)
				)

				# exit()
				# InstaBot(user_login_splt[0], user_login_splt[1], comment, ig_posts_list[h])
				user_indx_file.writelines(spacer)
				user_indx_file.writelines(str(rand_int_users))
				print(users_indx_list)
				print('Sleeping for %s seconds...\n' % nxt_com_wait)
				sleep(nxt_com_wait)

RunInstaBot()