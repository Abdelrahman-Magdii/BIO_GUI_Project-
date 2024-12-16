import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def Translation_Table(seq):
    # Translation dictionary from codons to their corresponding amino acids
    codon_to_amino_acid = {
        "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
        "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
        "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
        "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
        "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
        "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
        "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
        "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
        "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
        "TAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
        "TAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
        "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
        "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
        "TGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
        "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    s = ""
    sf = ""
    flag = 0

    for i in range(0, len(seq) - 2, 3):
        if codon_to_amino_acid[seq[i:i + 3]] == "M":
            flag = 1
        elif codon_to_amino_acid[seq[i:i + 3]] == "*":
            flag = 0
        if flag == 1:
            s += codon_to_amino_acid[seq[i:i + 3]]
        sf += codon_to_amino_acid[seq[i:i + 3]]

    return f"Translation of DNA to protein:\n{sf}\nString between 'M' and '*':\n{s}"


def calculate_result():
    # Get the DNA sequence from the input text
    dna_sequence = input_text.get().strip()
    if dna_sequence:
        result = Translation_Table(dna_sequence)
        result_text.set(result)
    else:
        messagebox.showwarning("Warning", "Please enter a DNA sequence.")


def choose_file():
    # Open file dialog to select a DNA file
    file_path = filedialog.askopenfilename(title="Select DNA File", filetypes=[("FASTA files", "*.fna")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                # Read the DNA sequence (assuming the sequence is in the second line)
                dna_sequence = file.readlines()[1].strip()
                result = Translation_Table(dna_sequence)
                result_text.set(result)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")


def clear_input():
    # Clear the contents of the input text and result label
    input_text.delete(0, tk.END)
    result_text.set("")


# Create the main window
root = tk.Tk()
root.title("DNA to Protein Translator")
root.geometry("800x850")
root.configure(bg="#2C3E50")

# Add UI elements

choose_button = tk.Button(root, text="Choose File", command=choose_file, bg="#16A085", fg="white",
                          font=("Arial", 12))
choose_button.pack(pady=30)

input_text = tk.Entry(root, font=("Arial", 12), bg="white", fg="black", width=50)
input_text.pack(pady=20)



calc_button = tk.Button(root, text="Calculate Result", command=calculate_result, bg="#16A085", fg="white",
                        font=("Arial", 12))
calc_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_input, bg="#F44336", fg="white", font=("Arial", 12))
clear_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", padx=10, pady=5, wraplength=750, bg="#2C3E50",
                        font=("Arial", 12, "bold"), fg='white')
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
