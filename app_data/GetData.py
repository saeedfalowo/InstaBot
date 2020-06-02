class GetData():
	f = open("filepaths.txt","r")
	filepaths = f.read()
	filepaths_list = filepaths.split("\n")

	phrases_filename_split = filepaths_list[0].split(",")
	phrases_filename = phrases_filename_split[1]

	userprof_filename_split = filepaths_list[1].split(",")
	userprof_filename = userprof_filename_split[1]

	posts_filename_split = filepaths_list[2].split(",")
	posts_filename = posts_filename_split[1]

	"""print("phrases file path: ", phrases_filename)
				print("userprof file path: ", userprof_filename)
				print("ig_posts file path: ", posts_filename)"""

	def GetListData(self):
		phrase_list 	= self.ExtractPhrases()
		user_login_list = self.ExtractUsersCreds()
		ig_posts_list 	= self.ExtractIgPosts()
		users_indx_list = self.ExtractUserIndex()

		return phrase_list, user_login_list, ig_posts_list, users_indx_list

	def ExtractPhrases(self):
		# Extract phrases from the phrases txt file
		f = open(self.phrases_filename,"r")
		phrases = f.read().encode("cp1252").decode()
		# print("Number of character in the text file: ", len(phrases))
		phrase_list = phrases.split("\n")
		# remove empty string from list
		while("" in phrase_list):
			phrase_list.remove("")

		return phrase_list

	def ExtractUsersCreds(self):
		# Extract user profiles frome the user_profile txt file
		f = open(self.userprof_filename,"r")
		user_login = f.read()
		user_login_list = user_login.split("\n")
		while("" in user_login_list):
			user_login_list.remove("")

		for i in range(len(user_login_list)):
			user_login_list[i]=user_login_list[i].replace(" ","")

		return user_login_list

	def ExtractIgPosts(self):
		# Extract user posts from the user_profile txt file
		f = open(self.posts_filename,"r")
		ig_posts = f.read()
		ig_posts_list = ig_posts.split("\n")
		while("" in ig_posts_list):
			ig_posts_list.remove("")

		for i in range(len(ig_posts_list)):
			ig_posts_list[i]=ig_posts_list[i].replace(" ","")
		post_links = ig_posts_list
		# print(post_links)

		return ig_posts_list

	def ExtractUserIndex(self):
		users_indx_file = open('users_indx.txt', 'r')
		users_indx = users_indx_file.read()
		users_indx_list = users_indx.split("\n")
		return users_indx_list

# print(GetData().ExtractUserIndex())
phrase_list, user_login_list, ig_posts_list, users_indx_list = GetData().GetListData()