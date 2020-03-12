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


def blank_pos(input_array):
    for i in range(len(input_array)):
        for k in range(len(input_array[i])):
            if input_array[i][k] == 0:
                return (i, k)


def valid_direction(blank_pos, previous_blank_pos=None):
    valid_direction_pos = []
    if blank_pos[0] + 1 < ARRAY_SHAPE[0]:
        valid_direction_pos.append([blank_pos[0] + 1, blank_pos[1]])
    if blank_pos[0] - 1 >= 0:
        valid_direction_pos.append([blank_pos[0] - 1, blank_pos[1]])
    if blank_pos[1] + 1 < ARRAY_SHAPE[1]:
        valid_direction_pos.append([blank_pos[0], blank_pos[1] + 1])
    if blank_pos[1] - 1 >= 0:
        valid_direction_pos.append([blank_pos[0], blank_pos[1] - 1])
    if previous_blank_pos != None:
        valid_direction_pos.pop(valid_direction_pos.index(previous_blank_pos))
    return valid_direction_pos


def swap(input1, input2):
    temp = input1
    input1 = input2
    input2 = temp
    return input1, input2


def new_test_puzzles(input_array, valid_direction_pos, blank_pos):
    valid_puzzles = []
    for vp in valid_direction_pos:
        input_array[vp[0]][vp[1]], input_array[blank_pos[0]][blank_pos[1]] = swap(input_array[vp[0]][vp[1]],
                                                                                  input_array[blank_pos[0]][
                                                                                      blank_pos[1]])
        valid_puzzles.append(input_array.copy())
        input_array[vp[0]][vp[1]], input_array[blank_pos[0]][blank_pos[1]] = swap(input_array[vp[0]][vp[1]],
                                                                                  input_array[blank_pos[0]][
                                                                                      blank_pos[1]])
    return valid_puzzles


def difference_count(input_array):
    b = FINAL_PUZ != input_array
    return len(input_array[b])


def efficient_arrays(list_of_arrays):
    arrays = []
    for l in list_of_arrays:
        if difference_count(l) == 0:
            return l
        arrays.append({
            "difference": difference_count(l),
            "array": l
        })
    arrays = sorted(arrays, key=lambda i: i['difference'])
    eff_arrays = []
    for a in arrays:
        if a['difference'] == arrays[0]['difference']:
            eff_arrays.append(a)
    return eff_arrays


def main(input_array):
    list = new_test_puzzles(input_array.copy(), valid_direction(blank_pos(input_array)), blank_pos(input_array))
    arrays = efficient_arrays(list)
    return arrays


print(main(INIT_PUZ.copy()))
print('sujan')