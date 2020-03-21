import numpy as np
import colorama

INIT_PUZ = np.array(
    [
        [0, 1, 3],
        [4, 2, 5],
        [7, 8, 6]
    ]
)
ARRAY_SHAPE = INIT_PUZ.shape
FINAL_PUZ = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
)

# unicode
left_down_angle = '\u2514'
right_down_angle = '\u2518'
right_up_angle = '\u2510'
left_up_angle = '\u250C'

middle_junction = '\u253C'
top_junction = '\u252C'
bottom_junction = '\u2534'
right_junction = '\u2524'
left_junction = '\u251C'

bar = '\u2502'
dash = '\u2500'

first_line = left_up_angle + dash + dash + dash + top_junction + dash + dash + dash + top_junction + dash + dash + dash + right_up_angle
middle_line = left_junction + dash + dash + dash + middle_junction + dash + dash + dash + middle_junction + dash + dash + dash + right_junction
last_line = left_down_angle + dash + dash + dash + bottom_junction + dash + dash + dash + bottom_junction + dash + dash + dash + right_down_angle


class get_subsidiary_puzzle:

    def __init__(self, input_array):
        self.input_array = input_array
        self.blank_pos_value = self.blank_pos_func()
        self.valid_direction_value = self.valid_direction_func()

    def swap(self, input1, input2):
        temp = input1
        input1 = input2
        input2 = temp
        return input1, input2

    def valid_direction_func(self):
        valid_direction_pos = []
        if self.blank_pos_value[0] + 1 < ARRAY_SHAPE[0]:
            valid_direction_pos.append([self.blank_pos_value[0] + 1, self.blank_pos_value[1]])
        if self.blank_pos_value[0] - 1 >= 0:
            valid_direction_pos.append([self.blank_pos_value[0] - 1, self.blank_pos_value[1]])
        if self.blank_pos_value[1] + 1 < ARRAY_SHAPE[1]:
            valid_direction_pos.append([self.blank_pos_value[0], self.blank_pos_value[1] + 1])
        if self.blank_pos_value[1] - 1 >= 0:
            valid_direction_pos.append([self.blank_pos_value[0], self.blank_pos_value[1] - 1])
        return valid_direction_pos

    def blank_pos_func(self):
        for i in range(len(self.input_array)):
            for k in range(len(self.input_array[i])):
                if self.input_array[i][k] == 0:
                    return (i, k)

    def difference_count(self, input_array):
        b = FINAL_PUZ != input_array
        return len(input_array[b])

    def efficient_arrays(self, list_of_arrays):
        arrays = []
        for l in list_of_arrays:
            arrays.append({
                "difference": self.difference_count(l),
                "array": l,
            })
        arrays = sorted(arrays, key=lambda i: i['difference'])
        eff_arrays = []
        for a in arrays:
            if a['difference'] == arrays[0]['difference']:
                eff_arrays.append(a)
        return eff_arrays

    def new_test_puzzles(self):
        valid_puzzles = []
        for vp in self.valid_direction_value:
            self.input_array[vp[0]][vp[1]], self.input_array[self.blank_pos_value[0]][
                self.blank_pos_value[1]] = self.swap(
                self.input_array[vp[0]][vp[1]], self.input_array[self.blank_pos_value[0]][self.blank_pos_value[1]])
            valid_puzzles.append(self.input_array.copy())
            self.input_array[vp[0]][vp[1]], self.input_array[self.blank_pos_value[0]][
                self.blank_pos_value[1]] = self.swap(
                self.input_array[vp[0]][vp[1]], self.input_array[self.blank_pos_value[0]][self.blank_pos_value[1]])
        return valid_puzzles

    def main(self):
        list = self.new_test_puzzles()
        arrays = self.efficient_arrays(list)
        return arrays


def get_efficient_list(list_of_arrays):
    perfect_list = False
    diff = list()
    eff_list = list()
    for l in list_of_arrays:
        diff.append(l[len(l) - 1]['difference'])
    diff.sort()
    for l in list_of_arrays:
        if l[len(l) - 1]['difference'] == 0 and diff[0] == 0:
            eff_list.append(l)
            perfect_list = True
            break
        elif l[len(l) - 1]['difference'] == diff[0]:
            eff_list.append(l)
    return eff_list, perfect_list


def puzzle_redirect(list_of_arrays):
    new_list_of_array = list()
    for l in list_of_arrays:
        gsp = get_subsidiary_puzzle(l[len(l) - 1]['array'].copy())
        subsidiary_data = gsp.main()
        for s in subsidiary_data:
            temp_list = l.copy()
            temp_list.append(s)
            new_list_of_array.append(temp_list)
    new_list, complete = get_efficient_list(new_list_of_array)
    if complete:
        return new_list
    else:
        return puzzle_redirect(new_list)


def main_puzzle(input_array):
    list_of_arrays = []
    list_of_arrays.append([{
        'difference': None,
        'array': input_array.copy()
    }])
    return puzzle_redirect(list_of_arrays)


def print_puzzle(array):
    print(first_line)
    for a in range(len(array)):
        for i in array[a]:
            print(bar, i, end=' ')
        print(bar)
        if a == 2:
            print(last_line)
        else:
            print(middle_line)


print('\nINPUT :')
print_puzzle(INIT_PUZ)
print('\nOUTPUT :')
print_puzzle(FINAL_PUZ)
my_list = main_puzzle(INIT_PUZ.copy())
print('\nTOTAL STEPS : ', len(my_list[0]))

print('\nSTEPS :')
for l in range(len(my_list[0])):
    print('\nstep',l+1,' :')
    print_puzzle(my_list[0][l]['array'])
