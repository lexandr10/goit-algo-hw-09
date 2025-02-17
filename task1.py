



def find_coins_greedy(sum):
    coins = [50, 25, 10, 5, 2, 1]
    iter = 0
    result = {50: 0, 10: 0, 2: 0, 1: 0}

    while sum:
        if coins[iter] <= sum:
            sum -= coins[iter]
            result[coins[iter]] += 1
        else:
            iter += 1
    return result





number = 113

print(find_coins_greedy(number))


def find_min_coins(amount):
    coins = [50,25,10,5,2,1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin


    if dp[amount] == float("inf"):
        return {}
    
    result = {50: 0, 10: 0, 2: 0, 1: 0}

    while amount > 0:
        coin = coin_used[amount] 
        result[coin] += 1
        amount -= coin
    
    return result

print(find_min_coins(number))