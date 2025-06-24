def sentiment_analysis_agent(article):
    content = article["headline"].lower() + " " + article["content"].lower()
    if "record" in content or "profit" in content or "growth" in content or "stellar" in content:
        return "positive"
    elif "concern" in content or "warning" in content or "turbulent" in content or "regulatory" in content:
        return "negative"
    else:
        return "neutral"
