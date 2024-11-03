class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50,
            'C': 100, 
            'D': 500, 
            'M': 1000
        }

        total=0
        n=len(s)

        for i in range(n):
            val = roman_to_int[s[i]]

            # if there is next index and the next index is greater, substract current val from total
            if i<n-1 and val < roman_to_int[s[i+1]]:
                total-=val
            # if its the last elem, or the next elem is smaller, add current val to total
            else:
                total+=val
        return total