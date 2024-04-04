import timeit

# Define the setup
setup = """
import math
str1 = 'ABCABC'
str2 = 'ABC'
"""

# Define the statement
statement = """
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        return str1[:math.gcd(len(str1), len(str2))]

sol = Solution()
sol.gcdOfStrings(str1, str2)
"""

# Time the statement
time = timeit.timeit(setup=setup, stmt=statement, number=10000)

print(f"Execution time for 10000 runs: {time} seconds")