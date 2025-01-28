def is_palindrome(s):
    cleaned_s = ''.join(s.split()).lower()

    return cleaned_s == cleaned_s[::-1]

word_or_phrase = input("Enter a word or phrase: ")
if is_palindrome(word_or_phrase):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
