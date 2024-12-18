import eel # type: ignore
import sys


eel.init('front')

@eel.expose
def save_date(filename:str, pos:int, neg:int):
    with open("save/" + filename + '.txt', 'w') as f:
        f.write(f"Понравилось: {pos} | Не понравилось: {neg}")
@eel.expose
def pos(filename:str)->int:
    return load_date(filename)[0]
@eel.expose
def neg(filename:str)->int:
    return load_date(filename)[1]

def load_date(filename:str):
    nums = [0,0]
    try:
        with open("save/" + filename + ".txt", 'r') as f:
            text = f.read()
            text = text.split(' ')
            nums[0] = int(text[1])
            nums[1] = int(text[5])
    except:
        nums = [0,0]
    return nums


if sys.platform == 'linux':
    eel.browsers.set_path("chrome", "/usr/bin/firefox")

eel.start('main.html', mode="chrome", size=(1920, 1080))


