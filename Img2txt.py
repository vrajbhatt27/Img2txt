from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import pytesseract as tess
from PIL import Image
import threading


tess.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

root = Tk()
root.geometry('425x250+550+200')
root.minsize(425, 250)
root.maxsize(425, 250)
root.config(bg="grey")
root.title("Image to Text")

try:
    os.mkdir('pics')
except:
    pass

try:
    os.mkdir('txt_files')
except:
    pass


filepath = None
default = os.path.join(os.getcwd(),'pics')
txtFile = os.path.join(os.getcwd(),'txt_files')


def browsefunc(lbl):
    global filepath, default
    filepath = filedialog.askopenfilename()
    lbl.config(text=str(filepath))

def single_img():
    try:
        img = Image.open(filepath)
        
        try:
            text = tess.image_to_string(img)
            fileName = os.path.basename(filepath)
            fileName = fileName.split('.')[0]

            with open(os.path.join(txtFile, fileName + '.txt'), 'w') as f:
                f.write(text)

            messagebox.showinfo("Status", "Done")
        except:
            messagebox.showinfo("Error", "Can't Convert")

    except:
        messagebox.showinfo("Error", "Select the image properly !!!")

def run():
    os.system("python dependencies//test.py")

def multiple_img(_event = None):
    threading.Thread(target=run).start()
    chk = True
    pics = os.listdir(default)

    lbl = Label(root, text='Converted: 0',
                font="Helvetica 10", bg="white", width=35)
    lbl.grid(row=5,column=0)

    for cnt,pic in enumerate(pics,1):
        img = Image.open(os.path.join(default,pic))
        
        try:
            text = tess.image_to_string(img)
            fileName = pic
            fileName = fileName.split('.')[0]

            with open(os.path.join(txtFile, fileName + '.txt'), 'w') as f:                    f.write(text)

            lbl.config(text='Converted: '+str(cnt))
        except:
            messagebox.showinfo("Error", "Can't Convert " + pic)
            chk = False
    
    
    
    if chk == True:
        messagebox.showinfo("Status", "Done")
                
# main window
def master_win():
    global root

    # Frame for browse ------------------------------------------------------
    fr = Frame(root, borderwidth=1, bg="grey")
    fr.grid(pady=35,padx=15)

    fpath = Label(fr, text=str(default), font="Helvetica 10", bg="white", width=35)
    fpath.grid(row=0,column=0)
    
    browse = Button(fr, text="Browse", width=10, bg='gray21',
                    fg='white', command=lambda: browsefunc(fpath))
    browse.grid(row=0, column=1, padx=5)
    #-------------------------------------------------------------------------

    # frame for button----------------------------------------------------------
    frb = Frame(root, borderwidth=8, bg="grey")
    frb.grid(row=1, column=0,padx=10)

    b1 = Button(frb, text="Convert", width=10,
                bg='gray21', fg='white', command=single_img)
    b1.grid(row=0, column=0, padx=10)

    b2 = Button(frb, text="Convert All", width=10, bg='gray21',
                fg='white', command=multiple_img)
    b2.grid(row=0, column=1, padx=10)

    root.bind('c',multiple_img)
    #-----------------------------------------------------------------------------

    root.mainloop()

master_win()
