import tkinter as tk


class Win:
    def __init__(self, root):
        """Define window for the app"""
        self.root = root
        self.root.geometry("400x300")
        self.root["bg"] = "coral"
        self.button_rename = tk.Button(self.root, text = "New window",
            command= lambda: self.new_window(Win2)).pack()

    def childclosed(self, event):
        print("All fine")

    def new_window(self, _class):
        self.new = tk.Toplevel(self.root)
        self.new.bind('<Destroy>', self.childclosed)
        _class(self.new)

class Win2:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x300+200+200")
        self.root["bg"] = "navy"

if __name__ == "__main__":
    root = tk.Tk()
    app = Win(root)
    app.root.title("App")
    root.mainloop()