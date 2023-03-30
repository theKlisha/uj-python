import PyPDF2  # pip install PyPDF2
from tkinter import BOTH, END, Text, Tk, Menu, filedialog

okno = Tk()
okno.title("My PDF text extractor")
okno.geometry("600x300")

text = Text(okno)
text.pack(padx=20, pady=20, fill=BOTH, expand=1)

def clear_text():
   text.delete("1.0", END)

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetypes=[("PDF", ".pdf"), ("All Files","*.*")])
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(END, content)

menubar = Menu(okno)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Open", command=open_pdf)
menu.add_command(label="Clear", command=clear_text)
menu.add_command(label="Quit", command=okno.destroy)
menubar.add_cascade(label="File", menu=menu)
okno.config(menu=menubar)
okno.mainloop()
