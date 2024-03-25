#Fahad Shafiq
#100831055

def sort_merge(data, depth=0):
    # If the list contains a single element, return it as is
    if len(data) <= 1:
        return data

    # Split the list into two halves and apply sort_merge recursively
    middle = len(data) // 2
    left_part = sort_merge(data[:middle], depth + 1)
    right_part = sort_merge(data[middle:], depth + 1)

    # Combine the two sorted halves together
    combined = combine(left_part, right_part, depth)

    # If this is the initial call, output the sorted array
    if depth == 0:
        print(f"Final sorted array: {combined}")
    return combined

def combine(left, right, depth):
    combined_list = []
    index_left = index_right = 0

    # Output the current merging process
    print(f"{'  '*depth}Combining {left} with {right}")

    # Merge the two halves by comparing their elements
    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            combined_list.append(left[index_left])
            index_left += 1
        else:
            combined_list.append(right[index_right])
            index_right += 1

    # Add the remaining elements from either left or right
    combined_list.extend(left[index_left:])
    combined_list.extend(right[index_right:])

    # Display the combined list after merging
    print(f"{'  '*depth}Combined result: {combined_list}")
    return combined_list

sample_data = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Initial array:", sample_data)
sort_merge(sample_data)
