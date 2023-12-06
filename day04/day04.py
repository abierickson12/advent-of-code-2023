import re


# Extract a list of the winning numbers and a list of the numbers that were scratched off by the elf
# for each game
def parse_scratchcards(scratchcards):
    winning_numbers = []
    scratched_numbers = []

    for card in scratchcards:
        winning_numbers.append(list(filter(None, card[card.find(':') + 2:card.find('|') - 1].split(' '))))
        scratched_numbers.append(card[card.find('|') + 1: card.find('\n')].split(' '))

    return winning_numbers, scratched_numbers


# Count the number of winning numbers that were scratched off per game and calculate
# the score based on the scoring system
def calculate_card_points(winning_numbers, scratched_numbers):
    scores = []
    rounds = len(winning_numbers)
    for i in range(rounds):
        count = len([j for j in winning_numbers[i] if j in scratched_numbers[i]])
        if count != 0:
            # The score is exponential to the count of winning numbers per game
            scores.append(pow(2, count - 1))

    return scores


def main():
    f = open('scratchcards.txt', 'r')
    scratchcards = f.readlines()

    winning_numbers, scratched_numbers = parse_scratchcards(scratchcards)
    scores = calculate_card_points(winning_numbers, scratched_numbers)
    print("Total points for the elf's pile of scratchcards:", sum(scores))


main()
