from random import randint

grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

moves = {"A": 0, "B": 1, "C": 2}

avail_moves = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]]

def print_grid():
    output =""
    for row in grid:
        output += "|"
        for column in row: 
            output += column + "|"
        print(output)
        output = ""

def player_move(grid):
    choice = input("please choose a move: ")
    grid[int(choice[1])-1][moves[choice[0]]] = "X"

def comp_move(grid):
    pass
    #get list of available moves
    #randint to pick an option
    
def main():
    print_grid()
    player_move(grid)
    print_grid()

if __name__ == "__main__":
    main()

