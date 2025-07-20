# ───────────────────────────────────────────────────────────────
#  Pixel Encryption Tool | Prodigy Internship Task - 2
# Purpose : Encrypt/Decrypt images using pixel XOR manipulation
# GitHub  : https://github.com/prajwal-sharmaa
# ───────────────────────────────────────────────────────────────

from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def banner():
    print("\n" + "🔐" * 30)
    print("      IMAGE ENCRYPTION / DECRYPTION TOOL")
    print("🔐" * 30 + "\n")

def process_image(image_path: str, key: int, mode: str):
    try:
        img = Image.open(image_path).convert("RGB")  # Auto convert to RGB
        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        # Output filename
        base = os.path.basename(image_path)
        name, ext = os.path.splitext(base)
        output_name = f"{name}_{mode.lower()}{ext}"

        output_path = os.path.join("output_images", output_name)
        os.makedirs("output_images", exist_ok=True)
        img.save(output_path)

        messagebox.showinfo("Done", f"{mode.title()}ion completed!\nSaved as: {output_path}")

    except FileNotFoundError:
        messagebox.showerror("Error", "Image file not found. Check your path.")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")

def run_gui():
    def browse_file():
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        entry_image.delete(0, tk.END)
        entry_image.insert(0, file_path)

    def process():
        mode_val = mode_var.get()
        image_path_val = entry_image.get()
        key_val = entry_key.get()

        if mode_val not in ["encrypt", "decrypt"]:
            messagebox.showerror("Error", "Select mode: encrypt or decrypt.")
            return

        if not key_val.isdigit() or not (0 <= int(key_val) <= 255):
            messagebox.showerror("Error", "Key must be a number between 0 and 255.")
            return

        if not os.path.isfile(image_path_val):
            messagebox.showerror("Error", "Image file not found.")
            return

        process_image(image_path_val, int(key_val), mode_val)

    root = tk.Tk()
    root.title("Pixel Encryption Tool")

    tk.Label(root, text="Mode:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    mode_var = tk.StringVar(value="encrypt")
    tk.OptionMenu(root, mode_var, "encrypt", "decrypt").grid(row=0, column=1, padx=5, pady=5, sticky="w")

    tk.Label(root, text="Image Path:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_image = tk.Entry(root, width=40)
    entry_image.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=browse_file).grid(row=1, column=2, padx=5, pady=5)

    tk.Label(root, text="Key (0-255):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_key = tk.Entry(root, width=10)
    entry_key.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Button(root, text="Process", command=process).grid(row=3, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()