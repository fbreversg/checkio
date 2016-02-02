def safe_pawns(pawns):
    
    safe = 0
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    
    tableroInv=[[0 for j in range(8)] for i in range(8)]
    for position in pawns:
        tableroInv[int(position[1])-1][letras[position[0]]-1]=1
        
    
    tablero = tableroInv[::-1]
    
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == 1:
                checked = False
                if (i+1) < 8:
                    if (j-1) >= 0:
                        if tablero[i+1][j-1] == 1:
                            checked = True
                    if (j+1) < 8:
                        if tablero[i+1][j+1] == 1:
                            checked = True
                if checked:
                        safe += 1
                            
    return safe       
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
