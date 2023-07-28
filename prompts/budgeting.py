def budgetingprompt(budget_info):
    income = budget_info["income"]
    rent = budget_info["rent"]
    utilities = budget_info["utilities"]
    groceries = budget_info["groceries"]
    others = budget_info["others"]
    prompt = f"I have a monthly income of {income} with expenses as follows: Rent/Mortgage: {rent}, Utilities: {utilities}, Groceries: {groceries}, and Other Expenses: {others}. Could you help me draft a budget plan?"
    return prompt
