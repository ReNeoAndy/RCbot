from pyautogui import *
import pyautogui
import random
import cv2

from PIL import ImageGrab
from MTM import matchTemplates
from time import sleep


screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)

def clicktheGames(wait=2.5):
	pyautogui.click(649, 164)
	time.sleep(wait)

#Pica al juego 2048
def clicktheGame(wait=2.5):
	pyautogui.click(361, 689)
	time.sleep(wait)
#le da al play
def clickPlaytheGame(wait=2.5):
	pyautogui.click(680,348)
	time.sleep(wait)
#Juega xdxd
def play2048(wait=2.5):
	pyautogui.click(577,450)
	time.sleep(wait)	
	movementList =['left', 'right', 'up', 'down']
	for x in range(524):
		pyautogui.press(random.choice(movementList))
	time.sleep(wait)


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
	pyautogui.scroll(2)
	pyautogui.keyUp('ctrl')

def zoomout():
	time.sleep(2.5)
	pyautogui.keyDown('ctrl')
	pyautogui.scroll(-2)
	pyautogui.keyUp('ctrl')


def end_game(wait=2.5):
    
    while not check_image("ss/gain_power.png"):
        print("noestaayuda")
    click_image("ss/gain_power.png")
    time.sleep(wait)
    

def run():
	clicktheGames()
	clicktheGame()
	clickPlaytheGame()
	play2048()
	pyautogui.scroll(2)
	zoomin()
	end_game()
	zoomout()
	pyautogui.scroll(10)
	clicktheGames()


if __name__ == '__main__':
	while True:
			run()
			time.sleep(222)	
	
	