import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

def hemolytic(file_path):
    tb = []
    with open(file_path, 'r') as infile:
        for line in infile:
            if line[0] == ">":
                s = line.split("|lcl|")
            else:
                if s[3] == 'non-hemolytic' or s[3] == 'non-hemolytic\n':
                    tb.append([line[:-1], 0])
                else:
                    tb.append([line[:-1], 1])
    head = ['Sequence', 'y']
    df = pd.DataFrame(tb, columns=head)
    return df

def split_sequence(file_path):
    tb = []
    l = []
    with open(file_path, 'r') as infile:
        for line in infile:
            if line[0] == ">":
                l.append(line[1:-1])
            else:
                seq = line[:-1]
                tb.append(seq)
    df = pd.DataFrame({"ID": l, "Sequence": tb})
    return df

def browse_file():
    filename = filedialog.askopenfilename(title="Select a File", filetypes=[("FASTA files", "*.fasta")])
    if filename:
        if 'HAPPENN' in filename:
            result = hemolytic(filename)
        elif 'seq' in filename:
            result = split_sequence(filename)
        result_text.set(result.to_string(index=False, justify='left'))

# Clear the output text
def clear_output():
    result_text.set("")

# GUI setup
root = tk.Tk()
root.title("Hemolytic File Processor")

# Customize window size
root.geometry("800x850")  # width x height

# Customize background color
root.config(bg='#2C3E50')  # dark blue background

# Customize font
font_settings = ("Arial", 14)

# GUI widgets
browse_button_hemolytic = tk.Button(root, text="Choose Hemolytic File", command=browse_file, font=font_settings, bg='#16A085', fg='white')
browse_button_hemolytic.pack(pady=10)

browse_button_split = tk.Button(root, text="Choose Split Sequence File", command=browse_file, font=font_settings, bg='#16A085', fg='white')
browse_button_split.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_output, font=font_settings, bg='#E74C3C', fg='white')
clear_button.pack(pady=10)

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

root.mainloop()
