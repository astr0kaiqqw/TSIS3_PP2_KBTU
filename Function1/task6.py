def reverse_words(sentence):
    words = sentence.split()  
    words.reverse()  
    return " ".join(words)  

user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print("Reversed sentence:", result)

