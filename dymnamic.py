def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Таблиця для зберігання мінімальної кількості монет для кожної суми від 0 до amount
    coin_table = [float('inf')] * (amount + 1)
    coin_table[0] = 0  # Нуль монет для суми 0
    
    # Таблиця для зберігання номіналів монет, які використовуються для кожної суми
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and coin_table[i - coin] + 1 < coin_table[i]:
                coin_table[i] = coin_table[i - coin] + 1
                coin_used[i] = coin
    
    # словник використаних монет
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Приклад використання
amount = 113
print(find_min_coins(amount))  # Output: {50: 2, 10: 1, 2: 1, 1: 1}
