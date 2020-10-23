import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk

class HistViewer(ttk.Frame):	
    def __init__(self, master, filename):
        super().__init__(master)
        self.master = master
        self.filename = filename
        self.grid(row=1, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)
        self.createWidgets()
		
    def make_histogram(self,frame):
        allWords = []
        fi = open('ignoredWords.txt','r')
        ignoredWords = fi.read().split()
        fi.close()
        symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        frequencies = {}
        fh = open(self.filename,'r', errors='ignore')
        for line in fh.readlines():
            words = line.split()
            for word in words:
                for i in word:
                    if i in symbols:
                        word = word.replace(i,'')
                word = word.lower()
                if len(word)>0 and (word not in ignoredWords):
                    if word not in frequencies:
                        frequencies[word] = 1
                    else:
                        frequencies[word]+=1
        fh.close()
        self.figure = Figure(figsize = (12,6), dpi = 100)
        self.plot = self.figure.add_subplot(1,1,1)
        self.plot.bar(frequencies.keys(), frequencies.values())
        self.plot.set_xticklabels(frequencies.keys(),rotation='vertical')
        self.canvas = FigureCanvasTkAgg(self.figure,frame)
        self.toolbar = NavigationToolbar2Tk(self.canvas,frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()
			
    def createWidgets(self):					
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame = ttk.Frame(self)
        self.make_histogram(self.frame)
        self.frame.grid(row = 0, column = 0, sticky = 'nwes')    
            
        # self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.histo.get_tk_widget().yview)
        # self.scrollbar.grid(row=0, column=0, sticky='nse')			
            
        # self.histo.get_tk_widget().configure(yscrollcommand=self.scrollbar.set)


































    
