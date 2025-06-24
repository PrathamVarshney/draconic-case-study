def evaluate_system(predictions):
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
    impact_counts = {}

    for p in predictions:
        sentiment_counts[p['sentiment']] += 1
        impact_counts[p['impact']] = impact_counts.get(p['impact'], 0) + 1

    print("Sentiment Distribution:", sentiment_counts)
    print("Impact Distribution:", impact_counts)
