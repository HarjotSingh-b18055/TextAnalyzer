import matplotlib.pyplot as plt
import numpy as np
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
        fh = open(self.filename,'r', errors='ignore')
        for line in fh.readlines():
            words = line.split()
            for word in words:
                apdWord = word
                while len(apdWord)>0 and (apdWord[-1]=='.' or apdWord[-1]==',' or apdWord[-1]==';' or apdWord[-1]==':' or apdWord[-1]=='?' or apdWord[-1]=='!' or apdWord[-1]=='\'' or apdWord[-1]=="\"" or apdWord[-1]==")" or apdWord[-1]=="]" or apdWord[-1]=="}"):
                    apdWord = apdWord[0:len(apdWord)-1]
                while len(apdWord)>0 and (apdWord[0]=='.' or apdWord[0]==',' or apdWord[0]==';' or apdWord[0]==':'or apdWord[0]=='\'' or apdWord[0]=="\"" or apdWord[0]=="(" or apdWord[0]=="[" or apdWord[0]=="{"):
                    apdWord = apdWord[1:len(apdWord)]
                apdWord = apdWord.lower()
                if len(apdWord)>0 and (apdWord not in ignoredWords):
                    allWords.append(apdWord)
        fh.close()
        frequencies = []
        uniqueWords = np.unique(allWords)
        for word in uniqueWords:
            frequencies.append(allWords.count(word))
        self.figure = Figure(figsize = (12,6), dpi = 100)
        self.plot = self.figure.add_subplot(1,1,1)
        self.plot.bar(uniqueWords,frequencies)
        self.plot.set_xticklabels(uniqueWords,rotation='vertical')
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

    