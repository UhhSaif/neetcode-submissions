class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: no required characters
        if t == "":
            return ""

        # Dictionaries for required and current window frequencies
        countT, window = {}, {}

        # Count required frequency of each character in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Number of satisfied requirements vs total distinct requirements
        have, need = 0, len(countT)

        # Best window indexes and shortest length found
        res, resLen = [-1, -1], float("infinity")

        # Left pointer
        l = 0

        # Expand window using right pointer
        for r in range(len(s)):
            c = s[r]

            # Add current character to window
            window[c] = 1 + window.get(c, 0)

            # Increment have when a required frequency is satisfied
            if c in countT and window[c] == countT[c]:
                have += 1

            # While all requirements are satisfied, shrink the window
            while have == need:

                # Save current window if it's the shortest found
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove leftmost character from window
                window[s[l]] -= 1

                # If a required frequency is no longer met,
                # decrement the number of satisfied requirements
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Shrink window from the left
                l += 1

        # Unpack the saved start and end indexes
        l, r = res

        # Return shortest substring, or empty string if none exists
        return s[l:r + 1] if resLen != float("infinity") else ""