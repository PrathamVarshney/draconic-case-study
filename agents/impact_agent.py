def impact_estimation_agent(sentiment, article):
    if sentiment == "positive":
        return "strong_positive_impact"
    elif sentiment == "negative":
        return "strong_negative_impact"
    else:
        return "minimal_impact"
