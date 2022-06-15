class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        res = 1
        
        for word in sorted(words, key=len):
            
            dp[word] = 1
            
            for i in range(len(word)):
                
                new_word = word[:i] + word[i+1:]
                
                if new_word in dp:
                    dp[word] = max(dp[word], dp[new_word]+1)
                    
                res = max(res, dp[word])
        
        return res