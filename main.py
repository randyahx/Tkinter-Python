from tkinter import *
from PIL import ImageTk, Image    
import os
import glob

# Change this to locate image folder  
mypath = "/Users/angrandy/Desktop/Tkinter-Python/images/*.*"

# Sort files in folder by date (Use this to set a fixed number of latest images to display)
filearray = sorted(glob.glob(mypath), key=os.path.getmtime)  
# Get latest file in folder (Use this if only 1 image is required)
latest_file = max(glob.glob(mypath), key=os.path.getmtime)

print("Check to see if files are in order from latest")
print(filearray)

root = Tk()
root.title('Stringe Sterilizer Image Viewer')

image_list = []
array_size = 5     # How many images to include (Set to latest 5 images)
image_size = 500   # Size of the GUI window, set to fit raspberry pi    

for i in range(0,array_size):
    image_list.append(ImageTk.PhotoImage(Image.open(str(filearray[i]))))  

print(image_list)

img = Label(image=image_list[0], height=image_size, width=image_size)
img.grid(row=0, column=0, columnspan=3)

def forward(index): # Go to next image    
    global img
    global btnPrevious
    global btnNext

    img.grid_forget()
    
    img = Label(image=image_list[index], height=image_size, width=image_size)
    btnPrevious = Button(root, text='<', command=lambda: previous(index-1)) 
    
    if index == array_size-1:  
        btnNext = Button(root, text='>', state=DISABLED)
    else:  
        btnNext = Button(root, text=">", command=lambda: forward(index+1))  

    img.grid(row=0, column=0, columnspan=3)
    btnPrevious.grid(row=1, column=0)
    btnNext.grid(row=1, column=2)

def previous(index):  # Go to previous image  
    global img
    global btnPrevious
    global btnNext

    img.grid_forget()
    
    img = Label(image=image_list[index+1], height=image_size, width=image_size)
    btnNext = Button(root, text=">", command=lambda: forward(index+1))
    
    if index == 0:  
        btnPrevious = Button(root, text='<', state=DISABLED)
    else:  
        btnPrevious = Button(root, text='<', command=lambda: previous(index-1)) 

    img.grid(row=0, column=0, columnspan=3)
    btnPrevious.grid(row=1, column=0)
    btnNext.grid(row=1, column=2)

btnPrevious = Button(root, text="<", command=previous, state=DISABLED)
btnExit = Button(root, text="Exit", command=root.quit)
btnNext = Button(root, text=">", command=lambda: forward(1))

btnPrevious.grid(row=1, column=0)
btnExit.grid(row=1, column=1)   
btnNext.grid(row=1, column=2)

root.mainloop()

    