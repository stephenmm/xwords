#!/usr/bin/python3
"""
tkinter version of scrable with a solver built in

Curent Task:
  Take the original game logic scrbl_solver.py and turn into class based solution in xwordsLogic.py

Next Tasks:
  Add the GUI around the game logic in this file

Historic Notes:
  Original solver logic scrbl_solver.py
  Original GUI board xwords_game.py
"""
import tkinter as tk

class Cons:
  BOARD_WIDTH=15
  BOARD_HEIGHT=15
  BOARD_SIZE=BOARD_WIDTH*BOARD_HEIGHT

#class XwordsGame():
#   def __init__(self):
#       self.root = tk.Tk()
#       self.mainFrm = tk.Frame( self.root, width=MainWinWidth, height=MainWinHeight )
#       self.quitBtn = tk.Button(self.root, text = 'Click and Quit', command=self.quit)
#       self.quitBtn.pack()
#       self.root.mainloop()
#
#   def quit(self):
#       self.root.destroy()
#
#app = Test()
#
#
#class AppUI(Frame):
#
#    def __init__(self, master=None):
#        Frame.__init__(self, master, relief=SUNKEN, bd=2)
#
#        self.menubar = Menu(self)
#
#        menu = Menu(self.menubar, tearoff=0)
#        self.menubar.add_cascade(label="File", menu=menu)
#        menu.add_command(label="New")
#
#        menu = Menu(self.menubar, tearoff=0)
#        self.menubar.add_cascade(label="Edit", menu=menu)
#        menu.add_command(label="Cut")
#        menu.add_command(label="Copy")
#        menu.add_command(label="Paste")
#
#        try:
#            self.master.config(menu=self.menubar)
#        except AttributeError:
#            # master is a toplevel window (Python 1.4/Tkinter 1.63)
#            self.master.tk.call(master, "config", "-menu", self.menubar)
#
#        self.canvas = Canvas(self, bg="white", width=400, height=400,
#                             bd=0, highlightthickness=0)
#        self.canvas.pack()
#
#
#root = Tk()
#
#app = AppUI(root)
#app.pack()
#
#root.mainloop()
#
#
import tkinter as tk

class Xwords_tkFrame(tk.Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Simple menu")

        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

    def onExit(self):
        self.quit()

class Xwords(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title('Xwords')
        self.board = Board()
        self.pack()

def main():
    root = tk.Tk()
    nib = Xwords()
    root.mainloop()

if __name__ == '__main__':
    main()
