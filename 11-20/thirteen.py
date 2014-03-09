input_file = open("thirteen_input.txt", 'r')
nums = []
for num in input_file.readlines():
	nums.append(int(num))

print sum(nums)