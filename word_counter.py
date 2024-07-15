import tkinter as tk

class WordCounterApp:
    def __init__(self, root):
        self.root = root
        root.geometry("1000x600")
        root.title("Word Counter App")

        self.title = tk.Label(root, text="Welcome to the Word Counter App!", fg="crimson", font=("Arial", 30, "bold"))
        self.title.pack(pady=25)

        self.inputLabel = tk.Label(root, text="Enter your text:", font=("Arial", 22))
        self.inputLabel.pack(pady=10)

        self.input_txt = tk.Text(root, width=60, height=13, wrap=tk.WORD, font=("Ariel",15))
        self.input_txt.pack(pady=0)

        self.count_button = tk.Button(root, text="Count Words", bg="blue", fg="white", 
                                      command=self.count_words, font=("Arial", 13), width=15, height=2)
        self.count_button.pack(pady=10)

        self.result = tk.Label(root, text="", font=("Arial", 25))
        self.result.pack()

    def count_words(self):
        user_text = self.input_txt.get("1.0", "end-1c").strip()
        if not user_text:
            self.result.config(text=f"Word count: 0")
            return
        else:
            words = len(user_text.split())
            self.result.config(text=f"Word count: {words}")

gui = tk.Tk()
app = WordCounterApp(gui)

gui.mainloop()
