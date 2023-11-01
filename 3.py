# Write your solution for algorithm 3 below
def sort_descending(unsorted_list):
    sorted_list = sorted(unsorted_list)
    sorted_list.reverse()
    return sorted_list


if __name__ == "__main__":
    print(sort_descending([5, 4, 1, 3, 2, 6]))