class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []
        #  make number info
        dic = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz",
        }
        length = len(digits)
        arr = []
        def recur(cur,word):
            if cur == length:
                arr.append(word)
                return

            now_word = dic[int(digits[cur])]
            for i in range(len(now_word)):
                word += now_word[i]
                recur(cur + 1,word)
                word = word[:-1]
        recur(0,"")
        return arr