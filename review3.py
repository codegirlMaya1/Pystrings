reviews = [
    "this product is really good. i'm impressed with its quality.",
    "the performance of this product is excellent. highly recommended!",
    "i had a bad experience with this product. it didn't meet my expectations.",
    "poor quality product. wouldn't recommend it to anyone.",
    "the product was average. nothing extraordinary about it."
]

def summarize_review(review, length=30):
    if len(review) <= length:
        return review
    end = length
    while end > 0 and review[end] != ' ':
        end -= 1
    return review[:end]

def append_compliment(summary, index):
    compliments = [
        "This product is really good!",
        "You won't be disappointed with this purchase.",
        "A great choice for anyone looking for quality.",
        "Definitely worth the investment.",
        "An excellent addition to your collection."
    ]
    return summary + "… " + compliments[index]

summaries = [summarize_review(review) for review in reviews]
summaries_with_compliments = [append_compliment(summary, i) for i, summary in enumerate(summaries)]

for review, summary in zip(reviews, summaries_with_compliments):
    print(f"First 30 characters: {review[:30]}")
    print(f"Appended sentence: {summary}")
    print()  # For better readability