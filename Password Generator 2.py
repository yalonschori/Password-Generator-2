import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import random
import string

root = ctk.CTk()
root.geometry("400x500")
root.title("Password Generator 2")


lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
numbers = [i for i in range(10)]

symbols = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "+",
    "=",
    "[",
    "]",
    "{",
    "}",
    "|",
    ":",
    ";",
    "'",
    '"',
    "<",
    ">",
    ",",
    ".",
    "?",
    "/",
    "`",
    "~",
]


def generate_password():
    condition1 = include_uppercase_checkbox_var.get()
    condition2 = include_lowercase_checkbox_var.get()
    condition3 = include_numbers_checkbox_var.get()
    condition4 = include_symbols_checkbox_var.get()
    combined_list = []
    required_list = []
    if not (condition1 or condition2 or condition3 or condition4):
        CTkMessagebox(title="Data Missing", message="Please pick 1 or more preferences")
        return
    if password_length_textbox.get("1.0", "end-1c"):
        if include_uppercase_checkbox_var.get():
            combined_list += uppercase_letters
            required_list += random.sample(uppercase_letters, 1)
        if include_lowercase_checkbox_var.get():
            combined_list += lowercase_letters
            required_list += random.sample(lowercase_letters, 1)
        if include_numbers_checkbox_var.get():
            combined_list += numbers
            required_list += random.sample(numbers, 1)
        if include_symbols_checkbox_var.get():
            combined_list += symbols
            required_list += random.sample(symbols, 1)
        if int(password_length_textbox.get("1.0", "end-1c")) <= 3:
            CTkMessagebox(
                message="the length of your password must be at least 4 characters long",
                title="Password Requirements Not Met",
            )
        elif int(password_length_textbox.get("1.0", "end-1c")) >= 21:
            CTkMessagebox(
                message="the length of your password must not exceed 20 characters",
                title="Password Requirements Not Met",
            )
        else:
            password_length = int(password_length_textbox.get("1.0", "end-1c"))
            new_password = required_list + random.sample(
                combined_list, password_length - 4
            )
            random.shuffle(new_password)
            new_password_string = " ".join(map(str, new_password)).replace(" ", "")
            your_new_password_textbox.delete("1.0", "end")
            your_new_password_textbox.insert("1.0", new_password_string)
    else:
        CTkMessagebox(
            message="the length of your password must be at least 4 characters long",
            title="Password Requirements Not Met",
        )


password_length_label = ctk.CTkLabel(root, text="Password Length")
password_length_textbox = ctk.CTkTextbox(
    root, width=200, height=20, fg_color="light gray", text_color="gray"
)

include_uppercase_checkbox_var = ctk.IntVar()
include_uppercase_checkbox = ctk.CTkCheckBox(
    root, text="include uppercase letters", variable=include_uppercase_checkbox_var
)

include_lowercase_checkbox_var = ctk.IntVar()
include_lowercase_checkbox = ctk.CTkCheckBox(
    root, text="include lowercase letters", variable=include_lowercase_checkbox_var
)

include_numbers_checkbox_var = ctk.IntVar()
include_numbers_checkbox = ctk.CTkCheckBox(
    root, text="include numbers", variable=include_numbers_checkbox_var
)

include_symbols_checkbox_var = ctk.IntVar()
include_symbols_checkbox = ctk.CTkCheckBox(
    root, text="include symbols", variable=include_symbols_checkbox_var
)

generate_password_button = ctk.CTkButton(
    root,
    text="Generate Password",
    width=350,
    height=50,
    fg_color="light gray",
    text_color="black",
    command=generate_password,
)

your_new_password_label = ctk.CTkLabel(root, text="Your New Password!")
your_new_password_textbox = ctk.CTkTextbox(
    root, width=300, height=50, fg_color="black", text_color="white"
)

password_length_label.pack(pady=10)
password_length_textbox.pack(pady=10)
include_uppercase_checkbox.pack(pady=10)
include_lowercase_checkbox.pack(pady=10)
include_numbers_checkbox.pack(pady=10)
include_symbols_checkbox.pack(pady=10)
generate_password_button.pack(pady=10)
# your_new_password_label.pack(pady=10)
your_new_password_textbox.pack(pady=10)
root.mainloop()
