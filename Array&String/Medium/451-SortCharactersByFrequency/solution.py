def frequencySort(s):
    freq = {}
    sorted_list = []
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    while freq:
        key = max(freq, key=freq.get)
        count = freq.pop(key)
        sorted_list.append(key * count)
        
    return ''.join(sorted_list)


if __name__ == "__main__":
    s = "Aadhaar"

    print(frequencySort(s))