class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_s = {}
        letters_t = {}
        for index in range(len(s)):
            s_val = s[index]
            t_val = t[index]

            if s_val not in letters_s:
                letters_s[s_val] = 0
            
            if t_val not in letters_t:
                letters_t[t_val] = 0

            letters_s[s_val] += 1
            letters_t[t_val] += 1

        for key, val in letters_s.items():
            if letters_t.get(key, 0) != val:
                return False
        
        return True
            