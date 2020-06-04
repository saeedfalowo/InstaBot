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

		# assign function input variables
		self.comment = comment
		self.post_link = post_link
		# initialize web driver and launch Instagram
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
		# Post a comment on an instagram post
		self.postInstaComment()
		# Kill the web browser
		self.driver.quit()

	def postInstaComment(self):
		# Navigate the an Instagram Post
		self.driver.get(self.post_link)
		sleep(5)
		# Locate the instagram post's text field and click to activate the field
		self.driver.find_element_by_xpath("//textarea[@placeholder=\"Add a comment…\"]")\
			.click()
		sleep(2)
		# Enter the comment text into the activated comment text field
		self.driver.find_element_by_xpath("//textarea[@placeholder=\"Add a comment…\"]")\
			.send_keys(self.comment)
		# Find the submit button and click to post the comment
		self.driver.find_element_by_xpath('//button[@type="submit"]')\
			.click()
		sleep(5)


class RunInstaBot:
	def __init__(self):
		# Import the contents of the app data text files
		import GetData
		# Assign text file data to class variables
		phrase_list 	= GetData.phrase_list
		user_login_list = GetData.user_login_list
		ig_posts_list 	= GetData.ig_posts_list
		users_indx_list	= GetData.users_indx_list
		num_comments_per_user = 10
		# print(users_indx_list[0])
		# print(users_indx_list==[''])

		# Open user posts history record text file to be updated
		user_indx_file = open('users_indx.txt', 'a+')

		# If user posts history record text file is not empty and the length is greated than or equal to
		# the total number of comments posted for all users
		if (users_indx_list != [''] and len(users_indx_list) >= len(user_login_list)*num_comments_per_user):
			open('users_indx.txt', 'w').close() # clear the text file
			users_indx_list = [''] # initialize the list

		# Find out how many users are registered for commenting
		num_users = len(user_login_list)
		num_comments = len(phrase_list)

		for h in range(len(ig_posts_list)): # loop through all the instagram posts

			for i in range(len(user_login_list)): # loop through all the users we have
			# for i in range(2):
				user_login_splt = user_login_list[i].split(",") # Extract user name and password
				# rand_int_users = random.randint(0,len(user_login_list)-1)
				nxt_com_wait = random.randint(10,30) # define the next wait duration

				# while rand_int_users not in rand_int_users_list:
				# 	rand_int_users = random.randint(0,len(user_login_list)-1)
				
				# rand_int_users_list.append(rand_int_users)

				if users_indx_list == ['']: # if the users_indx file is empty?
					# Select a user at random (random int index) 
					rand_int_users = random.randint(0,len(user_login_list)-1) # select user profile index at random
					users_indx_list[0] = str(rand_int_users) # initialize the first index of the user posts history record text file
					spacer = '' # declare the text file spacer before writing the user index

				else:
					nxt_int = True # declare while loop condition
					spacer = '\n' # declare the text file spacer before writing the user index

					# The while loop will keep generating a new user profile index until an index that has not appeared more
					# than a certain number of times is generated
					while nxt_int == True:
						rand_int_users = random.randint(0,len(user_login_list)-1) # select user profile index at random
						# print('lenght of users_indx_list: ', len(users_indx_list))
						# print(users_indx_list)
						# print('rand_int_users: ', rand_int_users)

						if str(rand_int_users) in users_indx_list: # if the generated index exists in the previously used user index list
							cnt = 0 # initialize counter variable
							# increment the counter everytime the same index as the newly generated user index is found
							for k in users_indx_list:
								if k==str(rand_int_users):
									cnt+=1

							# print('rand_int_users: ', rand_int_users)
							# print('number of %s in the users_indx_list: %s' %(str(rand_int_users), str(cnt)))
							# user_no_comments = len([j for j in users_indx_list if j==str(rand_int_users)])
							# user_no_comments = len([j for j in range(len(users_indx_list)) if users_indx_list[j]==str(rand_int_users)])
							# NameError: name 'rand_int_users' is not defined ----!!!! WHY !!!!----

							# if the number of the newly generated index is less than the set maximum number of comments per user
							# if user_no_comments < 10:
							if cnt < num_comments_per_user: 
								nxt_int = False # break out of the while loop

						else: # else if the generated index does not exist in the previously used user index list
							nxt_int = False # break out of the while loop


					users_indx_list.append(str(rand_int_users)) # added newly generated user index to the previously used user index list
					# if len(rand_int_users_list) == len(user_login_list):
					# 	rand_int_users_list = []

				# Loop through all the unique comments in the comments list
				for j in range(len(phrase_list)):
					rand_int_phrases = random.randint(0,len(phrase_list)-1) # select comment index at random
					if rand_int_phrases not in rand_int_phrases_list: # if the comment has not been used previously
						rand_int_phrases_list.append(rand_int_phrases) # added newly generated comment index to the previously used comment index list
						comment = phrase_list[rand_int_phrases] # extract the unique comment from the phrase list
						break

				print("Username:	%s \nPassword:	%s \nComment:	%s" %(
					user_login_splt[0], user_login_splt[1], comment)
				)

				# exit()
				# Run InstaBot to login to the selected user profile and post the unique comment to the defined instagram post
				# InstaBot(user_login_splt[0], user_login_splt[1], comment, ig_posts_list[h])

				# Write user index to the user index text file
				user_indx_file.writelines(spacer)
				user_indx_file.writelines(str(rand_int_users))
				print(users_indx_list)
				print('Sleeping for %s seconds...\n' % nxt_com_wait)
				sleep(nxt_com_wait) # wait

RunInstaBot()
# RunInstaBot()
# RunInstaBot()
