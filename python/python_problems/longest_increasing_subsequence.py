"""program for finding the longest increasing sub-sequence"""


sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
length_of_lis = []
lis_of_length = {}


def initialize():
    length = len(sequence)
    while length > 0:
        length_of_lis.append(1)
        length -= 1
    return


def longest_increasing_subsequence():
    initialize()
    lis_of_length[0] = [sequence[0]]
    first_index = 1
    while first_index < len(sequence):
        second_index = 0
        while second_index < first_index:
            if sequence[first_index] > sequence[second_index] and length_of_lis[second_index] + 1 > length_of_lis[first_index]:
                length_of_lis[first_index] = length_of_lis[second_index] + 1
                ref_list = lis_of_length.get(second_index)
                sub_sequence = ()
                if ref_list is not None:
                    sub_sequence = list(ref_list)
                    sub_sequence.append(sequence[first_index])
                lis_of_length[first_index] = sub_sequence
            second_index += 1
        first_index += 1

    print sequence
    print length_of_lis
    print lis_of_length
    return


if __name__ == '__main__':
    longest_increasing_subsequence()
