# 🖱️ AI Virtual Mouse System

<p align="center">
  <strong>Touchless Computer Interaction Using Computer Vision and Hand Gesture Recognition</strong>
</p>

<p align="center">
  Python • OpenCV • MediaPipe • NumPy • PyAutoGUI
</p>

---

## 📌 Overview

**AI Virtual Mouse System** is a computer vision-based human-computer interaction project that enables users to control basic computer operations through **real-time hand gestures captured using a webcam**.

The system uses **MediaPipe hand landmark detection** and **OpenCV** to identify hand and finger positions, while **PyAutoGUI** translates recognized gestures into system-level mouse and volume-control actions.

The project demonstrates the practical application of:

- Computer Vision
- Hand Landmark Detection
- Gesture Recognition
- Human-Computer Interaction (HCI)
- Desktop Automation
- Real-Time Image Processing

---

## 🎯 Key Capabilities

| Capability | Implementation |
|---|---|
| Real-time hand detection | ✅ |
| Hand landmark tracking | ✅ |
| Cursor movement | ✅ |
| Left mouse click | ✅ |
| Right mouse click | ✅ |
| System volume increase | ✅ |
| System volume decrease | ✅ |
| Gesture-based interaction | ✅ |
| Real-time webcam processing | ✅ |
| Tkinter-based launcher | ✅ |
| Touchless computer interaction | ✅ |

---

## 🧠 How It Works

The system follows a real-time computer vision pipeline:

```text
             Webcam
                │
                ▼
       Video Frame Capture
                │
                ▼
        OpenCV Preprocessing
                │
                ▼
     MediaPipe Hand Detection
                │
                ▼
      Hand Landmark Extraction
                │
                ▼
       Finger Configuration
                │
                ▼
       Gesture Identification
                │
        ┌───────┴────────┐
        ▼                ▼
   Mouse Actions     Volume Control
        │                │
        ▼                ▼
 Cursor / Clicks     System Volume
```

---

## ✋ Gesture-Based Controls

The current implementation supports the following interactions:

| Gesture / Finger Pattern | Action |
|---|---|
| Movement gesture | Cursor movement |
| Index + Middle finger interaction | Left click |
| Thumb/finger interaction | Right click |
| Four-finger pattern | Volume increase |
| Closed-hand pattern | Volume decrease |
| Stop interaction / `Q` | Exit application |

> Gesture recognition is based on finger landmark positions and relative distances detected through MediaPipe.

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Hand Tracking | MediaPipe |
| Numerical Processing | NumPy |
| Desktop Automation | PyAutoGUI |
| GUI | Tkinter |
| Version Control | Git / GitHub |

---

## 📂 Project Structure

```text
AI-Virtual-Mouse-System/
│
├── data/
│   ├── d_dictfile.txt
│   └── dictfile.txt
│
├── src/
│   ├── GUI.py
│   ├── handTrackingModule.py
│   └── virtual_mouse_hands.py
│
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

### Directory Description

**`src/`**

Contains the core Python implementation:

- `GUI.py` — graphical launcher for the Virtual Mouse application.
- `handTrackingModule.py` — hand detection, landmark extraction, finger-state detection, and distance calculation.
- `virtual_mouse_hands.py` — gesture processing and mouse/volume control logic.

**`data/`**

Contains supporting mapping/reference files used by the project.

**`requirements.txt`**

Contains the Python dependencies required by the project.

**`.gitignore`**

Prevents unnecessary files such as Python cache files, virtual environments, logs, and IDE files from being committed.

---

## ⚙️ Core Components

### 1. Hand Detection

MediaPipe detects the user's hand through the webcam and provides a set of hand landmarks representing finger and joint positions.

### 2. Landmark Processing

The system extracts the coordinates of relevant landmarks and uses their relative positions to determine the state of individual fingers.

### 3. Gesture Recognition

Finger configurations and distances between landmarks are evaluated to identify predefined gestures.

### 4. Cursor Control

Detected hand coordinates are mapped from the webcam frame to the computer screen resolution using coordinate interpolation and movement smoothing.

### 5. Mouse Automation

PyAutoGUI translates recognized gestures into operating-system mouse actions such as:

- Cursor movement
- Left click
- Right click

### 6. System Volume Control

Specific hand configurations trigger system-level volume commands through PyAutoGUI.

---

## 🖥️ Application Interface

The project includes a lightweight Tkinter-based launcher that provides a simple interface for starting the Virtual Mouse application.

```text
┌────────────────────────────────────┐
│                                    │
│          AI Virtual Mouse          │
│                                    │
│       [ Start Virtual Mouse ]      │
│                                    │
│              [ Exit ]              │
│                                    │
│  Status: Waiting for user input.   │
└────────────────────────────────────┘
```

---

## 🚀 Installation

### Prerequisites

- Python 3.x
- Webcam
- Windows/Linux desktop environment
- Working mouse and keyboard for initial setup

### Clone the Repository

```bash
git clone https://github.com/Mo-nesh/AI-Virtual-Mouse-System.git
```

Navigate to the project directory:

```bash
cd AI-Virtual-Mouse-System
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the Application

```bash
python src/GUI.py
```

The launcher will open and allow you to start the Virtual Mouse application.

---

## 🔧 Requirements

The project uses the following Python packages:

```text
opencv-python
mediapipe
numpy
pyautogui
```

These dependencies are also listed in `requirements.txt`.

---

## 📊 Technical Highlights

### Real-Time Processing

The application continuously processes webcam frames to detect hand landmarks and respond to gestures with minimal interaction delay.

### Coordinate Mapping

Hand coordinates are mapped from the camera frame to the system's screen resolution to enable virtual cursor movement.

### Movement Smoothing

A smoothing factor is applied to cursor coordinates to reduce unwanted movement and provide more stable interaction.

### Distance-Based Recognition

Distances between hand landmarks are used to distinguish gestures such as clicking interactions.

---

## 💡 Applications

The concepts demonstrated by this project can be applied to:

- Touchless Human-Computer Interaction
- Accessibility-focused interfaces
- Interactive presentations
- Smart classroom environments
- Public information kiosks
- Computer vision research
- Gesture-based desktop automation
- Experimental UI/UX systems

---

## 🔮 Future Enhancements

Potential improvements include:

- Drag-and-drop gestures
- Scrolling gestures
- Double-click recognition
- Customizable gesture mappings
- Multi-hand interaction
- Voice-assisted controls
- Gesture calibration
- Cross-platform optimization
- Improved gesture classification
- Machine-learning-based gesture recognition

---

## 📈 Learning Outcomes

This project provided practical experience in:

- Real-time computer vision
- MediaPipe hand tracking
- Image and video processing with OpenCV
- Landmark-based gesture recognition
- Coordinate transformation
- Desktop automation with PyAutoGUI
- GUI development with Tkinter
- Modular Python development
- Git and GitHub project management

---

## 👨‍💻 Author

### Monesh R

**Data Analyst | AI & Data Quality | Business Intelligence | Computer Vision**

Interested in building practical solutions using:

**Python • Data Analytics • Artificial Intelligence • Computer Vision • Automation • Business Intelligence**

**LinkedIn:**  
https://linkedin.com/in/moneshr

**GitHub:**  
https://github.com/Mo-nesh

---

## ⭐ Project Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.
