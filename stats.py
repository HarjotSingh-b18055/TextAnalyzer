from tkinter import ttk
from ttkthemes import ThemedStyle
import tkinter as tk
import os

class ShowStats(ttk.Frame):
	def __init__(self, master, file_contents):
		super().__init__(master)
		self.master = master
		self.grid(row=1, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)
		self.file_contents=file_contents
		self.createWidgets()
    
	def analysis(self):
		data = self.file_contents
		linelist = data.split('\n')
		linelist.pop()
		num_words = 0
		num_lines = 0
		num_char = 0
		num_spaces = 0
		word_freq = dict()
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		for line in linelist:
			# print(line,'\n\n')
			num_lines += 1
			line = line.strip(os.linesep)
			words = line.split()
			num_words += len(words)
			num_char += sum(1 for x in line if x not in (os.linesep,' ') )
			num_spaces += sum(1 for x in line if x in (os.linesep,' ') )
			for word in words:
				for i in word:
					if i in punctuations:
						word = word.replace(i,"")
				if word in word_freq:
					word_freq[word] +=1
				else:
					word_freq[word] = 1

		stat = " Analysis of File \n \n"
		stat = stat + " Number of lines in file are:		 " + str(num_lines)
		stat = stat + "\n Number of words in file are:		 " + str(num_words)
		stat = stat + "\n Characters (without spaces):		 " + str(num_char) 
		stat = stat + "\n Characters (with spaces):		 " + str(num_char+num_spaces)

		print(data)
		for key,values in sorted(word_freq.items(),key=lambda item: item[1],reverse=True):
			print(key," ",values)
		
		
		self.data_analysis = stat

	def createWidgets(self):					
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.text = tk.Text(self, background='white', relief='flat')		# display contents of file
		self.analysis()
		self.text.insert('1.0', self.data_analysis)
		self.text.configure(state='disabled')
		self.text.grid(row=0, column=0, sticky='nwes')
			
			
		self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)
		self.scrollbar.grid(row=0, column=0, sticky='nse')			
			
		self.text.configure(yscrollcommand=self.scrollbar.set)
