
from pyautogui import *
import pyautogui
import random
import cv2

from PIL import ImageGrab
from MTM import matchTemplates
from time import sleep

import os



import keyboard

import shutil

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()



print(currentMouseX, currentMouseY)



##pica a todos los juegos
def clicktheGames(wait=2.5):
	pyautogui.click(649, 164)
	time.sleep(wait)

#le da al play
def clickPlaytheGame(wait=2.5):
	pyautogui.click(680,348)
	time.sleep(wait)
#Juega xdxd

def mouse_click(x, y, wait=2.5):
    pyautogui.click(x, y)
    time.sleep(wait)


def click_image(img):
    time.sleep(1)
    x, y = find_image(img, screen_grab())
    if x is None or y is None:
        return

    im = cv2.imread(img)
    t_cols, t_rows, _ = im.shape
    mouse_click(x + t_rows * (3 / 5), y + t_cols * (2 / 3))

def screen_grab():
    im = ImageGrab.grab()
    img_name = os.getcwd() + "\\imgs\\full_snap__" + str(int(time.time())) + ".png"
    im.save(img_name, "PNG")
    return img_name



def check_image(img):
    b, _ = find_image(img, screen_grab())
    return True if b is not None else False



def find_image(image_path, root_image_path):
    matches = matchTemplates(
        [("img", cv2.imread(image_path))],
        cv2.imread(root_image_path),
        N_object=10,
        score_threshold=0.9,
        # maxOverlap=0.25,
        searchBox=None)
    if len(matches["BBox"]) == 0:
        return None, None
    else:
        box = matches["BBox"][0]
        return box[0], box[1]

def zoomin():
	time.sleep(2.5)
	pyautogui.keyDown('ctrl')
	pyautogui.scroll(3)
	pyautogui.keyUp('ctrl')

def zoomout():
	time.sleep(2.5)
	pyautogui.keyDown('ctrl')
	pyautogui.scroll(-2)
	pyautogui.keyUp('ctrl')


def zoomout1():
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.scroll(-1)
    pyautogui.keyUp('ctrl')


def end_game(wait=2.5):
    while not check_image("ss/gain_power.png"):
        print("noestaayuda")
    click_image("ss/gain_power.png")
    time.sleep(wait)
    



def picalealGame():
    while not check_image("ss/TokenS110.png"):
        print("noestaayuda picalealgame")
    click_image("ss/TokenS110.png")

def picalealstart():
    while not check_image("ss/start_game.png"):
    	print("noestaayuda picalealstart")
    click_image("ss/start_game.png")
    time.sleep(2)

def picaleaLabarritaSPaciadorawe():
    tiempo = [1,1.02,1.04]
    time.sleep(2)
    pyautogui.click(680,384)
    for x in range(55):
        time.sleep(random.choice(tiempo))
        pyautogui.press('space')
    time.sleep(2)    


def play():
    picalealGame()
    zoomout1()
    picalealstart()
    picaleaLabarritaSPaciadorawe()
    end_game()
    pyautogui.scroll(5)
    clicktheGames()

def run():
	clicktheGames()
	time.sleep(2)
	zoomin()
	pyautogui.scroll(-3)
	play()
	zoomout()
    


if __name__ == '__main__':
	while True:
			run()
			time.sleep(200)	
	
	
