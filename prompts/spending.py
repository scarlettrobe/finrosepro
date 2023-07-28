def spendingprompt(spending_info):
    food = spending_info["food"]
    entertainment = spending_info["entertainment"]
    transportation = spending_info["transportation"]
    others = spending_info["others"]
    prompt = f"My monthly spending is as follows: Food: {food}, Entertainment: {entertainment}, Transportation: {transportation}, and Others: {others}. Could you provide some insights and advice on my spending habits?"
    return prompt
