from itertools import cycle
from PIL import Image,ImageTk
import time 
import tkinter as tk 

root = tk.Tk()
root.title("slideshow app")

image_path = [
       r"C:\Users\hp\OneDrive\Pictures\Screenshots\Screenshot (1).png"
       
]

image_sizr = (1080,1080)
images = [Image.open(path). resize(image_sizr)for path in image_path]
photo_images = [ImageTk.PhotoImage(image)for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)


        slideshow = cycle(photo_image)
    def start_slideshow():
     for _ in range(len(image_path)):
              update_image()

playbutton = tk.Button(root, text='play slideshow',command='start_slideshow')
playbutton.pack()

root.mainloop()