import os
import json
import cv2
import numpy as np
import pyautogui
import turtle

from pynput.mouse import Controller, Button
from pynput import keyboard

import settings

def draw_from_data_file():
    print("Enter the file name (without extension) of the data file:")
    file_name = input("File Name: ") + ".json"

    if not os.path.exists(file_name):
        print("File not found.")
        return

    with open(file_name, "r") as file:
        data = json.load(file)

    start_delay = settings.get_setting("start_delay")
    print(f"Drawing will start in {start_delay} seconds. Switch to your drawing app.")
    pyautogui.sleep(start_delay)

    mouse = Controller()

    for point in data["pointarr"]:
        if point.startswith("n"):  # Move to a new position
            x, y = map(int, point[2:].split(","))
            mouse.position = (x + settings.get_setting("x_offset"), y + settings.get_setting("y_offset"))
            pyautogui.sleep(settings.get_setting("draw_speed"))
        else:  # Draw a line
            x, y = map(int, point.split(","))
            mouse.press(Button.left)
            mouse.position = (x + settings.get_setting("x_offset"), y + settings.get_setting("y_offset"))
            pyautogui.sleep(settings.get_setting("draw_speed"))
            mouse.release(Button.left)
            pyautogui.sleep(settings.get_setting("draw_speed"))

    print("Drawing completed.")

def draw_from_image():
    print("Enter the file name (with extension) of the image:")
    image_file = input("Image File: ")

    if not os.path.exists(image_file):
        print("File not found.")
        return

    img = cv2.imread(image_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, maxLineGap=5)

    data = {"pointarr": []}

    for line in lines:
        x1, y1, x2, y2 = line[0]
        data["pointarr"].append(f"n,{x1},{y1}")
        data["pointarr"].append(f"{x2},{y2}")

    with open("output_data.json", "w") as file:
        json.dump(data, file)

    print("Data file created from image.")

def make_data_file():
    print("Make your own data file: Press any key to mark a point, Enter to mark a new separate point, and Esc to finish.")

    data = {"pointarr": []}

    def on_press(key):
        if key == keyboard.Key.enter:
            data["pointarr"].append("n")
        elif key == keyboard.Key.esc:
            with open("output_data.json", "w") as file:
                json.dump(data, file)
            print("Data file created.")
            return False
        else:
            try:
                x, y = pyautogui.position()
                data["pointarr"].append(f"{x},{y}")
            except:
                pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def preview():
    print("Previewing drawing...")

    turtle.setup(width=800, height=600)
    turtle.bgpic("bg.png")

    turtle.penup()

    with open("output_data.json", "r") as file:
        data = json.load(file)

    for point in data["pointarr"]:
        if point.startswith("n"):
            x, y = map(int, point[2:].split(","))
            turtle.goto(x, y)
        else:
            x, y = map(int, point.split(","))
            turtle.pendown()
            turtle.goto(x, y)

    turtle.done()
