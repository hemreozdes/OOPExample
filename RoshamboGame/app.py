import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.move = None
        self.score = 0
#This decorator states that the make_move method must be defined in subclasses.
    @abstractmethod
    def make_move(self):
#This method will allow a player to make his move.
        pass

class ComputerPlayer(Player):
    def __init__(self, name: str = "Computer"):
        super().__init__(name)
#The name of the computer is set to "Computer"
    @abstractmethod
    def make_move(self):
#The make_move method is abstract and needs to be filled in subclasses.
        pass

class RandomComputerPlayer(ComputerPlayer):
    def __init__(self):
        super().__init__("Computer")
    def make_move(self):
        self.move = random.choice(['rock', 'paper', 'scissors'])
#The make_move method, randomly chooses a move
        return self.move

class HumanPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)
    def make_move(self):
        move = input(f"{self.name}, please enter your move (rock, paper, scissors): ").lower()
#In the make_move method, the user is asked to enter a move
        while move not in ['rock', 'paper', 'scissors']:
            print("Invalid move! Please try again.")
            move = input(f"{self.name}, please enter your move (rock, paper, scissors): ").lower()
#If an invalid move is entered, it's asked again until a correct move is entered
        self.move = move
        return self.move

def determine_winner(player1: Player, player2: Player):
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
#The winning_combinations dictionary defines winning combinations.
    print(f"{player1.name} chose {player1.move}, {player2.name} chose {player2.move}")
    if player1.move == player2.move:
        print("It's a tie!")
        return None
    elif winning_combinations[player1.move] == player2.move:
        print(f"{player1.name} wins this round!")
        player1.score += 1
        return player1
    else:
        print(f"{player2.name} wins this round!")
        player2.score += 1
        return player2

def display_scores(player1: Player, player2: Player):
    print(f"\nScores: {player1.name}: {player1.score}, {player2.name}: {player2.score}\n")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    player_name = input("Enter your name: ")
    human = HumanPlayer(player_name)
    
    computer = RandomComputerPlayer()
    rounds_played = 0
    move_history = []
    while True:
        print(f"\nRound {rounds_played + 1}:")
        human_move = human.make_move()
        computer_move = computer.make_move()
        move_history.append((human_move, computer_move))
        determine_winner(human, computer)
        display_scores(human, computer)
        rounds_played += 1
        continue_game = input("Do you want to play another round? (yes/no): ").lower()
        if continue_game != 'yes':
            break
    print("\nFinal Scores:")
    display_scores(human, computer)
    print("\nMove History:")
    for i, (human_move, computer_move) in enumerate(move_history, start=1):
        print(f"Round {i}: {human.name} chose {human_move}, {computer.name} chose {computer_move}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()