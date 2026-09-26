"""
GFC Financial Chatbot - Simplified Prototype
Rule-based chatbot using if-else logic for predefined financial queries.
Data source: Microsoft, Tesla & Apple 10-K analysis (FY 2023-2025).
"""

def simple_chatbot(user_query):
    """
    Match user input against predefined queries and return a canned response.
    All figures are in millions of USD unless otherwise stated.
    """
    # Normalize input for more flexible matching
    query = user_query.strip().lower()

    # ----- Predefined Query 1: Total Revenue -----
    if query in [
        "what is the total revenue?",
        "what is the total revenue",
        "total revenue",
        "show total revenue",
    ]:
        return (
            "Total Revenue (FY 2025):\n"
            "  • Microsoft: $281.7 billion\n"
            "  • Apple:     $416.2 billion\n"
            "  • Tesla:     $94.8 billion\n"
            "Apple has the highest total revenue among the three companies."
        )

    # ----- Predefined Query 2: Net Income Change -----
    elif query in [
        "how has net income changed over the last year?",
        "how has net income changed over the last year",
        "net income change",
        "net income growth",
    ]:
        return (
            "Net Income change from FY 2024 to FY 2025:\n"
            "  • Microsoft: increased by 15.5%  ($88.1 B → $101.8 B)\n"
            "  • Apple:     increased by 19.5%  ($93.7 B → $112.0 B)\n"
            "  • Tesla:     decreased by 46.1%  ($7.2 B → $3.9 B)\n"
            "Microsoft and Apple both grew profits; Tesla's net income declined."
        )

    # ----- Predefined Query 3: Operating Cash Flow -----
    elif query in [
        "what is the operating cash flow?",
        "what is the operating cash flow",
        "operating cash flow",
        "show cash flow",
    ]:
        return (
            "Operating Cash Flow (FY 2025):\n"
            "  • Microsoft: $136.2 billion\n"
            "  • Apple:     $111.5 billion\n"
            "  • Tesla:     $14.7 billion\n"
            "Microsoft generated the strongest operating cash flow."
        )

    # ----- Predefined Query 4: Company Comparison / Best Performer -----
    elif query in [
        "which company performed best?",
        "which company performed best",
        "best performing company",
        "who performed best",
    ]:
        return (
            "Based on the 2023–2025 analysis:\n"
            "  • Microsoft shows the strongest revenue growth (~15% YoY) driven by cloud & AI.\n"
            "  • Apple remains the highest-quality cash generator with superior profit margins.\n"
            "  • Tesla is in a transition phase (flat revenue, lower net income) but cash flow is still resilient.\n"
            "Overall, Microsoft currently demonstrates the clearest growth trajectory."
        )

    # ----- Predefined Query 5: Key Insights Summary -----
    elif query in [
        "give me key insights",
        "key insights",
        "summary",
        "financial summary",
    ]:
        return (
            "Key insights from the 10-K analysis (FY 2023–2025):\n"
            "1. Microsoft – Steady ~15% revenue growth, strong AI/cloud momentum, robust cash flow.\n"
            "2. Apple – Modest top-line growth, very high margins, consistent $110 B+ operating cash flow.\n"
            "3. Tesla – Revenue essentially flat; net income under pressure; energy storage is a bright spot.\n"
            "All three companies generate substantial operating cash flow, supporting continued investment."
        )

    # ----- Fallback -----
    else:
        return (
            "Sorry, I can only provide information on predefined queries.\n"
            "Try one of these:\n"
            "  • What is the total revenue?\n"
            "  • How has net income changed over the last year?\n"
            "  • What is the operating cash flow?\n"
            "  • Which company performed best?\n"
            "  • Give me key insights"
        )


# ---------------------------------------------------------------------------
# Interactive demo loop
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 58)
    print("  GFC Financial Chatbot (Simplified Prototype)")
    print("  Microsoft · Tesla · Apple | FY 2023–2025")
    print("=" * 58)
    print("Type a predefined query (or 'quit' to exit).\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            print("\nBot: Input stream closed. Exiting gracefully.")
            break
        except KeyboardInterrupt:
            print("\nBot: Interrupted. Goodbye!")
            break

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Thank you for using the GFC Financial Chatbot. Goodbye!")
            break
        if not user_input:
            continue
        response = simple_chatbot(user_input)
        print(f"Bot: {response}\n")
