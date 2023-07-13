class Solution(object):
    def longestCommonPrefix(self, strs):
        # 접두사니까
        strs.sort(key = lambda x : len(x))
        length = len(strs[0])
        answer = ""
        for i in range(len(strs[0])):
            word = strs[0][i]
            flag = True
            for c in strs:
                if c[i] == word:
                    continue
                else:
                    flag = False
            if flag:
                answer += word
            else:
                break
        return answer