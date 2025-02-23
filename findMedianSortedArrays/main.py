def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        duparry = nums1[:]
        duparry.extend(nums2)
        duparry.sort()
        len1 = len(duparry)
        mid = len1 // 2
        if (len1 % 2 == 0):
            return(duparry[mid - 1] + duparry[mid]) / 2
        else:
            return(duparry[mid])