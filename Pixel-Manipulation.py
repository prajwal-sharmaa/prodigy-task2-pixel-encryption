# ───────────────────────────────────────────────────────────────
#  Pixel Encryption Tool | Prodigy Internship Task - 2
# Purpose : Encrypt/Decrypt images using pixel XOR manipulation
# GitHub  : https://github.com/prajwal-sharmaa
# ───────────────────────────────────────────────────────────────

from PIL import Image
import os

def banner():
    print("\n" + "🔐" * 30)
    print("      IMAGE ENCRYPTION / DECRYPTION TOOL")
    print("🔐" * 30 + "\n")



    # The banner function prints a header for the tool.
def process_image(image_path: str, key: int, mode: str):
    try:
        img = Image.open(image_path)
        # Ensure image is in a supported mode
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGBA")
        pixels = img.load()
        width, height = img.size

        print(f"\n🔄 Processing {mode.title()}ion...")
        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]
                if len(pixel) == 3:
                    r, g, b = pixel
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key)
                elif len(pixel) == 4:
                    r, g, b, a = pixel
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key, a)
                else:
                    print(f"⚠️ Unsupported pixel format at ({x},{y}): {pixel}")

        # Output filename
        base = os.path.basename(image_path)
        name, ext = os.path.splitext(base)
        output_name = f"{name}_{mode.lower()}{ext}"

        output_path = os.path.join("output_images", output_name)
        os.makedirs("output_images", exist_ok=True)
        img.save(output_path)

        print(f"\n✅ {mode.title()}ion completed!")
        print(f"📁 Saved as: {output_path}")

    except FileNotFoundError:
        print("❌ Image file not found. Check your path.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


def main():
    banner()

    mode = input("🛠️  Choose mode [encrypt/decrypt] : ").strip().lower()
    image_path = input("🖼️  Enter image path            : ").strip()
    key_input = input("🔑 Enter encryption key (0-255) : ").strip()

    # Validations
    if mode not in ["encrypt", "decrypt"]:
        print("❌ Invalid mode selected. Please type 'encrypt' or 'decrypt'.")
        return

    if not key_input.isdigit() or not (0 <= int(key_input) <= 255):
        print("❌ Key must be a number between 0 and 255.")
        return

    key = int(key_input)

    process_image(image_path, key, mode)


if __name__ == "__main__":
    main()
