def is_palindrome(s):
    # Remove non-alph
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]


print(is_palindrome("madam"))          
print(is_palindrome("hello"))