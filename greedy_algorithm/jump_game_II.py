def jump(nums) -> int:
    i,curr,length,next = 0,-1, len(nums) - 1, -1
    ans = 0
    while next < length:
        if i > curr:
            ans += 1
            curr = next
        next = max(next, i + nums[i])
        i+=1
    return ans

# nums = [2,3,1,1,4] #ok
# nums = [2,3,0,1,4] #ok
nums = [0]
nums = [3,2,1]
print(jump(nums))