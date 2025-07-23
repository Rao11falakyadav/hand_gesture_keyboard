# 🎹 AI Virtual Keyboard using Hand Gestures

Control your keyboard using just your hand gestures in real-time!  
This AI-powered virtual keyboard tracks hand movements through your webcam and lets you type without touching your keyboard.

---

## 📽️ Demo Video

[![Watch the demo](https://img.youtube.com/vi/WnVJ3hhEaJg/0.jpg)](https://youtu.be/WnVJ3hhEaJg)

Click the image to watch on YouTube.

---

## ✨ Features

- 🖐️ Real-time hand tracking with MediaPipe
- ⌨️ Virtual on-screen keyboard with responsive gesture typing
- 🧠 Finger detection & gesture-based key pressing
- 🔧 Built using Python, OpenCV, wxPython, and Pynput

---

## 🛠️ Installation

```bash
git clone https://github.com/Rao11falakyadav/hand_gesture_keyboard.git
cd hand_gesture_keyboard
python3 -m venv .venv
source .venv/bin/activate  # For Mac/Linux
# .venv\Scripts\activate    # For Windows

pip install -r requirements.txt
python main.py
