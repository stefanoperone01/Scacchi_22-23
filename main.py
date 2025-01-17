#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:42:39 2022

@author: iannello

"""

from Scacchiera import Scacchiera
#from Pezzo import Pezzo
from Torre import Torre
from Pedone import Pedone
from Alfiere import Alfiere
from Regina import Regina
from Re import Re
from Cavallo import Cavallo


def in_board(posizione):
    
    """
    verifica che la posizione sia all'intgerno della scacchiera
    Parameters
    ----------
    posizione: coppia di coordinate

    Returns
    -------
    bool
        True se le coordinate corrispondono a una casella della
        scacchiera, False altrimenti
    """
    
    return posizione[0] in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'} and posizione[1] in range(1, 9)


def get_mossa():
    
    """
    acquisisce una mossa dallo standard input o termina il programma
    La mossa deve essere fornita nel formato:
        
        posizione_di_partenza posizione_di_destinazione
        
    dove una posizione è una coppia formata da una lettera
    in ['A', 'H'] e da una cifra in [1, 8]
    le due posizioni devono essere separate da un solo spazio

    se la lunghezza della stringa fornita in input è diversa
    da 5 il programma viene terminato

    Returns
    -------
    list
        posizione di partenza
    list
        posizione di destinazione

    """
    
    while True:
        mossa = input("Dammi la mossa: ")
        if not len(mossa) == 5:  # l'input non è una mossa
            exit(0)              # termina il programma
        partenza = [mossa[0].upper(), int(mossa[1])]
        destinazione = [mossa[3].upper(), int(mossa[4])]
        if in_board(partenza) and in_board(destinazione):
            return partenza, destinazione
        else:
            print(f'La partenza e/o la destinazione della mossa {mossa} non corrispondono a caselle della scacchiera')
            
def crea_scacchiera(scacchiera):
    
    '''
    Acquisisce una variabile di tipo Scacchiera e posiziona
    al suo interno i vari pezzi al loro posto

    Returns
    -------
    None.

    '''
    
    for i in range(1, 9):
        pb = Pedone('B')
        scacchiera.metti(pb, ['G', i])
        pw = Pedone('W')
        scacchiera.metti(pw, ['B', i])
        if i==1 or i==8:
            x = Torre('B')
            scacchiera.metti(x, ['H', i])  
            x = Torre('W')
            scacchiera.metti(x, ['A', i])
        elif i==2 or i==7:
            x = Cavallo('B')
            scacchiera.metti(x, ['H', i])  
            x = Cavallo('W')
            scacchiera.metti(x, ['A', i])
        elif i==3 or i==6:
            x = Alfiere('B')
            scacchiera.metti(x, ['H', i])  
            x = Alfiere('W')
            scacchiera.metti(x, ['A', i])
        elif i==4:
            king_b = Re('B')
            scacchiera.metti(king_b, ['H', i])  
            x = Regina('W')
            scacchiera.metti(x, ['A', i])
        elif i==5:
            x = Regina('B')
            scacchiera.metti(x, ['H', i])  
            king_w = Re('W')
            scacchiera.metti(king_w, ['A', i])


if __name__ == "__main__":
    # setup del gioco
    scacchiera = Scacchiera()
    # posiziono i pezzi sulla scacchiera
    crea_scacchiera(scacchiera) 
        
    scacchiera.visualizza()
    print()
    
    eliminati_bianchi=[]
    eliminati_neri=[]
    
# inizia il gioco
while True:
    while True:
        # acquisisce mossa da fare
        (partenza, destinazione) = get_mossa()
        # recupera il pezzo da muovere
        pezzo = scacchiera.get_pezzo(partenza)
        # muovi il pezzo sulla scacchiera
        if pezzo.verifica_mossa(destinazione): # la mossa è legale
            break
    # esegui mossa sulla scacchiera
    if not scacchiera.get_pezzo(destinazione) == None:
        if scacchiera.get_pezzo(destinazione).colore == 'W':
            eliminati_bianchi.append(scacchiera.get_pezzo(destinazione))
        else:
            eliminati_neri.append(scacchiera.get_pezzo(destinazione))
        scacchiera.togli(destinazione)
    scacchiera.togli(partenza)
    scacchiera.metti(pezzo, destinazione)

    scacchiera.visualizza()
    print()

