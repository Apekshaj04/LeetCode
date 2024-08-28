from collections import Counter

class Solution:
    # Function to sort the array according to the frequency of elements.
    def sortByFreq(self, arr):
        # Count the frequency of each element in the array
        freq = Counter(arr)
        
        # Sort elements first by frequency (descending) and then by value (ascending)
        sorted_elements = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        
        # Construct the result list
        result = []
        for element in sorted_elements:
            result.extend([element] * freq[element])
        
        return result

