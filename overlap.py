import tkinter as tk

def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return f"Overlap between Two Sequences '{a}', '{b}':\n{len(a[start:])}, {a[start:]}"
        start += 1

class DNAMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Matcher with Overlap Detection")
        self.root.geometry("800x850")
        self.root.configure(bg="#2C3E50")

        # Create widgets
        self.sequence1_label = tk.Label(root, text="Sequence 1", bg="#2C3E50", fg="white", font=("Arial", 12))
        self.sequence1_label.pack(pady=5)

        self.sequence1_entry = tk.Entry(root, width=50)
        self.sequence1_entry.pack(pady=10)

        self.sequence2_label = tk.Label(root, text="Sequence 2", bg="#2C3E50", fg="white", font=("Arial", 12))
        self.sequence2_label.pack(pady=5)

        self.sequence2_entry = tk.Entry(root, width=50)
        self.sequence2_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Overlap", command=self.check_overlap, bg="#16A085", fg="white", padx=20, pady=5)
        self.check_button.pack(pady=10)

        # Label to display results
        self.result_label = tk.Label(root, text="", bg="#2C3E50", font=("Arial", 12), fg="white")
        self.result_label.pack(pady=5)

    def check_overlap(self):
        seq1 = self.sequence1_entry.get()
        seq2 = self.sequence2_entry.get()

        if not seq1 or not seq2:
            self.result_label.config(text="Please enter valid sequences")
            return

        result = overlap(seq1, seq2)
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = DNAMatcherApp(root)
    root.mainloop()

    # Example sequences:
    # seq1: ACGGTAGGT
    # seq2: GGTAGGTCC
