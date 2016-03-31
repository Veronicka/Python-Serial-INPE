__author__ = 'Veronica'

from random import randint

header = [0xeb, 0x95, 0x4, 0xfa, 0x0, 0x0, 0x0, 0x0, 0x0]

def checksum(frame):
    return 0xFF - (sum(frame[4:]) & 0xFF)

def acknowledge():
    ack = [0xeb, 0x95, 0x3, 0x0, 0x55, 0xAA]
    #ack.append(checksum(ack))
    return ack

def housekeeping(n, t):
    n_Vp = [0x7f, 0x65, 0x51, 0x40, 0x33, 0x29, 0x21, 0x1a, 0x15, 0x10, 0xd, 0xa, 0x8, 0x7, 0x5, 0x4] #voltagem das placas
    n_Cont = [0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64] #contador1
    
    hkp = header
    hkp.append(t)
    hkp.append(0x7f)

    for vp in n_Vp:
        hkp.append(vp)
        
    for c1 in n_Cont:
        hkp.append(c1)

    for c1 in n_Cont:
        hkp.append(c1)

    for vp in n_Vp:
        hkp.append(vp)

    for vp in n_Vp:
        hkp.append(vp)

    hkp.append(checksum(hkp))
    
    return hkp

def modoNormal(n, t):
    modoN = header
    n_Cont1 = [0xad, 0x8a, 0x6e, 0x57, 0x46, 0x38, 0x2c, 0x23, 0x1c, 0x16, 0x12, 0xe, 0xb, 0x9, 0x7, 0x6]
    n_Cont2 = [0x109, 0xd3, 0xa8, 0x86, 0x6b, 0x55, 0x44, 0x36, 0x2b, 0x22, 0x1b, 0x16, 0x11, 0xe, 0xb, 0x9]
    n_Cont3 = [0x144, 0x102, 0xce, 0xa4, 0x83, 0x68, 0x53, 0x42, 0x35, 0x2a, 0x21, 0x1b, 0x15, 0x11, 0xd, 0xb]

    modoN.append(t)
    modoN.append(n)

    n_Cont = []
    random = randint(1,3)
    if random == 3:
        n_Cont = n_Cont1
    elif random == 2:
        n_Cont = n_Cont2
    else:
        n_Cont = n_Cont3

    for num in n_Cont:
        modoN.append(num)

    n_Cont = []
    random = randint(1,3)
    if random == 3:
        n_Cont = n_Cont1
    elif random == 2:
        n_Cont = n_Cont2
    else:
        n_Cont = n_Cont3

    for num in n_Cont:
        modoN.append(num)
    
    modoN.append(t)
    modoN.append(n)

    n_Cont = []
    random = randint(1,3)
    if random == 3:
        n_Cont = n_Cont1
    elif random == 2:
        n_Cont = n_Cont2
    else:
        n_Cont = n_Cont3

    for num in n_Cont:
        modoN.append(num)

    n_Cont = []
    random = randint(1,3)
    if random == 3:
        n_Cont = n_Cont1
    elif random == 2:
        n_Cont = n_Cont2
    else:
        n_Cont = n_Cont3

    for num in n_Cont:
        modoN.append(num)
    
    modoN.append(checksum(modoN))
    
    return modoN

