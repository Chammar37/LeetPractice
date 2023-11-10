class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n = len(nums)
        self.k = k
        self.heap = nums
        heapify(self.heap)
        # print(self.heap)
        
        #We drop everything else so we can grab the Kth largest element in the minheap in O(1) time
        for i in range(self.k, self.n, 1):
            heappop(self.heap)

    def add(self, val: int) -> int:
        # print(self.heap)
        heappush(self.heap, val)
        # print(self.heap)
        if len(self.heap) > self.k:
            heappop(self.heap)

        # elif(val > self.heap[0]): #if its greater than current kth largest, we need to consider it, if its less than current list , we dont care
        #     heappush(self.heap, val)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)