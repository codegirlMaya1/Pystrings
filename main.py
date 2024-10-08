reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

def capitalize_keywords(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    return review

for review in reviews:
    print(capitalize_keywords(review, keywords))

