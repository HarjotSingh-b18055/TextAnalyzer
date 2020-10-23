from tkinter import ttk
from ttkthemes import ThemedStyle
import tkinter as tk
import os
import nltk
nltk.download('punkt')


class ShowKeywordlinesViewer(ttk.Frame):
	def __init__(self, master, file_contents, kfile_contents):
		super().__init__(master)
		self.master = master
		self.grid(row=1, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)
		self.file_contents=file_contents
		self.kfile_contents=kfile_contents
		self.createWidgets()

	def keyword_analysis(self):
		data = self.file_contents
		tokens = nltk.sent_tokenize(data)
		stat = ""
		kdata = self.kfile_contents
		keyline = kdata.split('\n')
		keyline.pop()
		for line in tokens:
			cnt = 0
			line = line.strip(os.linesep)
			words = line.split()
			for word in words:
				for i in keyline:
					if(i == word):
						cnt+=1
			if(cnt>0):
				stat += str(line)+"\n"
			cnt = 0
				
		self.stat_lines = stat
	
	def createWidgets(self):					
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.text = tk.Text(self, background='white', relief='flat', font = "Calibri 14")		# display contents of file
		self.keyword_analysis()
		self.text.insert('1.0', self.stat_lines)
		self.text.configure(state='disabled')
		self.text.grid(row=0, column=0, sticky='nwes')
		self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)
		self.scrollbar.grid(row=0, column=0, sticky='nse')			
			
		self.text.configure(yscrollcommand=self.scrollbar.set)



































