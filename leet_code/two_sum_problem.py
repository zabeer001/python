#[1,5,37,8]
#target 45
#result = [2,3]

def two_sum(nums,tar):
    """ print(nums)
    print(tar) 
    """
    num_dic = {}
    for i, num in enumerate(nums):
        complement = tar - num
        if complement in num_dic:
            #print(num_dic,'got here in index ',num_dic[complement],i) 
            return [num_dic[complement],i]
        else:
            num_dic[num] = i

nums = [1,5,37,8]
target = 45
result = two_sum(nums,target)
print(result)