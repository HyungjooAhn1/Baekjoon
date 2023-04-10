n = input()
nums = [0 for _ in range(11)]
for i in n:
    if int(i) == 6 or int(i) == 9:
        if nums[6] <= nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[int(i)] += 1
print(max(nums))