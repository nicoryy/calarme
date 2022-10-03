import time
from pygame import mixer
import keyboard

def countdown(sec):
    while sec:
        min, second = divmod(sec, 60)
        if second < 10:
            second = f'0{second}'

        timer = f'{min}:{second}'
        print(timer, end='\r')
        time.sleep(1)
        sec -= 1
    while True:
        mixer.init()
        try:
            mixer.music.load('timer.mp3')
        except:
            mixer.music.load(R'C:\Users\pedro\AppData\Local\Programs\Python\Python310\Lib\site-packages\calarme\timer.mp3')
        mixer.music.set_volume(0.18)
        mixer.music.play(fade_ms=3000)
        while not keyboard.is_pressed('space'):
            continue
        mixer.music.stop()
        break


if __name__ == '__main__':
    
    hr = int(input('Digite o tempo em segundos: '))
    countdown(hr)
    # print('HIIIIIIIIIIIIIIIIIIIIIIIIII')