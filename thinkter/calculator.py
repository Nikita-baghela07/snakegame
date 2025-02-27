from tkinter import *
from PIL import Image, ImageTk


# # Initialize the main window
ABC_root = Tk()

ABC_root.geometry("733x434")
ABC_root.minsize(200, 300)

ABC_root.title("Calculator")

# Add a label
nikita = Label(text="""newspaper  ---- "times of india" """
, bg="red", fg="white", padx=20,pady=20, font="latin 10 bold", borderwidth=3, relief=SUNKEN, anchor="center", wraplength=900,width=16, height=1)
#add a pack
nikita.pack(padx=20, pady=20, fill=X, side=RIGHT)



# Load and display an image
image = Image.open("snake.jpg")
image1= Image.open("snake1.png")
image1 = image.resize((300, 200))  
resized_image = image.resize((300, 200))  # Resize the image to 300x200 pixels
photo = ImageTk.PhotoImage(resized_image)
photo1 = ImageTk.PhotoImage(image1)
image_Label = Label(image=photo1)
image_Label.pack(side=LEFT,padx=20, pady=20)
image_label = Label(image=photo)
image_label.pack(side=LEFT,padx=80, pady=80)

# Start the main event loop
ABC_root.mainloop()