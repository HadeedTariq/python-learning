import argparse

parser = argparse.ArgumentParser(description="Guess Number Game")
parser.add_argument(
    "-n", "--name", required=True, metavar="name", help="Enter your name"
)
args = parser.parse_args()
name = str(args.name)
choice = None


def arcade_start():
    global choice
    print(f"\n{name} welcome to the arcade")
    print("Please choose the game")
    print("1")
    print("2")
    print("Or press x to exit")
    choice = str(input(""))


arcade_start()
while choice != "x":
    from guess_number import game_play, ending_game

    game_play(name)
    ending_game(name)
    arcade_start()
