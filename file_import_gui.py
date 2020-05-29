from tkinter.filedialog import askopenfilename
import tkinter as tk
import csv


class FileImportGUI():
	file_paths = []
	def __init__(self):
		self.window = tk.Tk()
		self.window.columnconfigure([0,1], minsize=150)
		self.window.rowconfigure([0,1,2,3,4,5,6], minsize=50)
		self.window.title("Import Files")
		
		instuction_label1 = tk.Label(master=self.window, width=100, relief="raised", justify="center")
		instuction_label1.grid(row=0, column=0, padx=10, sticky="e")
		instuction_label1.configure(text="Select the Phrases text file")

		self.phrases_filepath_label = tk.Label(master=self.window, width=100, relief="ridge", justify="left")
		self.phrases_filepath_label.grid(row=1, column=0, padx=10, sticky="e")
		self.phrases_filepath_btn = tk.Button(master=self.window, text="Browse", command=self.getPhraseFilePath)		
		self.phrases_filepath_btn.grid(row=1, column=1, pady=10)
		
		instuction_label2 = tk.Label(master=self.window, width=100, relief="raised", justify="center")
		instuction_label2.grid(row=2, column=0, padx=10, sticky="e")
		instuction_label2.configure(text="Select the User Profile text file")
		 
		self.user_profile_filepath_label = tk.Label(master=self.window, width=100, relief="ridge", justify="left")
		self.user_profile_filepath_label.grid(row=3, column=0, padx=10, sticky="e")
		self.user_profile_filepath_btn = tk.Button(master=self.window, text="Browse", command=self.getUserProfFilePath)
		self.user_profile_filepath_btn.grid(row=3, column=1, pady=10)
		
		instuction_label3 = tk.Label(master=self.window, width=100, relief="raised", justify="center")
		instuction_label3.grid(row=4, column=0, padx=10, sticky="e")
		instuction_label3.configure(text="Select the Ig Posts text file")
		 
		self.posts_filepath_label = tk.Label(master=self.window, width=100, relief="ridge", justify="left")
		self.posts_filepath_label.grid(row=5, column=0, padx=10, sticky="e")
		self.posts_filepath_btn = tk.Button(master=self.window, text="Browse", command=self.getPostsFilePath)
		self.posts_filepath_btn.grid(row=5, column=1, pady=10)

		self.submit_btn = tk.Button(master=self.window, text="Submit", command=self.submit)
		self.submit_btn.grid(row=6, column=0, pady=10)


		self.window.mainloop()

	def getPhraseFilePath(self):
		phrases_filename = askopenfilename()
		self.phrases_filepath_label.configure(text=phrases_filename)
		self.file_paths.append(['phrases_filename,'+phrases_filename])

	def getUserProfFilePath(self):
		userprofile_filename = askopenfilename()
		self.user_profile_filepath_label.configure(text=userprofile_filename)
		self.file_paths.append(['userprofile_filename,'+userprofile_filename])

	def getPostsFilePath(self):
		posts_filename = askopenfilename()
		self.posts_filepath_label.configure(text=posts_filename)
		self.file_paths.append(['posts_filename,'+posts_filename])

	def submit(self):
		if self.file_paths:
			txtfile = open('filepaths.txt', 'w')
			newline = '\n'
			for i in range(len(self.file_paths)):
				if i == len(self.file_paths)-1:
					newline = ''
				txtfile.writelines(self.file_paths[i]+[newline])
		self.window.destroy()


FileImportGUI()