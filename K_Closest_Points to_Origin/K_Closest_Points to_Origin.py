class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minHeap = []
        for x , y in points:
            dis = (x**2 + y**2)**0.5
            minHeap.append([dis,x,y])
        heapq.heapify(minHeap)
        res=[]
        while k > 0:
            dis,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res