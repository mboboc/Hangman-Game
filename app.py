# The HANGMAN Game
# Boboc Madalina
# 2019


def game():
    # states of the human
    states = [
                    "   __________      \n"
                    "   |        |      \n"
                    "   |               \n"
                    "   |               \n"
                    "   |               \n"
                    "   |               \n"
                    "   |               \n"
                    "  _|_________      \n",

                    "   __________      \n"
                    "   |       _|_     \n"
                    "   |      (0 0)    \n"
                    "   |               \n"
                    "   |               \n"
                    "   |               \n"
                    "   |               \n"
                    "  _|_________      \n",
                    "   __________      \n"
                    "   |       _|_     \n"
                    "   |      (0 0)    \n"
                    "   |        |      \n"
                    "   |        |      \n"
                    "   |               \n"
                    "   |               \n"
                    "  _|_________      \n",

                    "   __________      \n"
                    "   |       _|_     \n"
                    "   |      (0 0)    \n"
                    "   |     Ɛ--|--3   \n"
                    "   |        |      \n"
                    "   |               \n"
                    "   |               \n"
                    "  _|_________      \n",

                    "   __________      \n"
                    "   |       _|_     \n"
                    "   |      (0 0)    \n"
                    "   |     Ɛ--|--3   \n"
                    "   |        |      \n"
                    "   |       / \\      \n"
                    "   |     =     =    \n"
                    "  _|_________      \n"
            ]
    dictionary = ["winner", "beautiful", "challenge", "behaviour", "clowning", "gaming"]
    count = state_idx = guessed = 0
    enter = "?"

    print("\nWelcome to The HANGMAN GAME\nPress ENTER to start...\n")
    while enter != '':
        enter = input()

    # for every word in the dictionary play game until user loses
    for word in dictionary:
        count += 1
        # set initial form of the word
        user_word = []
        for i in range(len(word)):
            user_word.append("_")
            guessed = state_idx = 0
        # play game until user guesses or loses
        while guessed == 0 and state_idx < len(states):
            print("--- Level {}/{} ---".format(count, len(dictionary)))
            print(states[state_idx])
            print(user_word)
            print("\n")
            letter = input()
            letter = letter.lower()
            if letter != "" and letter != "\n":
                if letter in word:
                    if letter in user_word:
                        pos = user_word[::-1].index(letter)
                    else:
                        pos = 0
                    idx = word.index(letter, pos)
                    user_word[idx] = letter
                    if "_" not in user_word:
                        print("Guessed word: {}".format(word.upper()))
                        guessed = 1
                        print("You WON!\nWant to go to the NEXT LEVEL?\nPress ENTER ...\n\n"
                              "Press q if you want to leave...")
                        action = "_"
                        while action != "" and action != 'q':
                            action = input()
                            action = action.lower()
                        if action == "":
                            break
                        else:
                            print("Quitting...")
                            return
                else:
                    state_idx += 1
            else:
                state_idx += 1
        if state_idx == len(states):
            print("GAME OVER!\nYOU LOST!\n")
            return


game()
