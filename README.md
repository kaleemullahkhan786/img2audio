---

# 🎧 Img2Audio Tool v2  
### *Convert any Image ↔ Audio WAV File — by Kaleemullah Khan*

---

## 🧩 Overview  
**Img2Audio** ek unique Python-based tool hai jo **images ko WAV audio files mein encode karta hai** aur **WAV se wapas image decode karta hai** — bina kisi data loss ke.  
Yeh educational aur research purpose ke liye design kiya gaya hai (for beginners learning how data can be hidden/transferred in sound format).

---

## 🌈 Features  
✅ Converts **any image format** (`.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`, etc.)  
✅ Fully reversible — decode audio back to the original image  
✅ **Colorful, hacker-style banner** and CLI interface  
✅ **Supports Termux, Linux, macOS, and Windows**  
✅ Minimal inputs — easy for beginners  
✅ Error-safe and clean output  
✅ Educational example of **steganography-like encoding**

---

## 🛠️ Requirements  
Install Python dependencies:

```bash
pip install colorama

That’s it! No heavy libraries required.


---

🚀 Usage

Run the tool

python3 img2audio_cli.py


---

1️⃣ Encode Image → Audio

When prompted:

Choose option:
1) Encode Image → WAV
2) Decode WAV → Image
Enter choice (1/2): 1

Then:

Enter image path: ~/storage/shared/Pictures/test.jpg
Save as [default: ./test_encoded.wav]:

✅ The tool will generate an audio file:
test_encoded.wav


---

2️⃣ Decode Audio → Image

Choose option 2, then:

Enter WAV file path: ./test_encoded.wav
Output folder [default: current]:

✅ The tool will restore your image as:
recovered_test.jpg


---

📂 Example Directory Flow

img2audio_cli.py
│
├── input/
│   └── myimage.png
│
├── output/
│   ├── myimage_encoded.wav
│   └── recovered_myimage.png


---

🎨 Banner Preview

   _            ___               ___
  (_)_ _  ___ _|_  |___ ___ _____/ (_)__
 / /  ' \/ _ `/ __// _ `/ // / _  / / _ \
/_/_/_/_/\_, /____/\_,_/\_,_/\_,_/_/\___/
        /___/
                   by Kaleemullah Khan

------------------------------------------------------------
   Simple Image <-> Audio Converter (All Formats Supported)
------------------------------------------------------------

1) Encode Image → WAV
2) Decode WAV → Image

Enter choice (1/2):


---

⚙️ Technical Summary

Function	Description

encode_image_to_wav()	Converts any image to binary and stores it in a WAV file with metadata.
decode_wav_to_image()	Extracts and rebuilds the image file from the WAV’s binary stream.
colorama	Used for terminal color formatting.
wave	Handles the creation and reading of .wav files.
struct	Encodes header and binary metadata for safe reconstruction.



---

💡 Example Idea

You can use this tool to:

Hide small images or data inside an audio file.

Experiment with steganography concepts.

Build creative apps that mix sound and visuals.



---

⚠️ Disclaimer

This tool is strictly for educational and ethical use.
Do not use it for hiding or transmitting illegal data.
The developer (Kaleemullah Khan) is not responsible for any misuse.


---

🧠 Author

Developed by: @KaleemullahKhan
Tool Name: Img2Audio v2
Platform: Termux / Linux / macOS / Windows


---

🌟 Support

If you like this tool, star the repo ⭐ and share it with learners.
Pull requests and ideas are welcome!


---

© 2025 Kaleemullah Khan — All Rights Reserved

---
