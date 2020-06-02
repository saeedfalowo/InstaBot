import random
import csv
from time import sleep

f = open("1-FRASES TXT - CDEXDITAL DO TESTE.txt","r")
phrases = f.read().encode("cp1252").decode()
# print("Number of character in the text file: ", len(phrases))
phrase_list = phrases.split("\n")
# remove empty string from list
while("" in phrase_list):
	phrase_list.remove("")

print(phrase_list[-4])

# with open('db.csv', 'a+', newline='') as f:
# 	csv_writer = csv.writer(f)
# 	csv_writer.writerow([1])

rand_int_list = []
for i in range(20):
	rand_int = random.randint(0,5)
	if rand_int not in rand_int_list:
		rand_int_list.append(rand_int)
		print(rand_int)
		sleep(1)