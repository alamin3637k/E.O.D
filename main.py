from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from cryptography.fernet import Fernet

class App:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.geometry("400x300")
        self.window.title("E.O.D")
        messagebox.showwarning("PLZ", "Save your key after encrypting from thekey.txt and for decrypting put the right key to thekey.txt (put only one key)")
    
    def encrypt(self):
        try:
            self.filePath = fd.askopenfiles()
            self.key = Fernet.generate_key()
            with open("thekey.txt",mode="ab") as thekey:
                thekey.truncate(0)
                thekey.write(self.key)
                thekey.close()
            for path in range(0, len(self.filePath)): 
                self.file = open(file=self.filePath[path].name,mode="rb")
                f = Fernet(self.key)
                token = f.encrypt(self.file.read())
                self.file = open(file=self.filePath[path].name,mode="wb")
                self.file.write(token)
                self.file.close()
            messagebox.showinfo("E.O.D", "DONE")
        except Exception as er:
            messagebox.showerror("E.O.D", er)
    
    def decrypt(self):
        try:
            self.filePath = fd.askopenfiles()
            with open("thekey.txt",mode="rb") as self.thekey:
                self.key = self.thekey.read()
            for path in range(0, len(self.filePath)): 
                self.file = open(file=self.filePath[path].name,mode="rb")
                f = Fernet(self.key)
                token = f.decrypt(self.file.read())
                self.file = open(file=self.filePath[path].name,mode="wb")
                self.file.write(token)
                self.file.close()
                messagebox.showinfo("E.O.D", "DONE")
        except Exception as ex:
            messagebox.showerror("E.O.D", ex)
        
            
    def ui(self):
        self.eb = Button(self.window, text="encrypt", command=self.encrypt)
        self.eb.pack()
        self.deb = Button(self.window, text="decrypt", command=self.decrypt)
        self.deb.pack()
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.ui()
    app.run()