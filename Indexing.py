import tkinter as tk
from tkinter import filedialog
import bisect


def IndexSorted(seq, ln):
    index = []
    for i in range(len(seq) - ln + 1):
        index.append((seq[i:i + ln], i))
    index.sort()
    return index


def query(t, p, index):
    keys = [r[0] for r in index]
    st = bisect.bisect_left(keys, p[:len(keys[0])])
    en = bisect.bisect(keys, p[:len(keys[0])])
    hits = index[st:en]
    l = [h[1] for h in hits]
    offsets = []
    for i in l:
        if t[i:i + len(p)] == p:
            offsets.append(i)
    return offsets


class DNAMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Offsets with Pattern Query")
        self.root.geometry("800x850")
        self.root.configure(bg="#2C3E50")

        # Create widgets
        self.file_button = tk.Button(root, text="Choose DNA File (TEXT)", command=self.choose_dna_file, bg="#16A085",
                                     fg="white", padx=20, pady=5)
        self.file_button.pack(pady=10)

        self.pattern_label = tk.Label(root, text="Pattern", bg="#2C3E50", fg="white", font=("Arial", 12))
        self.pattern_label.pack(pady=5)

        self.pattern_entry = tk.Entry(root, width=50)
        self.pattern_entry.pack(pady=10)

        self.query_button = tk.Button(root, text="Query", command=self.query_pattern, bg="#16A085", fg="white",
                                      padx=20, pady=5)
        self.query_button.pack(pady=10)

        # Labels to display results
        self.result_label = tk.Label(root, text="", bg="#2C3E50", font=("Arial", 12),fg="white")
        self.result_label.pack(pady=5)

    def choose_dna_file(self):
        self.dna_file = filedialog.askopenfilename(title="Select DNA File", filetypes=[("FASTA files", "*.fasta")])
        if self.dna_file:
            self.result_label.config(text=f"Selected DNA File: {self.dna_file}")

    def query_pattern(self):
        pattern = self.pattern_entry.get()
        if not pattern or not self.dna_file:
            self.result_label.config(text="Please select a DNA file and enter a pattern")
            return

        with open(self.dna_file, 'r') as file:
            seq = [line.strip() for line in file][1]  # Read sequence from file (skip header line)

        index = IndexSorted(seq, len(pattern))
        offsets = query(seq, pattern, index)

        self.result_label.config(text=f"Offsets of the pattern '{pattern}': {offsets}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DNAMatcherApp(root)
    root.mainloop()
