'''
Código feito por __Nicory__
        07/06/2022
----------------------------
Por puro intuito de estudos prática.
'''


from pygame import mixer
import datetime
import keyboard

class Alarme:
    def __init__(self):
        self.music = 'c:/Users/pedro/Desktop/nicory/projetos/projetosProntos/calarme/play.mp3'
       
        

    def tocar(self):
        '''
        Tocar o audio imediatamente

        '''
        mixer.init()
        mixer.music.load(self.music)
        while True:
            mixer.music.play()
            print(f'São {datetime.datetime.now().hour}:{datetime.datetime.now().minute}!')
            while not keyboard.is_pressed('space'):
                continue
            print('Tamo junto!')
            mixer.music.stop()
            break

    def mostrar_hora(self):
        hora = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        if minute < 10:
            minute = f'0{minute}'
        if hora < 10:
            hora = f'0{hora}'
        horas = [hora, minute]
        return horas
    

    def set_alarme(self, hora, minuto):
        '''
        Irá setar um alarme, um despertador na hora escolhida.
        :param hora: Digite a hora que deseja.
        :param minuto: Digite os minutos que deseja.

        '''
        mixer.init()
        # music = 'C:/Users/pedro/Desktop/nicory/projetos/projetosProntos/calarme/play.mp3'
        mixer.music.load(self.music)
        mixer.music.set_volume(0.5)
        print(f'São atualmente {datetime.datetime.now().hour}:{datetime.datetime.now().minute}...\nAlarme programado para {hora}:{minuto}')
        while True:
            if hora == datetime.datetime.now().hour and minuto == datetime.datetime.now().minute:
                mixer.music.play()
                if minuto < 10:
                    minuto = f'0{minuto}'
                print(f'São {hora}:{minuto}!')
                while not keyboard.is_pressed('space'):
                    continue
                print('Tamo junto!')
                mixer.music.stop()
                break


if __name__ == '__main__':
    alarme = Alarme()
    hr = int(input('Digite a hora: '))
    mi = int(input('Digite os minutos: '))
    alarme.set_alarme(hr, mi)
    

