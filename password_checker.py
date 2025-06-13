import tkinter as tk
import re
import random
import string

try:
    import nltk
    nltk.download('words', quiet=True)
    from nltk.corpus import words
    english_words = set(words.words())
    use_nltk = True
except:
    english_words = set()
    use_nltk = False


def check_strength(password):
    suggestions = []
    strength = 0

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    else:
        strength += 1

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        suggestions.append("Add a digit.")

    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1
    else:
        suggestions.append("Add a special character (e.g., !, @, #).")

    if use_nltk:
        lower_pass = password.lower()
        if lower_pass in english_words:
            suggestions.append("Avoid using dictionary words.")
            strength -= 1

    if strength <= 2:
        return "Weak", suggestions
    elif strength == 3 or strength == 4:
        return "Medium", suggestions
    else:
        return "Strong", suggestions


def generate_suggestion():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(12))


def analyze():
    password = entry.get()
    strength, tips = check_strength(password)

    result_label.config(text=f"Strength: {strength}")
    suggestion_text = "\n".join(tips) if tips else "Your password is strong!"
    suggestion_label.config(text=suggestion_text)

    if strength != "Strong":
        suggested_pass = generate_suggestion()
        alt_label.config(text=f"Suggested Strong Password:\n{suggested_pass}")
    else:
        alt_label.config(text="")


# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.config(padx=20, pady=20)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack()
entry = tk.Entry(root, show='*', font=("Arial", 12), width=30)
entry.pack(pady=10)

tk.Button(root, text="Check Strength", command=analyze).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)

suggestion_label = tk.Label(root, text="", wraplength=350, justify="left", fg="red")
suggestion_label.pack(pady=5)

alt_label = tk.Label(root, text="", fg="green", wraplength=350)
alt_label.pack(pady=10)

root.mainloop()
