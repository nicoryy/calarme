'''
Código feito por __Nicory__
        09/09/2022
----------------------------
Por puro intuito de estudos prática.
'''

from pygame import mixer
import datetime
import keyboard
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QMainWindow
from PyQt5 import QtWidgets
from calarme.view import Ui_Alarme


class Alarme(QMainWindow, Ui_Alarme):

    def __init__(self):
        super().__init__()

        self.music = 'c:/Users/pedro/Desktop/nicory/projetos/projetosProntos/calarme/timer.mp3'

        self.setupUi(self)

        self.pushButton.clicked.connect(self.set_alarme)
        self.spinBox.clear()
        self.spinBox_2.clear() 
    

    def set_alarme(self):
        '''
        Irá setar um alarme, um despertador na hora escolhida.
        :param hora: Digite a hora que deseja.
        :param minuto: Digite os minutos que deseja.

        '''
        hora = self.spinBox.value()
        minuto = self.spinBox_2.value()
        print(hora, minuto)


        mixer.init()
        # music = 'C:/Users/pedro/Desktop/nicory/projetos/projetosProntos/calarme/play.mp3'
        mixer.music.load(self.music)
        mixer.music.set_volume(0.5)
        print(f'São atualmente {datetime.datetime.now().hour}:{datetime.datetime.now().minute}...\nAlarme programado para {hora}:{minuto}')
        alarme.close()

        while True:
            if hora == datetime.datetime.now().hour and minuto == datetime.datetime.now().minute:
                mixer.music.play(fade_ms=3000)
                if minuto < 10:
                    minuto = f'0{minuto}'
                print(f'São {hora}:{minuto}!')
                while not keyboard.is_pressed('space'):
                    continue
                print('Tamo junto!')
                mixer.music.stop()
                break



if __name__ == '__main__':
    app = QApplication([])
    alarme = Alarme()
    alarme.show()
    app.exec()
    

