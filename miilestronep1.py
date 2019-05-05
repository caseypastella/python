from IPython.display import clear_output 
import random 

def display_board(board):
    
    print(' ')
    print(' ' + board[1] + '   |   '+ board[2] + '   |   ' + board[3]) 
    print()
    print(' ' '-----------------')  
    print()
    print(' ' + board[4] + '   |   ' +board[5] + '   |   ' + board[6])
    print()
    print(' ' '-----------------')
    print()
    print(' ' + board[7] + '   |   ' +board[8] + '   |   ' + board[9])
    


def player_input():
    player_marker = '' 
    while player_marker != 'X' and player_marker != 'O':
        player_marker = input('Player 1, Please choose X or O: ').upper()
    
    if player_marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X') 

def place_marker(board, marker, position): 
    board[position] = marker
    

def win_check(board, mark): 
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    else: 
        return False


def choose_first(): 
    if random.randint(0,1) == 0:
        return 'player 2'
        print('Player 1 will go first ') 
    else: 
        return 'player 1'
        print('Player 2 will go first ')
        
def space_check(board,position):
    return board[position] == ' '
            
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True   
    
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Please choose a number between 1 - 9: '))
        
    return position
def replay(): 
    return input('Type yes or no to play again: ').upper() 
     
      
    
print('Welcome to Tic Tac Toe!') 


while True: 
    
    theboard = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Want to play enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        gameon = True
    else: 
        gameon = False 
    
    while gameon == True: 
        if turn == 'Player 1'.lower(): 
             
            display_board(theboard)
            position = int(player_choice(theboard))
             
            place_marker(theboard, player1_marker, position) 
             
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('Congrats you have won the game') 
                gameon = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('You have tied')
                    break
                else:
                    turn = 'Player 2'
                    
             
        else: 
            display_board(theboard)
            position = player_choice(theboard)
             
            place_marker(theboard, player2_marker, position) 
             
            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('Player 2 has won!') 
                gameon = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('You have tied')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break