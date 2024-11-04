class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Explanation and Intuition:
        This function merges two strings, `word1` and `word2`, by adding characters in an alternating order.
        - We use two pointers, `i` and `j`, to keep track of the current position in each string.
        - In each iteration, we add one character from `word1` (if available) and one character from `word2` (if available).
        - If one string is longer, the remaining characters of the longer string are added at the end.

        This approach ensures we merge the strings in alternating order efficiently.
        """

        result = ""  # Initialize the result string
        i, j = 0, 0  # Pointers for word1 and word2

        # Loop until we've processed all characters in both strings
        while i < len(word1) or j < len(word2):

            # Add the next character from word1 if available
            if i < len(word1):
                result += word1[i]
                i += 1

            # Add the next character from word2 if available
            if j < len(word2):
                result += word2[j]
                j += 1
                
        return result
