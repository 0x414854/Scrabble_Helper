import tkinter as tk


def categorize_words(words, letters):
    categorized_words = {i: [] for i in range(2, 8)}

    for word in words:
        length = len(word)
        if length >= 2 and length <= 7:
            word_is_valid = True
            for letter in word:
                if word.count(letter) > letters.count(letter):
                    word_is_valid = False
                    break
            if word_is_valid:
                categorized_words[length].append(word)

    return categorized_words


def main():
    with open("words.txt") as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line_worlds = line.strip().split(" ")
            words += line_worlds
    letters = input_entry.get()
    letters = letters.upper()
    print("Letters entered by the user : ", letters)

    categorized_words = categorize_words(words, letters)

    for widget in result_frame.winfo_children():
        widget.destroy()

    for length, word_list in categorized_words.items():
        label = tk.Label(result_frame, text=f"{length} letter(s) words :", font=("Helvetica", 14, "bold"))
        label.pack(pady=10)
        words = tk.Label(result_frame, text=word_list)
        words.pack()


def validate():
    main()


def quit():
    root.quit()
    print("Program stop !")
    root.destroy()


root = tk.Tk()
root.geometry("1000x500")
root.title("Scrabble Helper")

input_frame = tk.Frame(root)
input_frame.pack(pady=20)

label = tk.Label(input_frame, text="Enter your 7 letters :")
label.pack(side="left")

input_entry = tk.Entry(input_frame, width=30)
input_entry.pack(side="left")

validate_button = tk.Button(input_frame, text="Validate", command=validate)
validate_button.pack(side="left", padx=10)

quit_button = tk.Button(input_frame, text="Quit", command=quit)
quit_button.pack(side="right", padx=10)

result_frame = tk.Frame(root)
result_frame.pack()

root.mainloop()
