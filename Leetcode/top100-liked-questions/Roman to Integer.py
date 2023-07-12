class Solution:
    def romanToInt(self, s: str) -> int:
        dir = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }   # infomation about romain
        min_number = 2000 # 이전에 나온 숫자에 대해서 기록해둠
        # 같으면 더하고, 이전숫자보다 크면 빼주면됨
        answer = 0
        for sp in s:
            if min_number < dir[sp]:
                answer += dir[sp] - 2*min_number
            else:
                answer += dir[sp]
            min_number = dir[sp]    

        return answer