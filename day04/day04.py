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
def calculate_card_matches(winning_numbers, scratched_numbers):
    win_count = []
    rounds = len(winning_numbers)
    for i in range(rounds):
        count = len([j for j in winning_numbers[i] if j in scratched_numbers[i]])
        win_count.append(count)

    return win_count


def main():
    f = open('scratchcards.txt', 'r')
    scratchcards = f.readlines()

    # Part 1
    winning_numbers, scratched_numbers = parse_scratchcards(scratchcards)
    win_count = calculate_card_matches(winning_numbers, scratched_numbers)
    scores = []
    for matches in win_count:
        # The score is exponential to the count of winning numbers per game
        if matches != 0:
            scores.append(pow(2, matches - 1))

    print("Total points for the elf's pile of scratchcards:", sum(scores))

    # Part 2
    count = len(winning_numbers)
    total_cards = [1] * count
    for i in range(count):
        first_copies = win_count[i]
        for j in range(1, first_copies + 1):
            total_cards[i+j] += total_cards[i]

    print('Total original and copied scratchcards:', sum(total_cards))


main()
