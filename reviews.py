#SECTION TWO.....
def tally_sentiments(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    
    for review in reviews:
        words = review.lower().split()
        for word in words:
            # Remove punctuation from the word
            word = word.strip(".,!?")
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
    
    return positive_count, negative_count

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
reviews = [
    "this product is really good i'm impressed with its quality",
    "the performance of this product is excellent highly recommended!",
    "i had a bad experience with this product it didn't meet my expectations",
    "poor quality product wouldn't recommend it to anyone",
    "the product was average nothing extraordinary about it"
]

positive_count, negative_count = tally_sentiments(reviews, positive_words, negative_words)
print(f"Total Positive Words: {positive_count}")
print(f"Total Negative Words: {negative_count}")