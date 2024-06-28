class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        result = []
        max_candies = max(candies)
      #  print(max_candies)
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
candies = [2,1,4,5,6]
extraCandies = 3
Solution = Solution()
result = Solution.kidsWithCandies(candies,extraCandies)
print(result)