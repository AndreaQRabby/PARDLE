import unidecode

with open("60000_parole_italiane.txt", "r") as file_in:
    five_letters = []
    for word in file_in:
        word = word.strip()
        if(len(word)==5 and not "\'" in word):
            five_letters.append(word.upper() + "\n")


with open("all_five.txt", "w") as file_out:
    for w in five_letters:
        file_out.write(w)

