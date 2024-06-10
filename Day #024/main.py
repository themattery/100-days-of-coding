PLACEHOLDER = '[name]'


with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names_list:
        name = name.strip("\n")
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/Letter_for_{name}", mode="w") as finished_letter:
            finished_letter.write(new_letter)
