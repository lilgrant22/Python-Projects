from tkinter import *
class Helper:
    def __init__(self, width, height):

        print("  initializing the Helper class ...")
        self.root = Tk()
        self.root.title("Help Demo")
        self.root.geometry('{}x{}'.format(width,height))
        self.root.configure(background='cyan')


        self.btn = Button(self.root, text="Do It!")

        self.btn.place(x=width//2, y=height//2)
        self.do_it_count = 0
        print("  done init!")

    def run(self):
        print("    Entering the Tk main event loop")
        self.root.mainloop()
        print("    Leaving the Tk main event loop")

if __name__ == '__main__':

    print("Inside main...")
    helper = Helper(400, 500)
    helper.run()
    print("done!")
