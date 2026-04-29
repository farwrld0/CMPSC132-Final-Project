import random

def get_difficulty():
    """
    Ask the player to choose a difficulty level, using number 1, 2, or 3.
    Return the max number of the game, max attempts and the difficulty name.
    """
    print("Choose Game Difficulty")
    print("1. Easy Mode (1 - 50), 20 attempts")
    print("2. Medium Mode (1 - 100), 10 attempts")
    print("3. Hard Mode (1 - 200), 5 attempts")
    choice = input("Please Enter Game Difficulty (1, 2, 3): ").strip()
    while choice not in ["1", "2", "3"]:
        print("Input must be 1, 2, or 3, Please choose again!")
        choice = input("Please Enter Game Difficulty (1, 2, 3): ").strip()
    
    levels = {"1": (50, 20, "Easy Mode!"), "2": (100, 10, "Medium Mode!"), "3": (200, 5, "Hard Mode!")}
    max_num, max_attempts, difficulty = levels[choice]
    return max_num, max_attempts, difficulty
    
def get_guess(max_num):
    """
    Ask the player to enter a valid guess number to proceed the game, within the range.
    Return a valid integer guess.
    """
    guess = None
    while guess is None:
        value = input(f"Enter your guess number! (1 - {max_num}):")
        if value.isdigit():
            value = int(value)
            if 1 <= value <= max_num:
                guess = value
            else:
                print(f"Input must be between 1 and {max_num}, Please choose again!")
        else:
            print("Invalid input, Please enter a number")
    return guess

def get_hint(target, guess):
    """
    Calculate the difference between target and guess number.
    Return a hint str based on the difference.
    """
    diff = target - guess
    if diff < 0:
        diff = -diff
    if diff <= 2:
        return "One more step!!!"
    elif diff <= 5:
        return "Very close!!!"
    elif diff <= 15:
        return "Almost there!"
    elif diff <= 30:
        return "Keep trying..."
    else:
        return "Not even close!"

def play_game(stats):
    """
    The main loop of the whole game, for one round.
    Updates wins, losses and games in the stats, a dictionary.
    """
    max_num, max_attempts, difficulty = get_difficulty()
    target = random.randint(1, max_num)
    attempts = 0
    found = False
    print(f"[{difficulty}] The range of guessing number is between 1 and {max_num}")
    print(f"You will have {max_attempts} attempts")
    while not found and attempts < max_attempts:
        guess = get_guess(max_num)
        attempts += 1
        if guess < target:
            hint = get_hint(target, guess)
            print(f"Too Low! {hint} ({max_attempts - attempts} attempts remain)")
        elif guess > target:
            hint = get_hint(target, guess)
            print(f"Too High! {hint} ({max_attempts - attempts} attempts remain)")
        else:
            found = True
            print(f"Congratulations! The number is {target}")
            print(f"You got it in {attempts} attempts!")
    
    if found:
        stats["wins"] += 1
        stats["games"] += 1
    else:
        print(f"Out of attempts! the number is {target}")
        stats["losses"] += 1
        stats["games"] += 1
 
def show_stats(stats):
    """
    Show the player's overall game performance.
    """
    print(f"Games Played: {stats['games']}")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")

def ask_replay():
    """
    Ask the player if they want to play again or not.
    """
    choice = input("Do you want to play again? Enter yes/no: ").strip().lower()
    while choice not in ["yes", "no"]:
        print("Must enter yes or no!")
        choice = input("Do you want to play again? Enter yes/no: ").strip().lower()
    return choice in ["yes"]

def main():
    """
    Entry to the game.
    Set the stats to start and manage the game loop.
    """
    print("This is Number Guessing Game!")
    stats = {"games": 0, "wins": 0, "losses": 0}
    play = True
    while play:
        play_game(stats)
        show_stats(stats)
        play = ask_replay()
    print("Thank you for playing the Game!")

if __name__ == "__main__":
    main()
