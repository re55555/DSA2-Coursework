def findMostFrequentWord(inputList1: list[str], inputList2: list[str]) -> str:

    import re

    #I want to ensure all the words are in lower case when considered
    text1 = " ".join(inputList1).lower()
    text2 = " ".join(inputList2).lower()

    #make sure to include only text
    a1 = re.findall(r"[a-zA-Z']+", text1)
    a2 = re.findall(r"[a-zA-Z']+", text2)

    # Remove words that exist in a2 from a1
    filtered = []
    for word in a1:
        if word not in a2:
            filtered.append(word)
            
    # If there are no valid words, return empty string to avoid crashing
    if len(filtered) == 0:
        return ""

    # Count how frequently words occur in the new list
    counts = {}
    for word in filtered:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # find out the last position of every repeated word 
    last_index = {}
    for i, word in enumerate(a1):
        if word in counts:
            last_index[word] = i

    # Sort by frequency then last occurrence
    ranked = sorted(
        counts.keys(),
        key=lambda w: (counts[w], last_index[w]),
        reverse=True
    )

    #Find the highest number of times a word appears
    highest_frequency = counts[ranked[0]]

    #Remove all the highest ranking word(s) to find the 2nd highest
    second_ranked = []
    for word in ranked:
        if counts[word] < highest_frequency:
            second_ranked.append(word)

    #If there is no 2nd most frequent word, return empty
    if len(second_ranked) == 0:
        return ""

    return second_ranked[0]




  
