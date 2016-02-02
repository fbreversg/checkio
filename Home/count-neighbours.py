def count_neighbours(grid, row, col):
    
    NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    count = 0

    for vecino in NEIGHBORS:
        try: 
            if ((row+vecino[0]) >= 0) and ((row+vecino[0]) < len(grid)) and ((col+vecino[1]) >= 0) and ((col+vecino[1]) < len(grid)):
                if grid[row+vecino[0]][col+vecino[1]]:
                    count += 1
        except:
            pass
    return(count)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    assert сount_neighbours(((1,0,1,0,1),(0,1,0,1,0),(1,0,1,0,1),(0,1,0,1,0),(1,0,1,0,1),(0,1,0,1,0),), 5, 4) == 2, "Ejemplo"
    
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
   
