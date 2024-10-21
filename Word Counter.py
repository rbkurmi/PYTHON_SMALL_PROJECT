def word_counter():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print(f"Your sentence has {len(words)} words.")

word_counter()
