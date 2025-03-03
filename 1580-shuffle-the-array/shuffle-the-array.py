class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mylist1 = nums[:n]
        mylist2 = nums[n:]
        new_list = []
        print(mylist1)
        print(mylist2)
        for i in range(len(mylist1)):
            new_list.append(mylist1[i])
            new_list.append(mylist2[i])

        return new_list