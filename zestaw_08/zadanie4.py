from tkinter import Label, StringVar, Button, PhotoImage, Entry, filedialog
import tkinter as tk 
from PIL import Image

okno = tk.Tk()
# tytuł, geometria, nieskalowalne

image_fp = None  
data_image = None
photo_image = None

def open_handler():
	global image_fp, data_image
	image_fp = filedialog.askopenfilename(initialdir=".", filetypes=(("PNG Files", "*.png"),))
	if image_fp:
		data_image = PhotoImage(file=image_fp)
		image_label.config(image=data_image)

def width_modified(event):
	global image_fp
	if image_fp:
		w = width_entry.get()
		if w != "" and w.isdigit():
			w = int(w)
			image = Image.open(image_fp)
			image_width = image.width
			image_height = image.height
			width_percentage = int((w*100)/image_width)
			height_set_to = int(image_height * (width_percentage/100))
			height_entry_str.set(str(height_set_to))

def height_modified(event):
	global image_fp
	if image_fp:
		h = height_entry.get()
		if h != "" and h.isdigit():
			h = int(h)
			image = Image.open(image_fp)
			image_width = image.width
			image_height = image.height
			height_percentage = int((h*100)/image_height)
			width_set_to = int(image_width * (height_percentage/100))
			width_entry_str.set(str(width_set_to))

def resize_handler():
	global image_fp, photo_image
	if image_fp:
		w = width_entry_str.get()
		h = height_entry_str.get()

		if w != "" and w.isdigit() and h != "" and h.isdigit():
			w = int(w)
			h = int(h)
			image = Image.open(image_fp)
			image.thumbnail((w,h), Image.Resampling.LANCZOS)
			image.save('temp.png')
			photo_image = PhotoImage(file='temp.png')
			image_label.config(image=photo_image)

def save_handler():
	global image_fp, photo_image
	if image_fp:
		image_save_fp = filedialog.askopenfilename(initialdir=".", filetypes=(("PNG files","*.png"),), defaultextension=".png")
		if image_save_fp:
			w = width_entry_str.get()
			h = height_entry_str.get()
			if w != "" and w.isdigit() and h != "" and h.isdigit():
				w = int(w)
				h = int(h)
				image = Image.open(image_fp)
				image.thumbnail((w,h), Image.Resampling.LANCZOS)
				image.save(image_save_fp.name)


# open_bnt = Button(... z open_handler)
# width_label = Label(...
width_entry_str = StringVar()
# width_entry = Entry(...
width_entry.bind("<KeyRelease>", width_modified)

# height_label = Label(...
height_entry_str = StringVar()
# height_entry = Entry(...
height_entry.bind("<KeyRelease>", height_modified)

# resize_btn = Button(... z resize_handler)

# save_btn = Button(... z save_handler)

image_label = Label(okno)
image_label.config(image="")
image_label.pack(fill="both", padx=10, pady=50)

okno.mainloop()
