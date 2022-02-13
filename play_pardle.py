# https://www.youtube.com/watch?v=SyWeex-S6d0

from pardle import Pardle
from colorama import Fore
from typing import List
from letter_state import LetterState
import random


def main():
    print("\n\n\n\n\n\n\n\n\n")
    print("--- PARDLE! ---")
    print("\n\n\n\n\n\n\n\n\n")

    # Import common word list and select random one as solution
    common_set = load_word_set("DATA/common_five.txt")
    secret = random.choice(list(common_set))
    pardle = Pardle(secret)
    # Import list with tryable words
    word_set = load_word_set("DATA/all_five.txt")

    while pardle.can_attempt:
        x = input("\nIndovina la PARDLA: ")
        
        if len(x) != pardle.WORD_LENGTH:
            print(Fore.RED + f"La parola deve essere lunga {pardle.WORD_LENGTH} caratteri!\n" + Fore.RESET)
            continue
        if x not in word_set:
            print(Fore.RED + f"Nope, non conosco la tua parola!\n" + Fore.RESET)
            continue

        pardle.attempt(x)
        display_results(pardle)

    if pardle.is_solved:
        print(Fore.GREEN + "\nWOW: Complimenti!\n\n" + Fore.RESET)
    else:
        print(Fore.RED + "\nSei un fallimento." + Fore.RESET)
        print(f"La parola era: {pardle.secret}" + "\n\n")



def display_results(pardle: Pardle):
    if(pardle.remaining_attempts > 0):
        print("\nLe tue parole fino ad ora...")
        print(f"Hai ancora {pardle.remaining_attempts} tentativi")

    lines = []

    for word in pardle.attempts:
        result = pardle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(pardle.remaining_attempts):
        lines.append(" ".join(["_"] * pardle.WORD_LENGTH))
    
    draw_border_around(lines)
    ## TODO: ADD CONTROLLO DELLE LETTERE USATE
    #print(" A B C D E F G ...")
    


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

if __name__ == '__main__':
    main()
