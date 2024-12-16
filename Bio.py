import subprocess
import tkinter as tk

def run_script(script_name):
    """Runs the specified script using subprocess."""
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")

def run_sec1():
    run_script("hemolytic.py")

def run_sec2():
    run_script("Fasta_file_processor.py")

def run_sec3_4():
    run_script("DNA_sequence_translator.py")

def run_sec5_exact_match():
    run_script("Exact_match_finder.py")

def run_sec5_bad_char():
    run_script("Bad_character.py")

def run_sec6():
    run_script("Indexing.py")

def run_sec7():
    run_script("Suffix_array.py")

def run_sec8():
    run_script("overlap.py")

# GUI Code
root = tk.Tk()
root.title("BIO Project")
root.geometry("900x850")
root.config(bg="#2C3E50")

button_style = {
    "font": ("Helvetica", 12, "bold"),
    "bg": "#16A085",
    "fg": "white",
    "activebackground": "#2C3E50",
    "activeforeground": "white",
    "width": 30,
    "height": 2,
    "relief": "groove",
    "bd": 4
}

title_frame = tk.Frame(root, bg="#2C3E50", height=60)
title_frame.pack(fill="x", side="top")

title_label = tk.Label(
    title_frame,
    text="BIO Project File Manager",
    font=("Helvetica", 16, "bold"),
    bg="#2C3E50",
    fg="white"
)
title_label.pack(pady=10)

btn_sec1 = tk.Button(root, text="hemolytic", command=run_sec1, **button_style)
btn_sec1.pack(pady=10)

btn_sec2 = tk.Button(root, text="Fasta_file_processor", command=run_sec2, **button_style)
btn_sec2.pack(pady=10)

btn_sec3_4 = tk.Button(root, text="DNA_sequence_translator", command=run_sec3_4, **button_style)
btn_sec3_4.pack(pady=10)

btn_sec5_exact_match = tk.Button(root, text="Exact_match_finder", command=run_sec5_exact_match, **button_style)
btn_sec5_exact_match.pack(pady=10)

btn_sec5_bad_char = tk.Button(root, text="Bad_character", command=run_sec5_bad_char, **button_style)
btn_sec5_bad_char.pack(pady=10)

btn_sec6 = tk.Button(root, text="Indexing", command=run_sec6, **button_style)
btn_sec6.pack(pady=10)

btn_sec7 = tk.Button(root, text="Suffix_array", command=run_sec7, **button_style)
btn_sec7.pack(pady=10)

btn_sec8 = tk.Button(root, text="Overlap", command=run_sec8, **button_style)
btn_sec8.pack(pady=10)


root.mainloop()
