from tkinter import ttk
from ttkthemes import ThemedStyle
import tkinter as tk
from tkinter import filedialog
from file_view import FileViewer			# tkinter frame to show file
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from histogram import HistViewer
from stats import ShowStats
from keywords_lines import ShowKeywordlinesViewer
from keywords_fileview import keywordFileViewer


class RootFrame(ttk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.master = master
		master.title("Text Analyzer")		# title bar
		self.filename=''			# contains the contents of the data file
		self.kfilename=''			# contains the contents of the keyword file
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
		self.choose_button.grid(row=2, column=1, padx=5, pady=5)
		

		# keyword button
		self.keyword_button = ttk.Button(self, text="Choose keyword file...", command = self.ChooseKeywordFileAction)
		self.keyword_button.grid(row=2, column=2, padx=5, pady=5)
		#keyword button 

		
		self.panel=ttk.Frame(self)
		self.panel.grid(row=1, column=0, sticky='w')
		
		self.show_file = ttk.Button(self.panel, text="Show datafile", command = self.ShowFile)
		self.show_file.grid(row=0, column=0, sticky='nsew', pady=10)
		
		self.show_stats = ttk.Button(self.panel, text="Show Stats", command = self.ShowStats)
		self.show_stats.grid(row=1, column=0, sticky='nsew', pady=10)
		
		self.show_hist = ttk.Button(self.panel, text="Show Histogram", command = self.ShowHist)
		self.show_hist.grid(row=2, column=0, sticky='nsew', pady=10)
				
		self.refreshButton = ttk.Button(self.panel, text = "Refresh", command = self.Refresh)
		self.refreshButton.grid(row=3, column=0, sticky='nsew', pady=10)
		
		self.show_keywordlines = ttk.Button(self.panel, text="Show keyword lines", command = self.ShowKeywordlines)	#show_keyword_lines Button
		self.show_keywordlines.grid(row=4, column=0, sticky='nsew', pady=10)

		self.show_keywordfile = ttk.Button(self.panel, text="Show keyword file", command = self.Showkeywordfile) #show keyword file button
		self.show_keywordfile.grid(row=5, column=0, sticky='nsew', pady=10)

	
		
		
	def ChooseFileAction(self, event=None):			# event handler for choose file
		self.filename = filedialog.askopenfilename()
		if(self.filename!=() and self.filename!=''):
			ind= self.filename.rfind('/')
			self.choose_button["text"]='File: '+self.filename[ind+1:]
		else: self.filename=''
		
		self.ShowFile()


	def ChooseKeywordFileAction(self, event=None):		#event handler for choose keyword file
		self.kfilename = filedialog.askopenfilename()
		if(self.kfilename!=() and self.kfilename!=''):
			ind= self.kfilename.rfind('/')
			self.keyword_button["text"]='File: '+self.kfilename[ind+1:]
		else: self.kfilename=''
		
		self.ShowFile()



	def ShowFile(self, event=None):				# event handler for show datafile
		if(self.window.winfo_exists()):			# to remove old window
			self.window.grid_forget()
			self.window.destroy()
		
	
		self.header["text"]='DataFile'

		if(self.filename!=''):
			m_file  = open(self.filename, 'r', errors='ignore')
			self.file_contents = m_file.read()
			self.window=FileViewer(self, self.file_contents)	# initialise frame to show file	
			m_file.close()
			
		else:
			self.header["text"] = 'No file chosen!'
			self.window=FileViewer(self, '')
			
	def Showkeywordfile(self, event=None):
		if(self.window.winfo_exists()):			# to remove old window
			self.window.grid_forget()
			self.window.destroy()
		
	
		self.header["text"]='Keyword Data File'

		if(self.kfilename!=''):
			km_file  = open(self.kfilename, 'r', errors='ignore')
			self.kfile_contents = km_file.read()
			self.window=keywordFileViewer(self, self.kfile_contents)	# initialise frame to show keyword file	
			km_file.close()
			
		else:
			self.header["text"] = 'No file chosen!'
			self.window=keywordFileViewer(self, '')

		
	def ShowStats(self, event=None):					
		if(self.window.winfo_exists()):

			self.window.grid_forget()
			self.window.destroy()
			
		self.header["text"]='Word Stats'

		if(self.filename!=''):
			m_file = open(self.filename,'r', errors = 'ignore')
			self.file_contents = m_file.read()
			self.window = ShowStats(self, self.file_contents)
			m_file.close()
		
		else:
			self.header["text"] = "No File Chosen !"
			self.window = ShowStats(self,'')

		# self.window = ShowStats(self, self.file_contents)		# initialise frame to show stats

		
	def ShowKeywordlines(self, event=None):					
		if(self.window.winfo_exists()):

			self.window.grid_forget()
			self.window.destroy()
			
		self.header["text"]='keywords containing lines'

		if(self.kfilename!='' and self.kfilename!=''):
			m_file = open(self.filename,'r', errors = 'ignore')
			self.file_contents = m_file.read()
			m_kfile = open(self.kfilename,'r', errors = 'ignore')
			self.kfile_contents = m_kfile.read()
			self.window = ShowKeywordlinesViewer(self, self.file_contents, self.kfile_contents)
			m_kfile.close()
			m_file.close()
		
		else:
			self.header["text"] = "No File Chosen !"
			self.window = ShowKeywordlinesViewer(self,'')
		

		
	def ShowHist(self, event=None):
		if(self.window.winfo_exists()):

			self.window.grid_forget()
			self.window.destroy()
		
		self.header["text"]='Histogram'

		if self.filename!='':
			self.window = HistViewer(self,self.filename)
		else:
			self.header['text'] = 'No File Chosen!'
			self.window = FileViewer(self,'')
		
		#self.window = ShowHistogram(self, self.file_contents)		# initialise frame to show historgam
		
	
	def Refresh(self):
		if (self.window.winfo_exists()):
			self.window.destroy()						#destroy the current window to refresh





root=tk.Tk()
root.geometry("1200x600")
root.configure(background='#eff0f1')
style=ThemedStyle(root)
style.set_theme('breeze')
style.configure('TButton', foreground = 'black')


my_gui = RootFrame(root)


root.mainloop()

