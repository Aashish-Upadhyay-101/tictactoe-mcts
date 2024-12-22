from copy import deepcopy 
from mcts import *

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

    def game_loop(self):
        print(self)

        mcts = MCTS() 

        while True: 
            user_input = input("> ")
            if user_input == "exit": break
            if user_input == "": continue 

            try:
                row = int(user_input.split(",")[0]) - 1
                col = int(user_input.split(",")[1]) - 1
                
                if self.position[row, col] != self.empty_square: 
                    print("Illegal move", self.position[row, col])
                    continue
                
                self = self.make_move(row, col)

                # AI move 
                best_move = mcts.search(self)
                try:
                    self = best_move.board
                except: 
                    pass
                print(self)

                if self.is_win():
                    print("player {} has won the game!".format(self.player_2))
                    break
                elif self.is_draw():
                    print("Game is draw!")
                    break

            except Exception as e: 
                print("Illegal move")
                

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
        # by default player_2 is always user and player_1 is AI

        # vertical sequence
        for col in range(3):
            winning_sequence = []
            for row in range(3): 
                if self.position[row, col] == self.player_2:
                    winning_sequence.append(self.player_2)
            
                if len(winning_sequence) == 3: 
                    return True 

        # horizontal sequence 
        for row in range(3):
            winning_sequence = [] 
            for col in range(3): 
                if self.position[row, col] == self.player_2: 
                    winning_sequence.append(self.player_2)
                
                if len(winning_sequence) == 3:
                    return True

        # 1st diagonal sequence 
        winning_sequence = [] 
        for row in range(3):
            col = row
            if self.position[row, col] == self.player_2:
                winning_sequence.append(self.player_2)
        if len(winning_sequence) == 3:
            return True
                

        # 2nd diagonal sequence
        winning_sequence = [] 
        for row in range(3):
            col = 2 - row
            if self.position[row, col] == self.player_2:
                winning_sequence.append(self.player_2)
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
    board.game_loop()
