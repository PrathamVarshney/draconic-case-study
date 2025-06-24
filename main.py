from agents.sentiment_agent import sentiment_analysis_agent
from agents.impact_agent import impact_estimation_agent
import json

with open("data/test_articles.json", "r") as f:
    test_articles = json.load(f)

results = []

for article in test_articles:
    sentiment = sentiment_analysis_agent(article)
    impact = impact_estimation_agent(sentiment, article)
    result = {
        "article_id": article["article_id"],
        "sentiment": sentiment,
        "impact": impact
    }
    results.append(result)
    print(f"Article ID: {article['article_id']}")
    print(f"  Sentiment: {sentiment}")
    print(f"  Predicted Market Impact: {impact}\n")
