import time
import os

# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Heart shape with stars
def heart():
    print("\n" * 2)
    for y in range(15, -15, -1):
        row = ""
        for x in range(-30, 30):
            if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0:
                row += "*"
            else:
                row += " "
        print(row)
    print("\n" * 2)

# Typing effect
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Main love proposal
def love_proposal():
    clear()
    heart()
    time.sleep(1)
    messages = [
        "Hey... ❤️",
        "I have something special to tell you...",
        "From the moment we met,",
        "You’ve made my world brighter and my heart fuller.",
        "So here it goes...",
        "",
        "Will you be mine? 💍💖",
    ]

    for message in messages:
        type_text(message)
        time.sleep(1)

    print("\n" + " " * 10 + "❤️ Yes    💔 No")

# Run the proposal
love_proposal()
