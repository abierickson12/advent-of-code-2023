# Obtain indices of matrix cells that are adjacent to the number
def get_adjacent_indices(row, start_index, end_index, max_row, max_column):
    indices = []
    if start_index > 0:
        # Check column/row of the part number's first character to prevent an index
        # out of bounds error
        indices.append([row, start_index - 1])
        if row > 0:
            # Upper left diagonal index
            indices.append([row - 1, start_index - 1])
        if row < max_row:
            # Lower left diagonal index
            indices.append([row + 1, start_index - 1])
    if end_index < max_column:
        # Check column/row of the part number's last character to prevent an index
        # out of bounds error
        indices.append([row, end_index + 1])
        if row > 0:
            # Upper right diagonal index
            indices.append([row - 1, end_index + 1])
        if row < max_row:
            # Lower right diagonal index
            indices.append([row + 1, end_index + 1])
    if row > 0:
        # Indices directly above digits
        for i in range(start_index, end_index + 1):
            indices.append([row - 1, i])
    if row < max_row:
        # Indices directly below digits
        for i in range(start_index, end_index + 1):
            indices.append([row + 1, i])

    return indices


# Determine if the number is adjacent to a symbol in the schematic and therefore a part number
def is_part(row, start_index, end_index, schematic_matrix):
    max_row = len(schematic_matrix) - 1
    max_column = len(schematic_matrix[row]) - 2
    indices = get_adjacent_indices(row, start_index, end_index, max_row, max_column)
    for x, y in indices:
        if not schematic_matrix[x][y].isdigit() and schematic_matrix[x][y] != '.':
            return True

    return False


# Extract the start index and end index consecutive digits in the matrix to track numbers
def parse_numbers(schematic_matrix):
    number_indices = []
    rows = len(schematic_matrix)
    columns = len(schematic_matrix[0]) - 1
    for i in range(rows):
        j = 0
        while j < columns:
            if schematic_matrix[i][j].isdigit():
                number = schematic_matrix[i][j]
                j += 1
                while schematic_matrix[i][j].isdigit():
                    number += schematic_matrix[i][j]
                    j += 1
                number_indices.append([i, j, number])
            j += 1

    return number_indices


# Determine which numbers in the schematic are missing part numbers
def locate_missing_parts(number_indices, schematic_matrix):
    part_numbers = []
    for number in number_indices:
        if is_part(number[0], number[1] - len(number[2]), number[1] - 1, schematic_matrix):
            part_numbers.append(int(number[2]))

    return part_numbers


# Locate the indices of the * symbol and track adjacent part numbers in a dict
def locate_gears(number_indices, schematic_matrix):
    asterisk_part_numbers = {}
    max_row = len(schematic_matrix) - 1
    max_column = len(schematic_matrix[0]) - 2
    for number in number_indices:
        indices = get_adjacent_indices(number[0], number[1] - len(number[2]), number[1] - 1, max_row, max_column)
        for x, y in indices:
            if schematic_matrix[x][y] == '*':
                asterisk_key = str(x) + ':' + str(y)
                if asterisk_key in asterisk_part_numbers.keys():
                    asterisk_part_numbers[asterisk_key].append(number[2])
                else:
                    asterisk_part_numbers[asterisk_key] = [number[2]]

    return asterisk_part_numbers


def main():
    f = open('engine_schematic.txt', 'r')
    schematic = f.readlines()
    schematic_matrix = [list(line) for line in schematic]
    schematic_matrix[len(schematic_matrix) - 1].append('\n')
    number_indices = parse_numbers(schematic_matrix)

    # Part 1
    part_numbers = locate_missing_parts(number_indices, schematic_matrix)
    print('Sum of missing part numbers:', sum(part_numbers))

    # Part 2
    gear_ratio_sum = 0
    asterisk_numbers = locate_gears(number_indices, schematic_matrix)
    # A gear can only have exactly two adjacent part_numbers
    for entry in asterisk_numbers:
        part_numbers = asterisk_numbers[entry]
        if len(part_numbers) == 2:
            gear_ratio_sum += int(part_numbers[0]) * int(part_numbers[1])
    print('Sum of gear ratios:', gear_ratio_sum)


main()