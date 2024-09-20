def three_sum(nums):
    # Sort the array to make it easier to skip duplicates
    nums.sort()
    result = []
    
    # Iterate through the array
    for i in range(len(nums)):
        # Skip duplicate elements to avoid repeating the same triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two-pointer approach
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left and right pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move the pointers
                left += 1
                right -= 1
            
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
triplets = three_sum(nums)