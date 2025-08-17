class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        result = ""
        value = num
        romans = [ ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                   ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                   ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1) ]

        while value:
            for ent in romans:
                if value >= ent[1]:
                    result += ent[0]
                    value = value % ent[1] + ((value // ent[1] - 1) * ent[1])
                    break

        return result


solution = Solution()

tests = [[3749, 'MMMDCCXLIX'], [58, 'LVIII'], [1994, 'MCMXCIV']]
for test in tests:
    test_result = solution.intToRoman(test[0])
    if test_result != test[1]:
        print(f"FAIL {test_result} != {test[1]}")
    else:
        print(f"PASS {test_result} = {test[1]}")

print(solution.intToRoman(1))
print(solution.intToRoman(3999))