class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} #dictonary
        freq=[[] for i in range(len(nums)+1)]#frequency list of list to store the string of numbers under the same frequency
        
        for n in nums:#intitalize the hashmap, fill in the values
            count[n]= 1+ count.get(n,0)#if the element does not exist make it exist
        for n,c in count.items():#iterate through the hash map and push the frequency as keys and the numbers as list of values
            freq[c].append(n)

        res=[]#create a result list
        for i in range(len(freq)-1,0,-1):#iterating the buckets from the n to 0
            for n in freq[i]:#iterating the bucket list
                res.append(n)#pushing the elements in the result list
                if len(res)==k:#if k elements are reached we return the result
                    return (res)