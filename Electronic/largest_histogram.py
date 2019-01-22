def largest_histogram(histogram):
    stack = [-1]
    max_area = 0

    for i in range(len(histogram)):
        while stack[-1] != -1 and histogram[stack[-1]] >= histogram[i]:
            last_elem_index = stack.pop()
            max_area = max(max_area, histogram[last_elem_index] * (i - stack[-1] - 1))
        stack.append(i)

    while stack[-1] != -1:
        last_elem_index = stack.pop()
        max_area = max(max_area, histogram[last_elem_index] * (len(histogram) - stack[-1] - 1))

    return max_area


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
