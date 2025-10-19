#!/usr/bin/env python3
"""
Img2Audio Tool v2
by Kaleemullah Khan
Colorful & professional version for Termux
"""

import os, struct, wave
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama for Termux/Windows compatibility
init(autoreset=True)

MAGIC = b"IMG2AUD"
VERSION = 1
ALLOWED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp", ".ico", ".heic", ".svg"
}

# ---------------- Banner ----------------
def print_banner():
    print(Fore.CYAN + Style.BRIGHT + r"""   _            ___               ___    
  (_)_ _  ___ _|_  |___ ___ _____/ (_)__ 
 / /  ' \/ _ `/ __// _ `/ // / _  / / _ \
/_/_/_/_/\_, /____/\_,_/\_,_/\_,_/_/\___/
        /___/                            """ + Style.RESET_ALL)
    print(Fore.GREEN + "                   by Kaleemullah Khan\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "------------------------------------------------------------")
    print("   Simple Image <-> Audio Converter (All Formats Supported)")
    print("------------------------------------------------------------\n" + Style.RESET_ALL)

# ---------------- Core encode/decode ----------------
def encode_image_to_wav(image_path: Path, wav_path: Path):
    ext = image_path.suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        print(Fore.YELLOW + f"[!] Warning: '{ext}' unusual extension, continuing anyway." + Style.RESET_ALL)

    with open(image_path, "rb") as f:
        img_bytes = f.read()
    filename_bytes = image_path.name.encode("utf-8")
    header = MAGIC + bytes([VERSION])
    header += struct.pack(">H", len(filename_bytes))
    header += filename_bytes
    header += struct.pack(">I", len(img_bytes))
    payload = header + img_bytes

    with wave.open(str(wav_path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(1)
        w.setframerate(44100)
        w.writeframes(payload)

    print(Fore.GREEN + f"[✓] Encoded successfully → {wav_path.name}" + Style.RESET_ALL)

def decode_wav_to_image(wav_path: Path, out_folder: Path):
    with wave.open(str(wav_path), "rb") as w:
        frames = w.readframes(w.getnframes())
    data = frames

    if not data.startswith(MAGIC):
        print(Fore.RED + "[✗] Error: Not a valid Img2Audio WAV file." + Style.RESET_ALL)
        return

    pos = len(MAGIC)
    version = data[pos]; pos += 1
    if version != VERSION:
        print(Fore.RED + f"[✗] Unsupported version: {version}" + Style.RESET_ALL)
        return
    fname_len = struct.unpack_from(">H", data, pos)[0]; pos += 2
    fname = data[pos:pos+fname_len].decode("utf-8"); pos += fname_len
    img_len = struct.unpack_from(">I", data, pos)[0]; pos += 4
    img_bytes = data[pos:pos+img_len]

    out_path = out_folder / ("recovered_" + fname)
    with open(out_path, "wb") as f:
        f.write(img_bytes)

    print(Fore.GREEN + f"[✓] Decoded and saved → {out_path.name}" + Style.RESET_ALL)

# ---------------- Main ----------------
def main():
    from os.path import expanduser
    print_banner()
    print(Fore.CYAN + "1) Encode Image → WAV")
    print("2) Decode WAV → Image\n" + Style.RESET_ALL)

    choice = input(Fore.YELLOW + "Enter choice (1/2): " + Style.RESET_ALL).strip()
    cwd = Path.cwd()

    try:
        if choice == "1":
            img_input = input(Fore.CYAN + "Enter image path: " + Style.RESET_ALL).strip()
            img_path = Path(expanduser(img_input)).resolve()
            if not img_path.exists():
                print(Fore.RED + "❌ Image file not found!" + Style.RESET_ALL)
                return
            default_out = cwd / f"{img_path.stem}_encoded.wav"
            out_str = input(Fore.CYAN + f"Save as [default: {default_out}]: " + Style.RESET_ALL).strip()
            out_path = Path(out_str) if out_str else default_out
            encode_image_to_wav(img_path, out_path)

        elif choice == "2":
            wav_input = input(Fore.CYAN + "Enter WAV file path: " + Style.RESET_ALL).strip()
            wav_path = Path(expanduser(wav_input)).resolve()
            if not wav_path.exists():
                print(Fore.RED + "❌ WAV file not found!" + Style.RESET_ALL)
                return
            out_dir = input(Fore.CYAN + f"Output folder [default: {cwd}]: " + Style.RESET_ALL).strip()
            out_folder = Path(expanduser(out_dir)) if out_dir else cwd
            out_folder.mkdir(parents=True, exist_ok=True)
            decode_wav_to_image(wav_path, out_folder)

        else:
            print(Fore.RED + "Invalid choice, exiting." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
