import re


def parse_record(record):
    record_moves = []
    for game in record:
        record_moves.append(re.sub(';|,|\n', '', game[game.find(':') + 2:]).split(' '))

    return record_moves


def calculate_power(record_moves):
    power_sum = 0
    for game in record_moves:
        max_red = 0
        max_green = 0
        max_blue = 0
        for i in range(1, len(game), 2):
            if game[i] == 'red':
                if max_red < int(game[i - 1]):
                    max_red = int(game[i - 1])

            elif game[i] == 'green':
                if max_green < int(game[i - 1]):
                    max_green = int(game[i - 1])

            elif game[i] == 'blue':
                if max_blue < int(game[i - 1]):
                    max_blue = int(game[i - 1])

        power_sum += max_red * max_green * max_blue

    return power_sum

def evaluate_games(record_moves):
    id = 1
    id_sum = 0
    for game in record_moves:
        possible = True
        for i in range(1, len(game), 2):
            if game[i] == 'red' and int(game[i - 1]) > 12:
                possible = False
                break

            elif game[i] == 'green' and int(game[i - 1]) > 13:
                possible = False
                break

            elif game[i] == 'blue' and int(game[i - 1]) > 14:
                possible = False
                break

        if possible:
            id_sum += id
        id += 1

    return id_sum


def main():
    f = open('game_record.txt', 'r')
    record_moves = parse_record(f.readlines())

    id_sum = evaluate_games(record_moves)
    print('Sum of IDs of possible games', id_sum)

    power_sum = calculate_power(record_moves)
    print('Sum of power of the minimum set of cubes', power_sum)


main()