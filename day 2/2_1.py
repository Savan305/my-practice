def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example
text = input("Enter string: ")
print("Palindrome" if is_palindrome(text) else "Not Palindrome")