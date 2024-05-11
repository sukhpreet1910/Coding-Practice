def remove_smallest(numbers):

    if len(numbers) == 0:
        return []
    
    smallest_index = 0
    for i, n in enumerate(numbers):
        if numbers[i] < numbers[smallest_index]:
            smallest_index = i

    
    # for i, n in enumerate(numbers):
    #     if i != index:
    #         new.append(n)

    return numbers[:smallest_index] + numbers[smallest_index + 1:]



print(remove_smallest([5, 3, 1, 1, 1]))