board = [" " for x in range(10)]


def full_board():
    return board.count(" ") == 1
def print_board():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("------")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("------")
    print(board[7] + "|" + board[8] + "|" + board[9])

def comp_turn():
    
    ret_move = 0
    possible_moves = [x for x in range(1, 10) if board[x] == " "]
    if len(possible_moves) > 0:
        for letter in ["O", "X"]:
            for pos_move in possible_moves:
                board_copy = board[:]
                board_copy[pos_move] = letter
                if isWin(letter):
                    ret_move = pos_move
                    return ret_move

        if not is_occupied(5):
            ret_move = 5
            return ret_move
        possible_corners = [x for x in [1, 3, 7, 9] if board[x] == " "]
        if len(possible_corners) > 0:
            ret_move = possible_corners[0]
            return ret_move
        possible_edges = [x for x in [2, 4, 6, 8] if board[x] == " "]
        if len(possible_edges) > 0:
            ret_move = possible_edges[0]
            return ret_move


    else:
        ret_move = 0
        return ret_move

    return ret_move

def is_occupied(pos):
    return board[pos]!= " "
def player_turn():

    while True:
        try:
            inp = input("please enter a number from 1-9 to place your x")
            play_move = int(inp)
            if (is_occupied(play_move)):
                print("already occupied")
                continue
            elif play_move > 9 or play_move < 1:
                print("must be between 1 or 9 inclusive")
                continue
            else:
                board[play_move] = "X"
                return


        except:
            print("please only enter a number")


def isWin(let):
    return in_row([1, 2, 3], let) or in_row([4, 5, 6], let) or in_row([7, 8, 9], let) or in_row([1, 4, 7], let) or in_row([2, 5, 8], let) or in_row([3, 6, 9], let) or in_row([1, 5, 9], let) or in_row([3, 5, 7], let)
def in_row(list, letter):
    for pos in list:
        if board[pos] != letter:
            return False
    return True


print_board()
while(not full_board()):
    if not isWin("O"):
        player_turn()
        print_board()
    else:
        print(" O the computer wins")
        break
    if not isWin("X"):
        comp_move = comp_turn()
        if comp_move == 0:
            print("draw, no one wins")
            break
        else:
            board[comp_move] = "O"
            print(" the computer put the O in position " + str(comp_move))
            print_board()

    else:
        print(" X (you) win!")
        break


if (full_board()):
    print("draw, no one wins")




