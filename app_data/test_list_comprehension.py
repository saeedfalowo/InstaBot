import random

users_indx_list = ['3', '4', '2', '1', '0']
rand_int_users = 3


nxt_int = True
spacer = '\n'
cnt = 0

for i in range(10):
	while nxt_int == True:
		rand_int_users = random.randint(0,5-1)
		print(rand_int_users)

		if str(rand_int_users) in users_indx_list:
			user_no_comments = len([j for j in users_indx_list if j==str(rand_int_users)])
			print(user_no_comments)
			# nxt_int = False
			# cnt+=1
			# if cnt >= 10:
			# 	exit()
			if user_no_comments < 10:
				nxt_int = False
		else:
			nxt_int = False