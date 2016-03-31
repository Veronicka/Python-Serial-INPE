__author__ = 'Veronica'

import serial

def escolhaPorta():
    MAX_PORTAS = 10 # numero maximo de portas
    k = 1
    dict = {}
    for p in ['COM%s' % (i + 1) for i in range(MAX_PORTAS)] :
        try:
            s = serial.Serial(p)
            dict[k] = s.portstr
            k+=1
            s.close()
        except (OSError, serial.SerialException):
            pass
    for i in dict:
        print i, " - ", dict[i]

    p = 15
    if len(dict) == 0:
        print "Nao ha porta serial!"
    else:
        while(p not in dict):
            p = int(input("\nEscolha a porta serial: \n"))    
            if p <= len(dict) and p!=0:
                porta = serial.Serial(dict[p], 9600, timeout=0)
                print "Porta escolhida: ", porta.portstr
                return porta
            else:
                print "Porta Nao existe!"
                        
def enviarFrame(porta, frame):
    print 'enviando ...'
    try:
        porta.write(frame)
        print 'enviado'

    except serial.SerialException:
        print 'ERRO: Nao enviado'

def receberFrame(porta, ok):
    print "recebendo frame ..."
    re = []
    while ok:
        try:
            data = porta.read(256)
            if len(data)>0:
                re.append(data)
            elif len(re) > 0:
                return re
        except serial.SerialException:
            print 'ERRO: impossivel receber'
                
    
    
                
   


