
'''
#80 删除有序数组中的重复项 II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''
nums = [1,1,1,2,2,3]

count = 0
p1=0
flag=0
n=len(nums)
while p1<n:
    if count > 0 and nums[p1] == nums[count-1] and flag >=2:
        p1 += 1
        flag = 0
    else:
        nums[count] = nums[p1]
        count += 1
        p1 += 1
        flag += 1
print(nums)
print(count)
# nums1 = [1,2,3,3,5,0]
# val = 3
# count = 0
# for item in nums1:
#     if item != val:
#         nums1[count] = item
#         count+=1
# print(nums1)
# print(count)


'''
# 88 合并两个有序数组
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，
其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
'''

#方式二
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# p1=p2=0
# res=[]
# while p1<m or p2<n:
#     if p1 == m:
#         res.append(nums2[p2])
#         p2 += 1
#     elif p2 == n:
#         res.append(nums1[p1])
#         p1 += 1
#     elif nums1[p1] < nums2[p2]:
#         res.append(nums1[p1])
#         p1 += 1
#     else:
#         res.append(nums2[p2])
#         p2 += 1
# nums1=res
# print(nums1)
# print(res)


#方式一
#         for idx in range(m,m+n):
#             nums1[idx]=nums2[idx-m]
#
#         nums1.sort()