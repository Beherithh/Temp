from random import randint

wordsList = ['python']

while True:
    errors = 0
    choice = int(input("Enter 1 to play hangman, 2 to add a new word, 3 to quit program: "))

    if choice == 2:
        newWord = input("Enter new word: ")
        wordsList.append(newWord)
        print(f"Added {newWord}")
    elif choice == 3:
        break
    elif choice == 1:
        word = wordsList[randint(0, len(wordsList) - 1)]
        guessedLetters = []
        rightLetters = []

        while errors <= 6:
            print(' +---+')
            print('  |   |')
            if errors >= 1:
                print('  O   |')
            else:
                print('      |')

            if errors >= 4:
                print(' /|\  |')
            elif errors >= 3:
                print(' /|   |')
            elif errors >= 2:
                print('  |   |')
            else:
                print('      |')

            if errors == 6:
                print(' / \  |')
            elif errors >= 5:
                print('   \  |')
            else:
                print('      |')
            print('      |')
            print('=========')
            if errors == 6:
                print(word)
                print('You lose!')
                break
            print('Guessed letters: ', end="")
            print(*guessedLetters, sep=",")

            for i in word:
                if i in rightLetters:
                    print(i, end="")
                else:
                    print('-', end="")

            letter = input('\nEnter letter: ')
            guessedLetters.append(letter)
            if letter in word:
                rightLetters.append(letter)
            else:
                errors += 1

            if set(rightLetters) == set(word):
                print(word)
                print('You win!')
                break
