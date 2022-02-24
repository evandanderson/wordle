import random, json

with open('words.json', 'r') as file:
    words = json.loads(file.read())


class Wordle:

    def __init__(self):
        self.word = words[random.randint(0,len(words))]


def validate(guess, word):
    validation = ''
    for i, char in enumerate(guess):
        if char == word[i]:
            validation += f'[*{char}*]'
        elif guess.count(char, i) <= word.count(char) and validation.count(f'*{char}*') < word.count(char):
            validation += f'[{char}*]'
        else:
            validation += f'[{char}]'
    return validation


def main():
    wordle = Wordle()
    remaining_guesses = 6
    while remaining_guesses > 0:
        guess = str(input()).lower()
        if guess.isalpha() and len(guess) == 5:
            remaining_guesses -= 1
            print(validate(guess, wordle.word))
            if guess == wordle.word:
                print('Success! Solved in ' + str(6 - remaining_guesses) + ' attempt(s)')
                break
        else:
            print('Word must be 5 characters')
    print('The word was: ' + wordle.word)

if __name__ == '__main__':
    main()