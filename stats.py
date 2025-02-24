def word_counter(text):
    num_words = 0
    
    for word in text.split():
        num_words += 1
    
    print(f"{num_words} words found in the document")

def letter_counter(text):
    text_sanitized = text.lower()
    letter_dict = {}

    for i in range(0, len(text_sanitized)):
        if text_sanitized[i] not in letter_dict:
            letter_dict[text_sanitized[i]] = 1
            #print(letter_dict[i])
        else:
            letter_dict[text_sanitized[i]] += 1
    return letter_dict