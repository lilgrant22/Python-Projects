from tkinter import *
import math
import keyword

"""
Shell class for helper GUI

This code is missing some code and needs modifying:

1) "do it" button OR entry return should process the entered command
2) "quit" button should exit the program.
3) Output text box should display the __doc__ string of command (use eval(cmd).__doc__),
    OR print "Invalid command" if not a valid built in Python command

"""


class Helper:


    def __init__(self, width, height):

        print("  initializing the Helper class ...")
        self.root = Tk()

        self.root.title("andrew.little.17@cnu.edu")
        # self.root.geometry('{}x{}'.format(width,height))
        # self.root.configure(background='blue')

        self.win = Frame(self.root)
        # self.win.configure(background='blue')
        self.win.grid_columnconfigure(4, weight=1)
        self.win.grid_rowconfigure(5, weight=1)

        self.cmd_label = Label(self.win, text="Enter cmd:")
        self.cmd_label.grid(row=2, column=1)

        self.cmd_entry = Entry(self.win, width=20, bg="white")
        self.cmd_entry.bind("<Return>", self.do_it)
        self.cmd_entry.grid(row=2, column=2)

        # Use place with just root, and grid when Frame is introduced
        self.btn = Button(self.win, text="Do It!", command=self.do_it)
        self.btn.grid(row=2, column=3)

        self.output_label = Label(self.win, text="Output:")
        self.output_label.grid(row=3, column=1)

        self.output = Text(self.win, width=80, wrap=WORD,bg='blue',fg='white')
        self.output.grid(row=4,column=1, columnspan=4)

        self.quit = Button(self.win, text="Quit!", command=self.root.quit)
        self.quit.grid(row=5, column=4)

        self.win.pack() # don't do geometry and size to fit
        print("  done init!")

    def do_it(self, *args):
        print("     Doing it for {}".format(self.cmd_entry.get()))
        self.output.delete(0.0, END)

        try:
            txt = eval(self.cmd_entry.get()).__doc__
        except Exception as e:
            print(e)
            txt = "Invalid Command"

        self.output.insert(END, txt)

        # self.output.insert(END, "{} ".format(eval(self.cmd_entry.get()).__doc__))

    def run(self):
        print("    Entering the Tk main event loop")
        self.root.mainloop()
        print("    Leaving the Tk main event loop")


if __name__ == '__main__':

    print("Inside main...")
    helper = Helper(600, 500)
    helper.run()
    print("done!")
