from copy import deepcopy 

class Board():
    def __init__(self, board=None): 
        self.player_1 = "x"
        self.player_2 = "o"
        self.empty_square = "."

        self.position = {}

        self.init_board()

        if board is not None: 
            self.__dict__ = deepcopy(board.__dict__)

    def init_board(self): 
        for row in range(3):
            for col in range(3):
                self.position[row, col] = self.empty_square

    def make_move(self, row, col): 
        board = Board(self) 
        board.position[row, col] = self.player_1

        (board.player_1, board.player_2) = (board.player_2, board.player_1)
    
        return board

    def generate_states(self):
        actions = [] 

        for row in range(3):
            for col in range(3):
                if self.position[row, col] == self.empty_square:
                    actions.append(self.make_move(row, col))
        
        return actions


    def is_draw(self):
        for row, col in self.position: 
            if self.position[row, col] == self.empty_square:
                return False 
        return True
    
    def is_win(self):
        player = self.player_2 
        return self.__is_win_or_lose(player)

    def is_lose(self):
        player = self.player_1
        return self.__is_win_or_lose(player)


    def __is_win_or_lose(self, player):
        # by default player_2 is always user and player_1 is AI

        # vertical sequence
        for col in range(3):
            winning_sequence = []
            for row in range(3): 
                if self.position[row, col] == player:
                    winning_sequence.append(player)
            
                if len(winning_sequence) == 3: 
                    return True 

        # horizontal sequence 
        for row in range(3):
            winning_sequence = [] 
            for col in range(3): 
                if self.position[row, col] == player: 
                    winning_sequence.append(player)
                
                if len(winning_sequence) == 3:
                    return True

        # 1st diagonal sequence 
        winning_sequence = [] 
        for row in range(3):
            col = row
            if self.position[row, col] == player:
                winning_sequence.append(player)
        if len(winning_sequence) == 3:
            return True
                

        # 2nd diagonal sequence
        winning_sequence = [] 
        for row in range(3):
            col = 2 - row
            if self.position[row, col] == player:
                winning_sequence.append(player)
        if len(winning_sequence) == 3:
            return True
        
        return False 
    
    def __str__(self):
        board_string = "" 
        for row in range(3):
            for col in range(3):
                board_string += " {}".format(self.position[row, col])
            
            board_string += "\n"
        
        return board_string


if __name__ == "__main__":
    board = Board()
    print('This is initial board state:')
    print(board)

    # generate available actions
    actions = board.generate_states()
    
    # take action (make move on board)
    board = actions[0]
    
    # print updated board state
    print('first generated move has been made on board:')
    print(board)
    
    # generate available actions after first move has been made
    actions = board.generate_states()

    # take action (make move on board)
    board = actions[3]
    print(board)

    # generate available actions after first move has been made
    actions = board.generate_states()
    
    print('\n\n\n\n Generating states...')
    # loop over generated action
    for action in actions:
        # print current action
        print(action)
    



                    
            
            

        
