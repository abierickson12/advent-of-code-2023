# Determine if the number is adjacent to a symbol in the schematic
def is_part(row, start_index, end_index, schematic_matrix):
    indices = []
    # Obtain indices of matrix cells that are adjacent to the part number
    if start_index > 0:
        # Check column/row of the part number's first character to prevent an index
        # out of bounds error
        indices.append([row, start_index - 1])
        if row > 0:
            # Upper left diagonal index
            indices.append([row - 1, start_index - 1])
        if row < len(schematic_matrix) - 1:
            # Lower left diagonal index
            indices.append([row + 1, start_index - 1])
    if end_index < len(schematic_matrix[row]) - 2:
        # Check column/row of the part number's last character to prevent an index
        # out of bounds error
        indices.append([row, end_index + 1])
        if row > 0:
            # Upper right diagonal index
            indices.append([row - 1, end_index + 1])
        if row < len(schematic_matrix) - 1:
            # Lower right diagonal index
            indices.append([row + 1, end_index + 1])
    if row > 0:
        # Indices directly above digits
        for i in range(start_index, end_index + 1):
            indices.append([row - 1, i])
    if row < len(schematic_matrix) - 1:
        # Indices directly below digits
        for i in range(start_index, end_index + 1):
            indices.append([row + 1, i])

    # Search for a symbol in adjacent cells
    for x, y in indices:
        if not schematic_matrix[x][y].isdigit() and schematic_matrix[x][y] != '.':
            return True

    return False


# Determine which numbers in the schematic are missing part numbers
def locate_missing_parts(schematic_matrix):
    part_numbers = []
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
                if is_part(i, j - len(number), j - 1, schematic_matrix):
                    part_numbers.append(int(number))
            j = j + 1

    return part_numbers


def main():
    f = open('engine_schematic.txt', 'r')
    schematic = f.readlines()
    schematic_matrix = [list(line) for line in schematic]
    schematic_matrix[len(schematic_matrix) - 1].append('\n')
    part_numbers = locate_missing_parts(schematic_matrix)

    print('Sum of missing part numbers:', sum(part_numbers))

main()