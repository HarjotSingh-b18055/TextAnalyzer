from tkinter import ttk
from ttkthemes import ThemedStyle
import tkinter as tk

class ShowStats(ttk.Frame):
	def __init__(self, master, file_contents):
		super().__init__(master)
		self.master = master
		self.grid(row=1, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)
		self.file_contents=file_contents
		self.createWidgets()
    
	def analysis(self):
		data = self.file_contents
		words = data.split()
		stat = "The number of words in file are : "
		stat = stat + str(len(words)) + "\n"
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
