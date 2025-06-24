# System Architecture: Multi-Agent Financial News Analyzer

## Why Multi-Agent?
- Agent 1: Analyzes **sentiment** of the news (positive/negative/neutral).
- Agent 2: Estimates **market impact** based on sentiment.

## Design Decisions
- Used heuristic keyword-based sentiment for speed.
- Simple if-else logic for impact estimation.
- Could be upgraded to OpenAI/LLM agents for smarter insights.

## Flow
1. Load article.
2. Sentiment agent processes content.
3. Impact agent receives sentiment, outputs likely market impact.

## Prompt Iteration Plan
1. Heuristic keywords
2. Enhanced rule set
3. Optional LLM agent (if enabled via API)

## Interesting Behaviors
- Mixed messages like “record profits but turbulent times” → marked as negative due to risk.
- Small-cap approvals trigger positive signals even with skeptical tone.
