def findMostFrequentWordInText(text: str) -> str:
    import re

    #Take out the excluded words stated in the question
    excluded = ["a", "the", "in", "of", "and", "to", "be", "is"]
    
    # Convert the string into a list of only lowercase words  
    text = text.lower()
    words = re.findall(r"[a-zA-Z']+", text)

    # Remove excluded words defined in the beginning 
    filtered = []
    for word in words:
        if word not in excluded:
            filtered.append(word)
    # If there are no valid words, return an empty string
    if len(filtered) == 0:
        return ""

    # Count how frequently the words occur
    counts = {}
    for word in filtered:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # Find the most frequent word
    most_frequent_word = ""
    highest_count = 0

    for word in counts:
        if counts[word] > highest_count:
            highest_count = counts[word]
            most_frequent_word = word

    return most_frequent_word


