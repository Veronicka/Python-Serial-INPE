__author__ = 'Veronica'
from frames import housekeeping, modoNormal

def contar(rodar, varredura, tempo):
    framesEnvio = []
    while(rodar):
        framesEnvio.append(contador(framesEnvio, varredura, tempo))
    return framesEnvio

def contador(framesEnvio, varredura, tempo):
    if tempo == 0x0:
        if varredura == 0x0 or varredura == 0xc8:
            varredura = 0x0
            framesEnvio.append(housekeeping(varredura, tempo))
            varredura += 0x1
            framesEnvio.append(housekeeping(varredura, tempo))
        else:
            i = 0
            while (i < 3):
                framesEnvio.append(housekeeping(varredura, tempo))

    else:
        if varredura == 0x0 or varredura == 0xc8:
            varredura = 0x0
            framesEnvio.append(housekeeping(varredura, tempo))
            i = 0
            while (i < 10):
                varredura += 0x1
                framesEnvio.append(housekeeping(varredura, tempo))
        else:
            i = 0
            while (i < 10):
                framesEnvio.append(housekeeping(varredura, tempo))

    return framesEnvio