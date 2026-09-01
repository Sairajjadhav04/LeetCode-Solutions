class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
        total = sum(target)
        while True:
            largest = -heapq.heappop(max_heap)
            remaining = total - largest
            if largest == 1 or remaining == 1:
                return True
            if remaining == 0 or remaining >= largest:
                return False
            previous = largest % remaining
            if previous == 0:
                return False
            total = remaining + previous
            heapq.heappush(max_heap, -previous)
        