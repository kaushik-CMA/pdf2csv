import tkinter as tk
from tkinter import filedialog, messagebox
from core.file_discovery import get_pdf_files
from core.processor import process

def  start_gui():
    root = tk.Tk()
    root.title("PDF to CSV")
    root.geometry("700x500")
    tk.Label(root,text="PDF or Folder").pack()
    path_entry = tk.Entry(root,width =80)
    path_entry.pack()

    recursive_var = tk.BooleanVar()

    tk.Checkbutton(root,text="recursive Scan", variable=recursive_var).pack()
    
    tk.Label(root, text=" Regex Pattern").pack()
    regex_entry = tk.Entry(root, width=80)
    regex_entry.pack()

    def choose_file():
        path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if path:
            path_entry.delete(0, tk.END)
            path_entry.insert(0, path)

    def choose_folder():
        path = filedialog.askdirectory()
        if path:
            path_entry.delete(0, tk.END)
            path_entry.insert(0, path)

    tk.Button(root, text=" Select PDF", command=choose_file).pack()
    tk.Button(root, text=" Select folder", command=choose_folder).pack()

    status_box = tk.Text(root, height=15)
    status_box.pack(fill="both",expand=True)

    def convert():
       try:
        path = path_entry.get().strip()

        regex_pattern = regex_entry.get().strip()
        if regex_pattern == "":
            regex_pattern = None

        recursive = recursive_var.get()
        pdfs = get_pdf_files(path, recursive)
        outputs = process(pdfs, regex_pattern)
        status_box.delete("1.0",tk.END)
        status_box.insert(tk.END, f"Found {len(pdfs)} PDF(s)\n\n")
        for output in outputs:
            status_box.insert(tk.END, f"{output}\n")

       except Exception as e:
        messagebox.showerror("Error", str(e))

    tk.Button(root, text="Convert", command=convert).pack()

    root.mainloop()