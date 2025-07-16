import pandas as pd
from textblob import TextBlob
import os

def analyze_sentiment(text):
    """Analyze sentiment of a given text and return sentiment category and polarity."""
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
        if polarity > 0:
            return "Positive", polarity
        elif polarity < 0:
            return "Negative", polarity
        else:
            return "Neutral", polarity
    except Exception as e:
        return "Error", None

def main():
    # Sample data: create a text file with reviews if it doesn't exist
    sample_reviews = [
        "I absolutely love this product! It's amazing and works perfectly.",
        "This is the worst experience I've ever had. Terrible service!",
        "The item is okay, nothing special but it gets the job done.",
        "Fantastic quality, highly recommend to everyone!",
        "Disappointed with the delivery time, but the product is fine."
    ]
    
    # Write sample reviews to a file
    input_file = "reviews.txt"
    with open(input_file, "w", encoding="utf-8") as f:
        for review in sample_reviews:
            f.write(review + "\n")
    
    # Read reviews from file
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            reviews = f.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return
    
    # Process reviews and store results
    results = []
    for idx, review in enumerate(reviews, 1):
        review = review.strip()
        if review:
            sentiment, polarity = analyze_sentiment(review)
            results.append({
                "Review Number": idx,
                "Review Text": review,
                "Sentiment": sentiment,
                "Polarity Score": polarity
            })
    
    # Create a DataFrame for nice output
    df = pd.DataFrame(results)
    
    # Display results
    print("\nSentiment Analysis Results:")
    print(df.to_string(index=False))
    
    # Save results to a CSV file
    output_file = "sentiment_results.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"\nResults saved to {output_file}")
    
    # Summary statistics
    print("\nSummary:")
    print(f"Total Reviews: {len(reviews)}")
    print(f"Positive Reviews: {len(df[df['Sentiment'] == 'Positive'])}")
    print(f"Negative Reviews: {len(df[df['Sentiment'] == 'Negative'])}")
    print(f"Neutral Reviews: {len(df[df['Sentiment'] == 'Neutral'])}")
    print(f"Average Polarity: {df['Polarity Score'].mean():.2f}")

if __name__ == "__main__":
    main()
