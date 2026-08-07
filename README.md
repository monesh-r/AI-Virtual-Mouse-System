# 🖱️ Virtual AI Mouse Using Hand Gestures

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A Computer Vision based Virtual Mouse that enables users to control the computer cursor using real-time hand gestures through a webcam without any physical mouse.

This project combines **Python**, **OpenCV**, and **MediaPipe Hand Tracking** to create an intuitive Human Computer Interaction (HCI) system.

---

# 📌 Project Overview

Traditional computer interaction depends on physical input devices.

This project demonstrates how Artificial Intelligence and Computer Vision can replace conventional mouse operations using hand gestures detected by a webcam.

The application tracks finger movements in real time and converts them into mouse actions including:

- Cursor Movement
- Left Click
- Right Click
- Double Click
- Drag & Drop
- Scroll
- Screenshot (optional if implemented)

---

# 🚀 Features

✅ Real-time Hand Detection

✅ Finger Landmark Tracking

✅ Cursor Movement

✅ Mouse Click Detection

✅ Gesture Recognition

✅ Smooth Mouse Movement

✅ User Friendly GUI

✅ Low Latency Performance

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Computer Vision | OpenCV |
| AI Framework | MediaPipe |
| Mouse Automation | PyAutoGUI |
| Numerical Computing | NumPy |
| GUI | Tkinter |

---

# 📂 Project Structure

```
Virtual-AI-Mouse/
│
├── GUI.py
├── handTrackingModule.py
├── virtual_mouse_hands.py
├── dictfile.txt
├── d_dictfile.txt
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Virtual-AI-Mouse.git
```

Navigate into project

```bash
cd Virtual-AI-Mouse
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python GUI.py
```

or

```bash
python virtual_mouse_hands.py
```

---

# 🖥️ How It Works

1. Webcam captures live video.
2. MediaPipe detects hand landmarks.
3. Finger positions are extracted.
4. Different gestures are identified.
5. Corresponding mouse commands are executed.
6. Cursor movement becomes completely touchless.

---

# 🎯 Supported Gestures

| Gesture | Action |
|----------|---------|
| Index Finger | Cursor Movement |
| Index + Middle Finger | Left Click |
| Thumb + Index | Right Click |
| Pinch Gesture | Drag |
| Two Finger Swipe | Scroll |

*(Gestures may vary depending on implementation.)*

---

# 📊 Applications

- Touchless Computer Interaction
- Accessibility Solutions
- Smart Classrooms
- Interactive Presentations
- Healthcare Systems
- Public Kiosks
- AI Research
- Human Computer Interaction (HCI)

---

# 📈 Future Enhancements

- Voice Commands
- Gesture Customization
- Multi-Hand Detection
- Virtual Keyboard
- Face Authentication
- AI Gesture Learning
- Cross Platform Optimization

---

# 📸 Screenshots

> Add screenshots of your application here.

Example

```
screenshots/
    home.png
    gesture.png
    tracking.png
```

---

# 📦 Requirements

```
opencv-python
mediapipe
numpy
pyautogui
tkinter
```

---

# 👨‍💻 Author

**Monesh R**

AI Data Analyst • Data Analyst • Business Intelligence • Computer Vision Enthusiast

LinkedIn:
https://linkedin.com/in/moneshr

GitHub:
https://github.com/monesh-r

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It motivates further development and helps others discover the project.

---

# 📄 License

This project is licensed under the MIT License.
