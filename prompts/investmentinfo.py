def investmentprompt(investment_type):
    return """Give a brief explanation of the following investment types:

Investment: Stock
Explanation: A stock represents a share in the ownership of a company and constitutes a claim on part of the company's assets and earnings.

Investment: Bonds
Explanation: Bonds are fixed income instruments that represent a loan made by an investor to a borrower.

Investment: {}
Explanation:""".format(
        investment_type.capitalize()
    )
