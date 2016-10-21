#https://www.interviewcake.com/question/python/stock-price
#challenge 1 THIS IS SLOW!

def get_max_profit(stock_prices_yesterday):

    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit




def get_max_profit(lst):
	l = list(lst)

	'''
	cant short sell so need to buy then sell
	buy low sell high
	need to return a profit for that day
	do know what is going to happen next
	what if min comes before max
	need min before max, second max
	'''
	print(l)
	while len(l) > 2:
		low = min(l)
		hi = max(l)
		low_i = l.index(low)
		hi_i = l.index(hi)
		print(l)
		if low_i < hi_i:
			return -low+  hi
		else:
			l.pop(hi_i)
	#at this pt, we have success or not?
	if low_i < hi_i:
		return -min(l)+max(l)
	else:
		return -max(l) + min(l)

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday_2 = [12, 7, 5, 8, 11, 9]
stock_prices_yesterday_neg = [12, 10, 7, 4, 3, 2]
print(get_max_profit(stock_prices_yesterday_neg))
# returns 6 (buying for $5 and selling for $11)
