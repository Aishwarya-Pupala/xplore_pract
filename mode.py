import collections
# list of elements to calculate mode
num_list = [21, 133, 199, 133,199,143]

# Print the list
print(num_list)

# calculate the frequency of each item
data = collections.Counter(num_list)
data_list = dict(data)

# Print the items with frequency
print(data_list)

# Find the highest frequency
max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]
if len(mode_val) == len(num_list):
   print("No mode in the list")
else:
   print("The Mode of the list is : " + ', '.join(map(str, mode_val)))