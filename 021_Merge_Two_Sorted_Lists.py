list1 = [1,2,4]
list2 = [1,3,4]


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        newlist = []
        for i in list1:
            for j in list2:
                if j <= i:
                    newlist.append(j)
                    list2.remove(j)
                else:
                    break
            newlist.append(i)
        return newlist
    
sol = Solution()
print(sol.mergeTwoLists(list1, list2))