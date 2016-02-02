def checkio(game_result):
    
    #check horizontals
    for row in game_result:
        if (''.join(row)) == 'XXX':
            return "X"
        elif (''.join(row)) == 'OOO':
            return "O"
            
    #check verticals
    for i in range(3):
        if game_result[0][i] == game_result[1][i] == game_result[2][i] != '.':
            if game_result[0][i] == 'X':
                return "X"
            else:
                return "O"
    
    #check diagonals
    if (game_result[0][0] == game_result[1][1] == game_result[2][2] != '.') or (game_result[0][2] == game_result[1][1] == game_result[2][0] != '.'):
        if game_result[1][1] == 'X':
            return "X"
        else:
            return "O"
            
    return "D"
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

