from tkinter import ttk
from ttkthemes import ThemedStyle
import tkinter as tk

class keywordFileViewer(ttk.Frame):	
	def __init__(self, master, kfile_contents):
		super().__init__(master)
		self.master = master
		self.grid(row=1, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)
		self.kfile_contents=kfile_contents
		self.createWidgets()
		
			
	def createWidgets(self):					
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.text = tk.Text(self, background='white', relief='flat')		# display contents of keyword file
		self.text.insert('1.0', self.kfile_contents)
		self.text.configure(state='disabled')
		self.text.grid(row=0, column=0, sticky='nwes')
			
			
		self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)
		self.scrollbar.grid(row=0, column=0, sticky='nse')			
			
		self.text.configure(yscrollcommand=self.scrollbar.set)
	
