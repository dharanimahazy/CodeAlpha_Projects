import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

root = tk.Tk()
root.title("CodeAlpha - Language Translation Tool")
root.geometry("600(x)500")
root.configure(bg="#f4f6f9")

LANGUAGES = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn"
}

def translate_text():
    text_to_translate = input_text.get("1.0", tk.END).strip()
    src_lang_name = src_lang_combo.get()
    tgt_lang_name = tgt_lang_combo.get()
    
    if not text_to_translate:
        messagebox.showwarning("Warning", "Please enter some text to translate.")
        return
        
    try:
        src_code = LANGUAGES.get(src_lang_name, "auto")
        tgt_code = LANGUAGES.get(tgt_lang_name, "en")
        
        translated_res = GoogleTranslator(source=src_code, target=tgt_code).translate(text_to_translate)
        
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_res)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

def copy_to_clipboard():
    translated_content = output_text.get("1.0", tk.END).strip()
    if translated_content:
        pyperclip.copy(translated_content)
        messagebox.showinfo("Success", "Translated text copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy.")

title_label = tk.Label(root, text="Language Translation Tool", font=("Arial", 16, "bold"), bg="#3b5998", fg="white", pady=10)
title_label.pack(fill=tk.X)

main_frame = tk.Frame(root, bg="#f4f6f9", padx=20, pady=15)
main_frame.pack(fill=tk.BOTH, expand=True)

lang_frame = tk.Frame(main_frame, bg="#f4f6f9")
lang_frame.pack(fill=tk.X, pady=5)

tk.Label(lang_frame, text="Source Language:", font=("Arial", 10, "bold"), bg="#f4f6f9").grid(row=0, column=0, sticky="w")
src_lang_combo = ttk.Combobox(lang_frame, values=["Auto Detect"] + list(LANGUAGES.keys()), width=18, state="readonly")
src_lang_combo.current(0)
src_lang_combo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(lang_frame, text="Target Language:", font=("Arial", 10, "bold"), bg="#f4f6f9").grid(row=0, column=2, sticky="w", padx=20)
tgt_lang_combo = ttk.Combobox(lang_frame, values=list(LANGUAGES.keys()), width=18, state="readonly")
tgt_lang_combo.current(1)
tgt_lang_combo.grid(row=0, column=3, padx=5, pady=5)

tk.Label(main_frame, text="Enter Text:", font=("Arial", 11, "bold"), bg="#f4f6f9").pack(anchor="w", pady=(10, 2))
input_text = tk.Text(main_frame, height=6, font=("Arial", 11), wrap=tk.WORD, bd=2, relief=tk.GROOVE)
input_text.pack(fill=tk.X)

translate_btn = tk.Button(main_frame, text="Translate Text", font=("Arial", 11, "bold"), bg="#4caf50", fg="white", activebackground="#45a049", cursor="hand2", command=translate_text, pady=5)
translate_btn.pack(fill=tk.X, pady=15)

tk.Label(main_frame, text="Translated Output:", font=("Arial", 11, "bold"), bg="#f4f6f9").pack(anchor="w", pady=(5, 2))
output_text = tk.Text(main_frame, height=6, font=("Arial", 11), wrap=tk.WORD, bd=2, relief=tk.GROOVE, bg="#eef2f7")
output_text.pack(fill=tk.X)

button_frame = tk.Frame(main_frame, bg="#f4f6f9")
button_frame.pack(fill=tk.X, pady=10)

copy_btn = tk.Button(button_frame, text="Copy Output", font=("Arial", 10), bg="#008cba", fg="white", activebackground="#007ba0", command=copy_to_clipboard, cursor="hand2")
copy_btn.pack(side=tk.RIGHT, padx=5)

root.mainloop()