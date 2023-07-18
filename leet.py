# Given a sorted array of distinct integers and a target value, return the index if the target is found.If not, return the
# index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1

nums = [1, 3, 5, 6, 8, 9, 10, 192]
def search_index(target):
    for i, num in enumerate(nums):
        if num >= target:
            return i

    return len(nums)

print(search_index(97))

# Given dictionary - LinkedIn ex:
my_dict = {
    "key1": [1, 2, 3],
    "key2": [4, 5, 6],
    "key3": "hello",
    "key4": [7, 8, 9, 10]
}

# Threshold value
threshold = 14

# Initialize an empty dictionary to store the filtered key-value pairs
new_dict = {}

# Iterate through the items (key-value pairs) of the given dictionary
for key, value in my_dict.items():
    # Check if the value is a list and all elements in the list are integers
    if isinstance(value, list) and all(isinstance(x, int) for x in value):
        # Calculate the sum of the elements in the list
        sum_of_list = sum(value)
        # Check if the sum is greater than the threshold
        if sum_of_list > threshold:
            # Add the key-value pair to the new dictionary
            new_dict[key] = value

# Print the new dictionary
print(new_dict)
