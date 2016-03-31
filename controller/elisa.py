__author__ = 'Veronica'

import threading
from model.frames import housekeeping, acknowledge, modoNormal
from model.serialPython import escolhaPorta, enviarFrame, receberFrame
from view.view import View
from model.contador import contar

class ExperimentoElisa(object):

    varredura = 0x0
    tempo = 0x0
    frame = []


    def __init__(self):
        self.view = View().start()
        self.start(self.view)

    def start(self, opcao):
        if opcao == 1:
            self.port = escolhaPorta()
            return self.ouvirPorta(self.port)
        elif opcao == 2:
            return ""
        elif opcao == 3:
            return self.view.finalizar()
        else:
            return self.view.finalizar()

    def ouvirPorta(self, porta):
        receber = receberFrame(porta, True)
        print receber
        self.framesRecebidos(receber)


    def framesRecebidos(self, frame):
        t2 = threading.Thread(name='T2', target=contar(False, ExperimentoElisa.varredura, ExperimentoElisa.tempo))

        #t2.start()

        f = ''
        for i in frame:
            f+=i
        respostaOBC = [ord(b) for b in f]
        print respostaOBC

        if respostaOBC[2] == 8:
            print 'TURN ON'
            enviarFrame(self.port, acknowledge())
            self.frame.append(contar(True, ExperimentoElisa.varredura, ExperimentoElisa.tempo))

        elif respostaOBC[2] == 4:
            print 'DATA REQUEST'
            self.frame.append(contar(False, ExperimentoElisa.varredura, ExperimentoElisa.tempo))

            for fm in self.frame:
                enviarFrame(self.port, fm)

        elif respostaOBC[2] == 2:
            print 'DATA SEND'
            enviarFrame(self.port, acknowledge())
            if respostaOBC[4] == 0:
                ExperimentoElisa.tempo = 0x0
            else:
                ExperimentoElisa.tempo = 0x1

        elif respostaOBC[2] == 7:
            print 'RESET'
            enviarFrame(self.port, acknowledge())
            
        elif respostaOBC[2] == 9:
            print 'TURN OFF'
            enviarFrame(self.port, acknowledge())

        else:
            print 'Impossivel verificar'


