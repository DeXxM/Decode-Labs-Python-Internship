"""
QUIZ MASTER - A 3-Question Quiz Game
------------------------------------
Key skill : Control Flow (if / elif / else) + Variables
What it does:
    * Asks the player's name and greets them
    * Asks 3 multiple-choice questions
    * Uses if / else to check each answer and update a score counter (+1 per correct answer)
    * Prints a final score, a percentage, and a personalised result message
    * Lets the player replay without restarting the program
"""

import time

LINE = "=" * 46


def pause(seconds=0.6):
    """Small delay so the game feels alive."""
    time.sleep(seconds)


def ask_question(number, question, options, correct_letter):
    """
    Shows one question, reads the player's answer and returns:
        1 -> correct answer
        0 -> wrong answer
    """
    print(f"\nQuestion {number} of 3")
    print("-" * 46)
    print(question)
    for letter, text in options.items():
        print(f"   {letter}) {text}")

    # Keep asking until the player enters a valid option (A/B/C/D)
    answer = input("\nYour answer: ").strip().upper()
    while answer not in options:
        print("Please type only A, B, C or D.")
        answer = input("Your answer: ").strip().upper()

    # ---- CONTROL FLOW: the heart of the project ----
    if answer == correct_letter:
        print("✅ Correct! +1 point")
        return 1
    else:
        print(f"❌ Wrong! The correct answer was {correct_letter}) {options[correct_letter]}")
        return 0


def show_result(name, score, total):
    """Prints the final score and a message chosen with if / elif / else."""
    percentage = round(score / total * 100)

    print("\n" + LINE)
    print("               FINAL RESULT")
    print(LINE)
    print(f"Player : {name}")
    print(f"Score  : {score} / {total}   ({percentage}%)")
    print("Stars  : " + "⭐" * score + "☆" * (total - score))
    print(LINE)

    if score == 3:
        print(f"🏆 PERFECT SCORE, {name}! You are a Quiz Master!")
    elif score == 2:
        print(f"🎉 Great job, {name}! Just one away from perfect.")
    elif score == 1:
        print(f"🙂 Not bad, {name}. A little more practice and you'll nail it.")
    else:
        print(f"💪 Don't give up, {name}! Try again and beat your score.")


def play_game():
    """Runs one full round of the quiz."""
    print("\n" + LINE)
    print("          🎮  WELCOME TO QUIZ MASTER  🎮")
    print(LINE)

    name = input("Enter your name: ").strip()
    if name == "":
        name = "Player"   # default value if the name is left blank

    print(f"\nHello, {name}! Answer 3 questions. Each correct answer = 1 point.")
    pause()

    score = 0   # the score counter variable

    score += ask_question(
        1,
        "What is the capital of France?",
        {"A": "London", "B": "Paris", "C": "Madrid", "D": "Berlin"},
        "B",
    )
    pause()

    score += ask_question(
        2,
        "Which planet is known as the Red Planet?",
        {"A": "Mars", "B": "Venus", "C": "Jupiter", "D": "Saturn"},
        "A",
    )
    pause()

    score += ask_question(
        3,
        "Which Python keyword is used to make a decision?",
        {"A": "for", "B": "def", "C": "if", "D": "import"},
        "C",
    )
    pause()

    show_result(name, score, 3)


def main():
    play_again = "Y"
    while play_again == "Y":
        play_game()
        play_again = input("\nPlay again? (Y/N): ").strip().upper()
        if play_again != "Y":
            print("\nThanks for playing Quiz Master! 👋")


if __name__ == "__main__":
    main()