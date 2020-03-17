import numpy as np

INIT_PUZ = np.array(
    [
        [1, 2, 6],
        [4, 5, 3],
        [7, 8, 0]
    ]
)
ARRAY_SHAPE = INIT_PUZ.shape
FINAL_PUZ = np.array(
    [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
    ]
)

class get_subsidurry_puzzle:

    def __init__(self, input_array, previous_blank_pos=None):
        self.input_array = input_array
        self.blank_pos_value = self.blank_pos_func()
        self.previous_blank_pos = previous_blank_pos
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
        if self.previous_blank_pos != None:
            valid_direction_pos.pop(valid_direction_pos.index(self.previous_blank_pos))
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
            if self.difference_count(l) == 0:
                return l
            arrays.append({
                "difference": self.difference_count(l),
                "array": l,
                "blank_pos": self.blank_pos_value
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

gsp = get_subsidurry_puzzle(INIT_PUZ.copy())
print(gsp.main())
