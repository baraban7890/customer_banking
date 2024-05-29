# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Please set the savings balance for your savings account in USD. "))
    savings_interest = float(input("Please set the interest rate of your savings account. "))
    savings_maturity = int(input("Please set the number of months (integer) for your savings account. "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The amount of interest earned on your savings account is: {interest_earned:.2f} and the updated savings account balance is {updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Please set the savings balance for your CD account. "))
    cd_interest = float(input("Please set the interest rate of your CD account. "))
    cd_maturity = int(input("Please set the number of months (integer) for your CD account. "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The amount of interest earned on your CD account is: {interest_earned:.2f} and the updated CD account balance is: {updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()