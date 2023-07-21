import replit
import random
import hangman_words, hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    replit.clear()
    if guess in display:
        print("You've already guessed this letter")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'You guessed letter "{guess}", that is not in the word.\nYou lost a life. Remaining lives: {lives-1}')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won.")

    print(hangman_art.stages[lives])
    
input("Press enter to exit;")