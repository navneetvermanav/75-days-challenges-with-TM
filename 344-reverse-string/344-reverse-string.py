class Solution(object):
    def reverseString(self, s):
        start, end = 0, len(s)-1
        while start < end :
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1