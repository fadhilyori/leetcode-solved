class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)

        return list(counter_t - counter_s)[0]