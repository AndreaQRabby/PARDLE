import unidecode

with open("1000_parole_italiane_comuni.txt", "r") as file_in:
    five_letters = []
    for word in file_in:
        #check for accents and length
        if(len(word)==5+1 and unidecode.unidecode(word)==word and not "\'" in word):
            five_letters.append(word.upper())

common_five = open("common_five.txt", "a")
for w in five_letters:
    common_five.write(w)

common_five.close()

