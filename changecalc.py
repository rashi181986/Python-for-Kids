def count_division_ways(total_money, denominations):
    # Initialize a list to store the number of ways to reach every value up to 'total_money'
    # dp[i] will store the number of ways to make change for amount 'i'
    dp = [0] * (total_money + 1)
    
    # Base case: There is 1 way to make zero money (using no coins)
    dp[0] = 1
    
    # Iterate through each coin denomination
    for coin in denominations:
        # Update the ways for every amount from the coin value up to the total
        for current_amount in range(coin, total_money + 1):
            dp[current_amount] += dp[current_amount - coin]
            
    return dp[total_money]

# Example Usage:
amount_to_divide = 10  # Total money
available_coins = [1, 2, 5]  # Available denominations

result = count_division_ways(amount_to_divide, available_coins)
print(f"There are {result} ways to divide ${amount_to_divide} using denominations {available_coins}.")
