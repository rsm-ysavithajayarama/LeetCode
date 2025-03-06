class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        listofnum = [ num for sublist in grid for num in sublist ] 
        listofall = [num for num in range(1,len(listofnum)+1)]
        mylist = []

        
        
        mydict = Counter(listofnum)
        new = [k for k,v in mydict.items() if v > 1]

        for i in listofall:
            if i not in listofnum:
                mylist.append(i)

        return new + mylist
