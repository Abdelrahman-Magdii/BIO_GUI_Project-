import tkinter as tk
from tkinter import filedialog
import numpy as np



def Badchars(seq, sub_seq):
    table = np.zeros([4, len(sub_seq)])
    row = ["C", "G", "A", "T"]
    for i in range(4):
        num = -1
        for j in range(len(sub_seq)):
            if row[i] == sub_seq[j]:
                table[i, j] = -1
                num = -1
            else:
                num += 1
                table[i, j] = num
    x = -1
    i = 0
    while i < len(seq) - len(sub_seq) + 1:
        if sub_seq == seq[i:i + len(sub_seq)]:
            x = i
        else:
            for j in range(i + len(sub_seq) - 1, i - 1, -1):
                if seq[j] != sub_seq[int(j - i)]:
                    k = row.index(seq[j])
                    i += table[k, j - i]
                    break
        i = int(i + 1)
    return f"Bad Character Matching of pattern '{sub_seq}' at offset: {x}"


class DNAMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bad Character Matching")
        self.root.geometry("800x850")
        self.root.configure(bg="#2C3E50")

        # Create widgets
        self.file_button = tk.Button(root, text="Choose DNA File", command=self.choose_dna_file, bg="#16A085",
                                     fg="white", padx=20, pady=5)
        self.file_button.pack(pady=10)

        # Label for Sub-sequence input
        self.subseq_label = tk.Label(root, text="Sub-sequence", bg="#2C3E50", fg="white", font=("Arial", 12))
        self.subseq_label.pack(pady=5)

        self.subseq_entry = tk.Entry(root, width=50)
        self.subseq_entry.pack(pady=10)

        self.match_button = tk.Button(root, text="Match", command=self.match_sequence, bg="#16A085", fg="white",
                                      padx=20, pady=5)
        self.match_button.pack(pady=10)

        # Labels to display results
        self.native_result_label = tk.Label(root, text="", bg="#2C3E50", font=("Arial", 12),fg='white')
        self.native_result_label.pack(pady=5)

        self.badchars_result_label = tk.Label(root, text="", bg="#2C3E50", font=("Arial", 12),fg='white')
        self.badchars_result_label.pack(pady=5)

    def choose_dna_file(self):
        self.dna_file = filedialog.askopenfilename(title="Select DNA File", filetypes=[("FASTA files", "*.fasta")])
        if self.dna_file:
            self.native_result_label.config(text=f"Selected DNA File: {self.dna_file}")

    def match_sequence(self):
        sub_seq = self.subseq_entry.get()
        if not sub_seq or not self.dna_file:
            self.native_result_label.config(text="Please select a DNA file and enter a sub-sequence")
            return

        with open(self.dna_file, 'r') as file:
            seq = [line.strip() for line in file][1]  # Read sequence from file (skip header line)

        badchars_result = Badchars(seq, sub_seq)

        self.badchars_result_label.config(text=badchars_result)


if __name__ == "__main__":
    root = tk.Tk()
    app = DNAMatcherApp(root)
    root.mainloop()
