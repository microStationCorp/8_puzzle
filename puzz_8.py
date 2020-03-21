import numpy as np

INIT_PUZ = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
)
ARRAY_SHAPE = INIT_PUZ.shape
FINAL_PUZ = np.array(
    [
        [1, 0, 3],
        [4, 2, 5],
        [7, 8, 6]
    ]
)


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


my_list = main_puzzle(INIT_PUZ.copy())

print('input:\n',INIT_PUZ,'\n')
print('output:\n',FINAL_PUZ,'\n')

for l in my_list:
    for i in l:
        print(i['array'])
        print()