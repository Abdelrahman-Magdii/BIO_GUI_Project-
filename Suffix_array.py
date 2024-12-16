import tkinter as tk
from tkinter import scrolledtext

def suffix_array(t):
    l = [t[i:] for i in range(len(t))]
    l2 = l.copy()
    l.sort()
    dec = {}
    for i in range(len(l)):
        dec[l[i]] = i
    table = []
    for i in range(len(l)):
        table.append([l2[i], i, dec[l2[i]]])
    return f"The index of the text '{t}':\n{dec}\nThe Suffix Array:\n{table}"

class SuffixArrayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suffix Array Generator")
        self.root.geometry("800x600")
        self.root.configure(bg="#2C3E50")

        # Create widgets
        self.text_label = tk.Label(root, text="Text String", bg="#2C3E50", fg="white", font=("Arial", 12))
        self.text_label.pack(pady=5)

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Suffix Array", command=self.generate_suffix_array, bg="#16A085", fg="white",
                                         padx=20, pady=5)
        self.generate_button.pack(pady=10)

        # ScrolledText widget with automatic scrollbar
        self.result_label = scrolledtext.ScrolledText(root, wrap="word", width=90, height=20, font=("Arial", 12),
                                                     bg='#2C3E50', fg='white')
        self.result_label.pack(pady=5)

    def generate_suffix_array(self):
        text = self.text_entry.get()
        if not text:
            self.result_label.insert(tk.END, "Please enter a text string\n")
            return

        result = suffix_array(text)
        self.result_label.insert(tk.END, result + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = SuffixArrayApp(root)
    root.mainloop()
