class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # left and right of our rates with min being 1 n max being largest num in piles
        l , r = 1, max(piles)
        # track result of min rate
        res = r

        # binary search
        while l <= r:
            # get mid rate
            k = (l + r) // 2
            # see how long it takes to eat all piles at k rate
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            # If rate k finishes within h hours, save it and try slower rates
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                # going too slow speed up
                l = k + 1
        return res
            