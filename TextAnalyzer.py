from tkinter import ttk
from ttkthemes import ThemedStyle
import tkinter as tk
from tkinter import filedialog
from file_view import FileViewer	# tkinter frame to show file


class RootFrame(ttk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.master = master
		master.title("Text Analyzer")		# title bar
		self.filename=''			# contains the contents of the data file
		self.pack(fill=tk.BOTH, expand=1)		

		self.window=tk.Frame(self)
		self.createWidgets()			# call to create widgets
		
	def createWidgets(self):

		self.grid_columnconfigure(0,weight=0)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=0)
		

		self.grid_rowconfigure(0,weight=0)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=0)
		# grid weights configure
		
				
		
		self.header = ttk.Label(self, text="Please choose a file...",font="Arial 25 bold")
		self.header.grid(row=0, column=0, columnspan=3)
		self.choose_button = ttk.Button(self, text="Choose datafile...", command = self.ChooseFileAction)
		self.choose_button.grid(row=2, column=2, padx=5, pady=5)
		
		
		self.panel=ttk.Frame(self)
		self.panel.grid(row=1, column=0, sticky='w')
		
		self.show_file = ttk.Button(self.panel, text="Show datafile", command = self.ShowFile)
		self.show_file.grid(row=0, column=0, sticky='nsew', pady=10)
		
		self.show_stats = ttk.Button(self.panel, text="Show Stats", command = self.ShowStats)
		self.show_stats.grid(row=1, column=0, sticky='nsew', pady=10)
		
		self.show_hist = ttk.Button(self.panel, text="Show Histogram", command = self.ShowHist)
		self.show_hist.grid(row=2, column=0, sticky='nsew', pady=10)
				
		


		
		
	def ChooseFileAction(self, event=None):			# event handler for choose file
		self.filename = filedialog.askopenfilename()
		if(self.filename!=() and self.filename!=''):
			ind= self.filename.rfind('/')
			self.choose_button["text"]='File: '+self.filename[ind+1:]
		else: self.filename=''
		
		self.ShowFile()


	def ShowFile(self, event=None):				# event handler for show datafile
		if(self.window.winfo_exists()):			# to remove old window
			self.window.grid_forget()
			self.window.destroy()
		
	
		self.header["text"]='DataFile'

		if(self.filename!=''):
			m_file  = open(self.filename, 'r')
			self.file_contents = m_file.read()
			self.window=FileViewer(self, self.file_contents)	# initialise frame to show file	
			m_file.close()
			
		else:
			self.header["text"] = 'No file chosen!'
			self.window=FileViewer(self, '')
			
		
	def ShowStats(self, event=None):					
		if(self.window.winfo_exists()):

			self.window.grid_forget()
			self.window.destroy()
			
		self.header["text"]='Word Stats'
		
		#self.window = ShowStats(self, self.file_contents)		# initialise frame to show stats
		
		
		
	def ShowHist(self, event=None):
		if(self.window.winfo_exists()):

			self.window.grid_forget()
			self.window.destroy()
			
		self.header["text"]='Histogram'

		
		#self.window = ShowHistogram(self, self.file_contents)		# initialise frame to show historgam
		
	











root=tk.Tk()
root.geometry("1200x600")
root.configure(background='#eff0f1')
style=ThemedStyle(root)
style.set_theme('breeze')
style.configure('TButton', foreground = 'black')


my_gui = RootFrame(root)


root.mainloop()

