print(id(34))

# print(id[])

nums1 = [1,2,3]
nums2 = [1,2,3,4]

nums1 = nums2
print(id(nums1))
print(id(nums2)) 

nums2.append(5)

print(id(nums1))
print(id(nums2)) 
    # both still pointing to the same var label
