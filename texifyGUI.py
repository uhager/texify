#!/usr/bin/env python 

## simple GUI to run texify.sh ans pdftexify.sh (need to be in path)
## author: Ulrike Hager

from Tkinter import *
import os,tkFileDialog

cd_ini=os.getcwd()
class MainFrame(Frame): 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid() 
        self.createWidgets()
        self.bind_all('<Control-Key-q>',self.Close)
        self.bind_all('<Control-t>',self.Texify)
    def createWidgets(self):
        self.pdflatex = IntVar()
        self.pdflatex.set(1);
        self.pdf = StringVar()
        self.bib = StringVar()
        self.file = StringVar()
        self.dirname = StringVar()
        self.dirname.set(os.getcwd())
        self.quitButton = Button ( self, text="Quit", underline=0, command=self.quit )
        self.FileEntry = Entry(self,textvariable=self.file)
        self.FileButton = Button(self, text='TeX file',
                                 command = lambda: self.file.set(tkFileDialog.askopenfilename(parent=self,initialdir=self.dirname.get(),title='tex file',filetypes=[('TeX','*.tex')])))
        self.texButton = Button(self, text='TeXify', underline=0, command = self.Texify)
        self.pdfButton = Checkbutton(self, text='ps2pdf', variable=self.pdf, onvalue="-p", offvalue="")
        self.pdfButton.config(state='disabled')
        self.pdftexifyButton = Checkbutton(self, text='pdflatex', variable= self.pdflatex, command=self.togglePdftex)
        self.bibButton = Checkbutton(self, text='BibTeX', variable=self.bib, onvalue="-b", offvalue="")
        self.FileButton.grid(row=1,column=0,sticky=W+E+S+N)
        self.FileEntry.grid(row=1,column=1,columnspan=2,sticky=W+E+S+N)
        self.pdftexifyButton.grid(row=2,column=0,sticky=W)
        self.bibButton.grid(row=2,column=1,sticky=W)
        self.pdfButton.grid(row=2,column=2,sticky=W)
        self.texButton.grid(row=5,column=0,sticky=W)
        self.quitButton.grid(row=5,column=2,sticky=E)
    def togglePdftex(self):
        if self.pdflatex.get() == False:
            self.pdfButton.config(state='normal')
        else:
            self.pdfButton.config(state='disabled')
    def Texify(self, event = None):
        self.dirname.set( os.path.dirname( self.file.get() ) )
        filename = os.path.basename( self.file.get() )
        print self.dirname.get()  + ' ' + filename
        if self.pdflatex.get() == False:
            tex_command = 'texify.sh ' + filename + ' ' + self.pdf.get() + ' ' + self.bib.get()
        else:    
            tex_command = 'pdftexify.sh ' + filename + ' ' + self.bib.get()
        tex_command += ' -f' + self.dirname.get() + '/'
#        command = 'cd ' + self.dirname.get() + ' ; ' + tex_command + '; cd ' + cd_ini
        print tex_command
        os.system(tex_command)
    def Close(self,event=None):
        sys.exit(0);
    

root = Tk()
root.geometry('+50+50') 
app = MainFrame(master=root) 
app.master.title("TeXifyer") 
#app.master.geometry('400x300+200+150')

app.mainloop()
root.destroy
