'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

'''
Our lives would be easier without the linear time constraint: we would just sort the array, while filtering out negative numbers, and iterate over the sorted array and return the first number that doesn't match the index. However, sorting takes O(n log n), so we can't use that here.

Clearly we have to use some sort of trick here to get it running in linear time. Since the first missing positive number must be between 1 and len(array) + 1 (why?), we can ignore any negative numbers and numbers bigger than len(array). The basic idea is to use the indices of the array itself to reorder the elements to where they should be. We traverse the array and swap elements between 0 and the length of the array to their value's index. We stay at each index until we find that index's value and keep on swapping.

By the end of this process, all the first positive numbers should be grouped in order at the beginning of the array. We don't care about the others. This only takes O(N) time, since we swap each element at most once.

Then we can iterate through the array and return the index of the first number that doesn't match, just like before.
'''

def missing_pos_int(nums):
    if not nums:
        return 1

    for i, num in enumerate(nums):
        '''
        (i + 1) != nums[i] --> Check if the element is in the correct position. (i+1) is to offset so the first index is 1 
        (since that is the smallest position integer)
        0 < nums[i] <= len(nums) --> Only care about the positive numbers in range.
        '''
        while (i + 1) != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            if nums[i] == nums[v-1]: # if swapping value is same, then the current element is in the correct position.
                break
            nums[i], nums[v-1] = nums[v-1], nums[i]

    for i, num in enumerate(nums, 1):   # enumerate(nums, 1) means start the "counter" at 1 (instead of 0)
        if i != num:
            return i
    return len(nums) + 1

def main():
    print("in: {}, out: {}".format([5,6,7], missing_pos_int([5,6,7])))
    print("in: {}, out: {}".format([3,0,-1,1], missing_pos_int([3,0,-1,1])))

if __name__ == '__main__':
    main()
