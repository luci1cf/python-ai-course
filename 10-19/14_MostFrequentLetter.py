# Find Most Frequent Letters in Wordd

# Variables
#-----------------------------------------------------------------------------
random_words = [
    "Lighthouse", "Cat", "Umbrella", "Giraffe",
    "Success", "Volcano", "Balloon",
    "Butterfly", "Mississippi", "Strawberry"
]

# Functions
#---------------------------------------------------------------------------------
def most_frequent_letters(word):
    print('-'*50)
    print(f'Checking word: {word}')

    # Count Letters
    word = word.lower()
    dict_count = {}

    for letter in word:
        if letter not in dict_count:
            count = word.count(letter)
            dict_count[letter] = count

    # Print Reports
    for letter, count in dict_count.items():
        if count > 1:
            print(f'{letter} used {count} times.')
        else:
            print(f'{letter} used {count} time.')

    # Find Max Count Letters
    max_count = max(dict_count.values())
    max_letters =  []
    for k, v in dict_count.items():
        if v == max_count:
            max_letters.append(k)

    # Report Results
    print(f'The most frequent letter {max_letters}. Used {max_count} times.')

    return max_letters, max_count

# Main
#----------------------------------------------------------------------------------

for word in random_words:
    results = most_frequent_letters(word)
    # letters = results[0]
    # count   = results[1]
    # print(letters, count)