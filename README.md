# 🖱️ AI Virtual Mouse System using Computer Vision and Hand Gesture Recognition

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-FF6F00?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

> **An AI-powered virtual mouse application that enables touchless computer interaction using real-time hand gesture recognition. Built with Python, OpenCV, and MediaPipe to demonstrate the capabilities of Computer Vision and Human-Computer Interaction (HCI).**

---

# 📖 Overview

The **AI Virtual Mouse System** is an intelligent Computer Vision application that transforms hand gestures into mouse actions using a standard webcam. Instead of relying on a physical mouse, users can interact with their computer through natural hand movements, creating a seamless and touchless user experience.

The project combines **Python**, **OpenCV**, and **MediaPipe** to perform real-time hand tracking, gesture recognition, and cursor control while showcasing practical applications of Artificial Intelligence in Human-Computer Interaction (HCI).

---

# ✨ Features

- 🖐️ Real-time hand detection and tracking
- 🎯 AI-powered hand landmark recognition
- 🖱️ Touchless cursor movement
- 👆 Gesture-based mouse click operations
- 🤏 Drag and Drop functionality
- 📜 Scroll support *(if implemented)*
- ⚡ Smooth cursor navigation with low latency
- 💻 Simple and intuitive graphical interface
- 📷 Webcam-based interaction without additional hardware

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| AI Framework | MediaPipe |
| Mouse Automation | PyAutoGUI |
| Numerical Computing | NumPy |
| GUI | Tkinter |

---

# 📂 Project Structure

```text
AI-Virtual-Mouse-System/
│
├── GUI.py
├── handTrackingModule.py
├── virtual_mouse_hands.py
├── dictfile.txt
├── d_dictfile.txt
├── requirements.txt
├── LICENSE
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Mo-nesh/AI-Virtual-Mouse-System.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd AI-Virtual-Mouse-System
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the Application

```bash
python GUI.py
```

or

```bash
python virtual_mouse_hands.py
```

---

# 🧠 How It Works

1. Captures live video from the webcam.
2. Detects and tracks hand landmarks using MediaPipe.
3. Identifies finger positions and hand gestures.
4. Maps recognized gestures to mouse operations.
5. Executes cursor movement and mouse events in real time.

---

# ✋ Supported Gestures

| Hand Gesture | Mouse Action |
|--------------|--------------|
| Index Finger | Cursor Movement |
| Index + Middle Finger | Left Click |
| Thumb + Index Finger | Right Click |
| Pinch Gesture | Drag & Drop |
| Two Finger Swipe | Scroll *(if implemented)* |

> **Note:** Available gestures may vary depending on the current implementation.

---

# 🎯 Applications

- Human-Computer Interaction (HCI)
- Touchless Computing
- Accessibility Solutions
- Smart Classrooms
- Interactive Presentations
- Healthcare Systems
- Public Information Kiosks
- AI & Computer Vision Research
- Gesture-Based Automation

---

# 📈 Future Enhancements

- 🎙️ Voice Command Integration
- ✋ Custom Gesture Mapping
- 🖐️ Multi-Hand Recognition
- ⌨️ Virtual Keyboard Support
- 🤖 AI-Based Gesture Learning
- 🌐 Cross-Platform Compatibility
- ⚡ Enhanced Tracking Accuracy

---

# 📸 Screenshots

Add screenshots or a demonstration GIF to showcase the application.

```text
assets/
├── banner.png
├── demo.gif
├── home.png
├── tracking.png
└── gesture.png
```

Example:

```markdown
![Application Demo](assets/demo.gif)
```

---

# 📦 Requirements

```text
opencv-python
mediapipe
numpy
pyautogui
Pillow
tkinter
```

---

# 💼 Skills Demonstrated

- Python Programming
- Artificial Intelligence
- Computer Vision
- MediaPipe Framework
- OpenCV
- Gesture Recognition
- Human-Computer Interaction (HCI)
- Image Processing
- Real-Time Video Processing
- Software Development
- GUI Development
- Automation

---

# 🤝 Contributing

Contributions are welcome!

If you have ideas for new features, optimizations, or bug fixes:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 👨‍💻 Author

### **Monesh R**

**Data Analyst | AI Data Analyst | Business Intelligence | Computer Vision Enthusiast**

📧 **Email:** moneshmuddu@gmail.com

🔗 **LinkedIn:** https://linkedin.com/in/moneshr

💻 **GitHub:** https://github.com/monesh-r

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support helps improve project visibility and encourages future development.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for additional information.

---

<p align="center">
Made with ❤️ using <strong>Python</strong>, <strong>OpenCV</strong> & <strong>MediaPipe</strong>
</p>
