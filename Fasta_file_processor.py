import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def GC_Content(sequence):
    l = len(sequence)
    num_G = sequence.count("G")
    num_C = sequence.count("C")
    total = num_C + num_G
    return str(total / l)

def Complement(sequence):
    dic = {"G": "C", "C": "G", "A": "T", "T": "A"}
    s = list(sequence)
    for i in range(len(sequence)):
        s[i] = str(dic[s[i]])
    s = "".join(s)
    return s

def Reverse(sequence):
    s = list(sequence)
    s = reversed(s)
    s = "".join(s)
    return s

def Reverse_Complement(sequence):
    seq = Reverse(sequence)
    seq = Complement(seq)
    return seq

def browse_file():
    filename = filedialog.askopenfilename(title="Select a File", filetypes=[("FASTA files", "*.fasta")])
    if filename:
        with open(filename) as file:
            sequence = file.readlines()[1].strip()  # Skip header line and take sequence part
        display_results(sequence)

def display_results(sequence):
    if sequence:
        gc_content = GC_Content(sequence)
        complement = Complement(sequence)
        reverse = Reverse(sequence)
        reverse_complement = Reverse_Complement(sequence)

        result_text.set(f"GC Content: {gc_content}\n"
                        f"Complement: {complement}\n"
                        f"Reverse: {reverse}\n"
                        f"Reverse Complement: {reverse_complement}")
    else:
        messagebox.showerror("Error", "No DNA sequence found.")

def clear_results():
    input_text.delete(0, tk.END)
    result_text.set("")

# GUI setup
root = tk.Tk()
root.title("DNA Sequence Processor (GC_Content, Complement, Reverse, Reverse_Complement)")

# Customize window size
root.geometry("800x850")  # width x height

# Customize background color
root.config(bg='#2C3E50')  # dark blue background

# Customize font
font_settings = ("Arial", 12)

# GUI widgets
choose_file_button = tk.Button(root, text="Choose File", command=browse_file, font=font_settings, bg='#16A085', fg='white')
choose_file_button.pack(pady=10)

input_label = tk.Label(root, text="Or Input DNA Sequence Manually:", font=font_settings, bg='#2C3E50', fg='white')
input_label.pack()

input_text = tk.Entry(root, width=30, font=font_settings)
input_text.pack(pady=10)

def process_input():
    sequence = input_text.get().strip()
    if sequence:
        display_results(sequence)
    else:
        messagebox.showerror("Error", "Please enter a valid DNA sequence.")

input_button = tk.Button(root, text="Process Sequence", command=process_input, font=font_settings, bg='#16A085', fg='white')
input_button.pack(pady=10)

# Use a ScrolledText widget to allow multiline output
result_text = tk.StringVar()
result_label = ScrolledText(root, wrap="word", width=90, height=20, font=font_settings, bg='#2C3E50', fg='white')
result_label.pack(padx=20, pady=10)

# Update ScrolledText with the content from result_text variable
def update_result():
    result_label.delete(1.0, tk.END)  # Clear current content
    result_label.insert(tk.END, result_text.get())  # Insert new content

# Bind update_result to happen whenever result_text changes
result_text.trace_add("write", lambda *args: update_result())

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_results, font=font_settings, bg='#F44336', fg='white')
clear_button.pack(pady=10)

root.mainloop()
