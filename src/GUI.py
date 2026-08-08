import tkinter as tk
import subprocess
import sys
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent
VIRTUAL_MOUSE_PATH = BASE_DIR / "virtual_mouse_hands.py"

process = None


def stop_program():
    global process

    if process is not None and process.poll() is None:
        process.terminate()
        process = None


def run_virtual_mouse():
    global process

    if process is not None and process.poll() is None:
        current_status.config(
            text="Virtual Mouse is already running..."
        )
        return

    try:
        process = subprocess.Popen(
            [sys.executable, str(VIRTUAL_MOUSE_PATH)],
            cwd=str(BASE_DIR)
        )

        current_status.config(
            text="Virtual Mouse is running..."
        )

    except Exception as error:
        current_status.config(
            text=f"Unable to start Virtual Mouse: {error}"
        )


def close_application():
    stop_program()
    root.destroy()


# -----------------------------
# GUI Configuration
# -----------------------------

root = tk.Tk()
root.title("AI Virtual Mouse")
root.geometry("480x240")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=480,
    height=240,
    bg="#333333",
    highlightthickness=0
)

canvas.pack(fill="both", expand=True)


title_label = tk.Label(
    canvas,
    text="AI Virtual Mouse",
    bg="#333333",
    fg="white",
    font=("Arial", 18, "bold")
)

title_label.place(
    relx=0.5,
    rely=0.18,
    anchor="center"
)


button_start = tk.Button(
    canvas,
    text="Start Virtual Mouse",
    command=run_virtual_mouse,
    bg="#1E90FF",
    fg="white",
    activebackground="#1877D1",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    width=20,
    height=2
)

button_start.place(
    relx=0.5,
    rely=0.48,
    anchor="center"
)


button_exit = tk.Button(
    canvas,
    text="Exit",
    command=close_application,
    bg="#555555",
    fg="white",
    activebackground="#444444",
    activeforeground="white",
    font=("Arial", 10),
    width=10
)

button_exit.place(
    relx=0.5,
    rely=0.72,
    anchor="center"
)


current_status = tk.Label(
    root,
    text="Waiting for user input.",
    bd=1,
    relief=tk.SUNKEN,
    anchor=tk.W
)

current_status.pack(
    side=tk.BOTTOM,
    fill=tk.X
)


root.protocol("WM_DELETE_WINDOW", close_application)

root.mainloop()
