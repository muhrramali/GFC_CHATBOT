# GFC Financial Chatbot – Documentation

## Overview
This is a simplified rule-based AI chatbot prototype built for the GFC project.  
It answers a small set of predefined financial questions about Microsoft, Tesla and Apple using data extracted and analysed from their Form 10-K filings (fiscal years 2023–2025).

## How it works
The chatbot uses classic **if-else rule-based logic**:

```python
def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "..."
    elif user_query == "How has net income changed over the last year?":
        return "..."
    # ... more conditions
    else:
        return "Sorry, I can only provide information on predefined queries."
```

- User input is normalized (lower-cased, stripped).
- Exact (or near-exact) matches trigger the corresponding canned response.
- Any unrecognized query receives a polite fallback message that lists the supported questions.

## Predefined queries the chatbot can answer

| # | Query | What the response contains |
|---|-------|----------------------------|
| 1 | What is the total revenue? | FY 2025 revenue for Microsoft, Apple and Tesla |
| 2 | How has net income changed over the last year? | YoY net-income change (2024 → 2025) for all three companies |
| 3 | What is the operating cash flow? | FY 2025 operating cash flow comparison |
| 4 | Which company performed best? | High-level performance ranking and rationale |
| 5 | Give me key insights | Summary of the main trends from the Task-1 analysis |

## Data source
All numbers come from the Task-1 extraction of SEC 10-K filings:

- Microsoft, Tesla, Apple  
- Metrics: Total Revenue, Net Income, Operating Cash Flow (and supporting context)  
- Period: Fiscal years 2023, 2024, 2025

## How to run
```bash
python simple_financial_chatbot.py
```
Then type any of the predefined queries above. Type `quit` to exit.

## Limitations
- Only the five predefined queries (and a few close variants) are recognized.
- Free-form or complex questions (e.g. “Compare Microsoft’s 2023 assets with Tesla’s”) are not supported.
- No natural-language understanding beyond simple string matching.
- No memory / conversation state across turns.
- Data is static (loaded from the earlier analysis); it does not refresh automatically.

These limitations are intentional: the prototype focuses on demonstrating rule-based logic, which is the foundation for the more advanced NLP and machine-learning components being developed by other team members.

## Role in the larger project
This rule-based layer gives the chatbot its first reliable “understanding” of common financial questions.  
NLP specialists, ML engineers, data-integration specialists and UX designers will later extend the system so it can handle freer language, learn from interactions, access live data and present insights through a polished interface.
