import argparse
import random

game_count = 0
user_wins = 0
user_wins_percentage = 0
choice = None

if __name__ == "__main__":
    name = None
    choice = "choice"
    parser = argparse.ArgumentParser(description="Guess Number Game")
    parser.add_argument(
        "-n", "--name", required=True, metavar="name", help="Enter your name"
    )
    args = parser.parse_args()
    name = str(args.name)


def game_play(name="Player One"):
    global game_count
    global user_wins
    global user_wins_percentage
    global choice
    # real logic
    game_count += 1
    num = random.randrange(1, 4)
    user_choice = input(f"{name.capitalize()} Guess which number I am thinking of: ")
    user_choice = int(user_choice)
    print(f"\n{name} you choose {user_choice}")
    print(f"\nI was thinking about the number {num}")
    if user_choice == num:
        user_wins += 1
        print(f"\n{name}, you win")
    else:
        print(f"\n{name}, you lose")
    print(f"\nGame's Count: {game_count}")
    print(f"\n{name}'s wins: {user_wins}")
    print(f"\nYour winning percentage: {float(user_wins*100/game_count)}%")
    print(f"\nPlay again, {name}?")
    choice = input("\nY for Yes\nQ for quit\n")
    while str(choice).lower() == "y":
        game_play(name)


if choice and str(choice).lower() != "q":
    game_play(name)


def ending_game(name):
    if choice == "q":
        print(f"\nThankyou for playing {name}")
        print("Bye")


if __name__ == "__main__":
    ending_game(name)
