import pandas as pd
import random
import os

# Set random seed
random.seed(42)

# Products and phrases
products = [
    "phone", "laptop", "headphones", "book", "tablet", "camera", "watch",
    "speaker", "keyboard", "mouse", "backpack", "shoes", "jacket", "cookware",
    "vacuum", "TV", "monitor", "printer", "smartwatch", "earbuds"
]
qualities = ["high", "excellent", "decent", "poor", "amazing", "subpar", "fantastic", "terrible"]
features = ["battery life", "screen quality", "sound", "durability", "design", "performance", "comfort", "usability"]
adjectives = ["great", "awesome", "disappointing", "average", "wonderful", "frustrating", "reliable", "flimsy"]
seller_terms = ["fast delivery", "supportive seller", "neat packaging", "kind communication", "helpful responses"]

# Templates
positive_templates = [
    "This {product} is {adjective}! The {feature} is {quality}.",
    "Absolutely love my new {product}. Works perfectly.",
    "Highly recommend this {product}! Great {feature}.",
    "Fantastic {product} with {quality} {feature}.",
    "Super impressed! {feature} of the {product} is top-notch."
]
negative_templates = [
    "This {product} is {adjective}. The {feature} is {quality}.",
    "Extremely disappointed with this {product}.",
    "Broke within days. {feature} is just {quality}.",
    "Worst {product} I've ever owned.",
    "Terrible experience. Avoid this {product}."
]
neutral_templates = [
    "The {product} is okay. {feature} is {quality}.",
    "It’s decent for the price. Nothing amazing though.",
    "Works fine, but {feature} could be better.",
    "The {product} meets basic expectations.",
    "An average {product}, does what it says."
]
friendly_templates = [
    "Thanks for the {seller_term} with this {product}!",
    "Seller was {adjective}. Loved the service for this {product}.",
    "Really appreciated the {seller_term}.",
    "Smooth shopping experience. Seller was {adjective}.",
    "Loved the packaging and how {seller_term} was handled."
]
critical_templates = [
    "The {product} could improve its {feature}.",
    "Needs better {feature}, otherwise okay.",
    "Not very {adjective}, especially the {feature}.",
    "This {product} lacks good {feature}.",
    "Could be improved — {feature} needs work."
]

# Generate reviews
def generate_reviews(sentiment, num_reviews, templates):
    reviews = []
    for _ in range(num_reviews):
        template = random.choice(templates)
        review = template.format(
            product=random.choice(products),
            feature=random.choice(features),
            quality=random.choice(qualities),
            adjective=random.choice(adjectives),
            seller_term=random.choice(seller_terms)
        )
        reviews.append({"reviewText": review, "Sentiment": sentiment})
    return reviews

# Set number per class
num_per_class = 2000

sentiments = {
    "Positive": positive_templates,
    "Negative": negative_templates,
    "Neutral": neutral_templates,
    "Friendly": friendly_templates,
    "Critical": critical_templates
}

all_reviews = []
for sentiment, templates in sentiments.items():
    all_reviews.extend(generate_reviews(sentiment, num_per_class, templates))

# Shuffle, deduplicate
random.shuffle(all_reviews)
df = pd.DataFrame(all_reviews).drop_duplicates(subset=["reviewText"])
print(f"Generated {len(df)} unique reviews.")

# Save to /data/
output_dir = "C:/Users/Intel/PycharmProjects/Sentiment Analysis/data"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "product_reviews.csv")
df.to_csv(output_path, index=False)
print(f"Dataset saved to: {output_path}")
