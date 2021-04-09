database = {"Food": 0, "Clothing": 0, "Entertainment": 0}

class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self):
        database[self.category] += self.amount

    def withdrawal(self):
        database[self.category] -= self.amount
        

    def balances(self):
        for budget_item, budget_amount in database.items():
            print("%s: %d" %(budget_item, budget_amount))

    def transfers(self):
        pass # Performed transfer operation in the conditional statement below
             # Created this because it was a requirement in the task

check = False
while check == False:
    userOp = int(input("\nOptions: (1) Deposit  (2) Withdrawal  (3) Balances  (4) Transfer  (5) Exit \n"))
    if userOp == 1:
        userAmount = int(input("How much to deposit: \n"))
        userCat = input("Which category: \n")
        new_budget = Budget(userCat, userAmount)
        new_budget.deposit()
    elif userOp == 2:
        userAmount = int(input("How much to withdraw: \n"))
        userCat = input("Which category: \n")
        new_budget = Budget(userCat, userAmount)
        new_budget.withdrawal()
    elif userOp == 3:
        new_budget = Budget("", 0)
        new_budget.balances()
    elif userOp == 4:
        transferFrom = input("From: ")
        transferTo = input("To: ")
        new_budget = Budget(transferTo, database[transferFrom])
        new_budget.deposit()
        database[transferFrom] = 0
        print("Transfer Done.")
    elif userOp == 5:
        exit()


