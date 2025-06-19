crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

def chatbot_response(user_query):
    query = user_query.lower()

    if "sustainable" in query or "eco" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f" Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    elif "trending" in query or "rising" in query:
        rising = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"Coins trending up: {', '.join(rising)}."

    elif "long-term" in query or "should i buy" in query or "growth" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high" and data["sustainability_score"] > 7/10:
                return f"{coin} is a strong pick — profitable *and* sustainable for long-term growth!"
        return "No perfect match for long-term and green right now. Try checking back later!"

    elif "bitcoin" in query:
        return "Bitcoin is powerful and rising, but it’s energy-hungry. Consider greener options for sustainability."

    elif "ethereum" in query:
        return "Ethereum is stable with decent sustainability. It’s a solid choice for steady investors."

    elif "cardano" in query:
        return "Cardano is rising, energy-efficient, and has one of the best sustainability scores!"

    else:
        return "I didn’t catch that. You can ask me things like:\n- 'Which crypto is trending up?'\n- 'What’s the most sustainable coin?'\n- 'Should I buy Bitcoin?'"


def crypto_buddy():
    print(" Hey there! I’m CryptoBuddy – your AI sidekick for smart crypto investing.")
    print(" Ask me about crypto trends, green coins, or long-term picks.")
    print(" Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("CryptoBuddy: 🏁 Goodbye for now! Remember: Crypto is risky – always DYOR (Do Your Own Research)!")
            break
        response = chatbot_response(user_input)
        print(f"CryptoBuddy: {response}\n")

crypto_buddy()
  
   