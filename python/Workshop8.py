#1
def intersection_nested_lists(list1, list2):
    result = []
    for l2 in list2:
        if isinstance(l2, list):
            intersection = [num for num in list1 if (isinstance(num, list) and num == l2) or num in l2]
        else:
            intersection = [l2] if l2 in list1 else []
        result.append(intersection)
    return result

nums1 = [[1, 2], 0, 1, -1, 2, [3, 4, 5], 6, 7]
nums2 = [[1, 2], [-1, 0], [[1,2]], [[3, 5]], [6]]



#2
def intersection_nested_lists(list1, list2):
    return [[num for num in list1 if (isinstance(num, list) and num == l2) or num in l2] for l2 in list2]

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 28], [1, 5, 8, 18, 15]]



#3
def intersection_nested_lists(list1, list2):
    result = []
    for l2 in list2:
        intersection = [num for num in list1 if num in l2]
        result.append(intersection)
    return result

nums1 = [[1, 2], 0, 1, -1, 2, [3, 4, 5], 6, 7]
nums2 = [[1, 2], [-1, 0], [[1,2]], [[3, 5]], [6]]

print(intersection_nested_lists(nums1, nums2))
