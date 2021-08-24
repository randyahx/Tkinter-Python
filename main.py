from tkinter import *
from PIL import ImageTk, Image    

root = Tk()
root.title('Stringe Sterilizer Image Viewer')

img1 = ImageTk.PhotoImage(Image.open("images/img1.png"))
img2 = ImageTk.PhotoImage(Image.open("images/img2.png"))
img3 = ImageTk.PhotoImage(Image.open("images/img3.png"))
img4 = ImageTk.PhotoImage(Image.open("images/img4.png"))
img5 = ImageTk.PhotoImage(Image.open("images/img5.png"))

image_list = [img1, img2, img3, img4, img5]

img = Label(image=img1, height=200)
img.grid(row=0, column=0, columnspan=3)

def forward(index):
    global img
    global btnPrevious
    global btnNext

    img.grid_forget()
    
    img = Label(image=image_list[index-1], height=200)
    btnPrevious = Button(root, text='<', command=lambda: previous(index-1)) 
    
    if index == 5:  
        btnNext = Button(root, text='>', state=DISABLED)
    else:  
        btnNext = Button(root, text=">", command=lambda: forward(index+1))  

    img.grid(row=0, column=0, columnspan=3)
    btnPrevious.grid(row=1, column=0)
    btnNext.grid(row=1, column=2)

def previous(index):  
    global img
    global btnPrevious
    global btnNext

    img.grid_forget()
    
    img = Label(image=image_list[index-1], height=200)
    btnNext = Button(root, text=">", command=lambda: forward(index+1))
    
    if index == 1:  
        btnPrevious = Button(root, text='<', state=DISABLED)
    else:  
        btnPrevious = Button(root, text='<', command=lambda: previous(index-1)) 

    img.grid(row=0, column=0, columnspan=3)
    btnPrevious.grid(row=1, column=0)
    btnNext.grid(row=1, column=2)

btnPrevious = Button(root, text="<", command=previous, state=DISABLED)
btnExit = Button(root, text="Exit", command=root.quit)
btnNext = Button(root, text=">", command=lambda: forward(2))

btnPrevious.grid(row=1, column=0)
btnExit.grid(row=1, column=1)   
btnNext.grid(row=1, column=2)

root.mainloop()

    