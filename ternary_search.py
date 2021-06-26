def ternary_search(arr_list,num_to_find,left,right):
    if (right >= left):
        mid1 = left + (right - left)//3
        mid2 = mid1 + (right - left)//3
        
        mid1_num = arr_list[mid1]
        mid2_num = arr_list[mid2]

        if mid1_num == num_to_find:
            return mid1

        if mid2_num == num_to_find:
            return mid2

        if mid1_num > num_to_find:
            return ternary_search(arr_list, num_to_find, 1, mid1-1)

        if mid2_num < num_to_find:
            return ternary_search(arr_list,num_to_find, mid2+1, right)

        return ternary_search(arr_list,num_to_find,mid1+1, mid2-1)

    return -1

arr_list = [3,4,10,12,23,34,55,68,73]
num_to_find = 68#int(input("Enter Number You want to find: "))

result = ternary_search(arr_list,num_to_find,1,len(arr_list))
print(f"Index of the element {result}")
'''

# A recursive ternary search function. It returns location of x in
# given array arr[l..r] is present, otherwise -1
def ternarySearch(arr, l, r, x):
	if (r >= l):
		mid1 = l + (r - l)//3
		mid2 = mid1 + (r - l)//3

		# If x is present at the mid1
		if arr[mid1] == x:
			return mid1

		# If x is present at the mid2
		if arr[mid2] == x:
			return mid2

		# If x is present in left one-third
		if arr[mid1] > x:
			return ternarySearch(arr, l, mid1-1, x)

		# If x is present in right one-third
		if arr[mid2] < x:
			return ternarySearch(arr, mid2+1, r, x)

		# If x is present in middle one-third
		return ternarySearch(arr, mid1+1, mid2-1, x)
	
	# We reach here when element is not present in array
	return -1
	
# This code is contributed by ankush_953
	
arr = [1,3,4,6,7,8,9,10,11,15,19,21,23,24,28,30,31,33,35,37,39]
x = 39
print(ternarySearch(arr, 1, len(arr), x))
'''
