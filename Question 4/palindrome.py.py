def isPalindrome(word: str) -> bool:
    #I want to ensure letters are considered the same so will change all inputs to lowercase
    word = word.lower()
    
    # First step, empty string or 1 character string are palindromes
    if len(word) <= 1:
        return True
    #if the first and last characters don't match, it is not a palindrome
    if word[0] != word[-1]:
        return False
    # Now to check the inside characters recursively
    return isPalindrome(word[1:-1])
