import pyautogui
import numpy as np
import bezier
import time
import random
from human_mouse import MouseController

mouse = MouseController(always_zigzag=True)

def move_mouse_to(x, y):
        mouse.move(x, y, speed_factor=0.0003)


def main():
    move_mouse_to(1000, 200)
  
    print("Hareketler tamamlandı.")

if __name__ == "__main__":
    main()