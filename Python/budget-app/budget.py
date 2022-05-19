class Category:
    def __init__(self, category: str):
        self._category = category
        self.ledger = []
        self.spent = []

    def deposit(self, amount: float, description: str = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.spent.append(amount)
            return True
        else:
            return False

    def get_balance(self):
        values = [key['amount'] for key in self.ledger]
        balance = sum([float(value) for value in values])
        return balance

    def transfer(self, amount: float, another_category):
        if self.check_funds(amount):
            self.withdraw(amount, description=f"Transfer to {another_category._category}")
            another_category.deposit(amount, description=f"Transfer from {self._category}")
            return True
        else:
            return False

    def check_funds(self, amount: float) -> bool:
        balance = self.get_balance()
        return amount <= balance

    def __repr__(self):
        amounts, descriptions, rows = [], [], []
        for item in self.ledger:
            # amounts.append(str(round(item['amount'], 2))[:7])
            str(item['amount'])
            # amounts.append(str(item['amount'])[:7])
            amount = item['amount']
            amounts.append("{:4.2f}".format(amount))
            descriptions.append(item['description'][:23])

        for item in list(zip(descriptions, amounts)):
            rows.append(list(item))

        string = f'{self._category:*^30}\n'
        for row in rows:
            spaces_in_description = 23 - len(row[0])
            row[0] = f"{row[0]}{spaces_in_description * ' '}"

            spaces_in_amount = 7 - len(str(row[1]))
            row[1] = f"{spaces_in_amount * ' '}{row[1]}"

            string += f"{row[0]}{row[1]:>5}\n"

        string += f'Total: {self.get_balance()}'
        return string


def create_spend_chart(categories: list):
    category_names = []
    total_spent = 0
    for category in categories:
        total_spent += category.spent[0]
        category_names.append(category._category)
    percentage_before = [round((category.spent[0]/total_spent)*100) for category in categories]

    ten_multiplicity = [number * 10 for number in range(11)]
    percentages = []

    for num in percentage_before:
        big_difference = 100
        the_closest = 0
        for ten_idx in ten_multiplicity:  # [0, 10, 20, 30, ... 100]
            if num - ten_idx < 0:
                pass

            elif big_difference > (num - ten_idx):
                the_closest = ten_idx
                big_difference = (num - ten_idx)

        percentages.append(the_closest + 10)
        # added 10 here to make it match with tha chart bar

    percentages_bar = [f"{item * 10:>3}|" for item in range(11)][::-1]

    o_as_list = [round((item / 10)) * "o" for item in percentages]
    o_completed = []

    for percent in o_as_list:
        percent += f"{(11 - len(percent)) * ' '}"
        percent = percent[::-1]
        o_completed.append(list(percent))

    o_completed.insert(0, percentages_bar)

    string = 'Percentage spent by category\n'
    for idx in range(11):
        for itm in o_completed:
            if "|" in itm[idx]:
                string += f"{itm[idx]} "
            else:
                string += f"{itm[idx]}  "
        string += f"\n"

    dashes = len(percentages) * 3 + 1
    string += f"    {dashes * '-'}\n     "

    # return the largest len() in the category_names
    maxi = 0
    for name in category_names:
        tmp = len(name)
        if tmp > maxi:
            maxi = tmp

    name_completed = []

    for name in category_names:
        name += f"{(maxi - len(name)) * ' '}"
        name_completed.append(list(name))

    for idx in range(maxi):
        for itm in name_completed:
            string += f"{itm[idx]}  "
        string += f"\n     "
    return string[:-6]
