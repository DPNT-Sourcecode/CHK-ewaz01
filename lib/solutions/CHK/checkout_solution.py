

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict

def checkout(skus):
    price_map = {
        "A" : 50,
        "B" : 30,
        "C" : 20,
        "D" : 15
    }

    offer_map = {
        "A" : (3, 130),
        "B" : (2, 45)
    }

    sku_freq = defaultdict(int)

    for sku in skus:
        if sku not in price_map:
            return -1
        sku_freq[sku] += 1

    print(sku_freq)

    total_checkout_value = 0
    for sku, sku_freq in sku_freq.items():
        if sku in offer_map:
            group_quantity = offer_map[sku][0]
            group_cost = offer_map[sku][1]
            groups = sku_freq // group_quantity
            remaining_individuals = sku_freq - (groups * group_quantity)
            total = (groups * group_cost) + (remaining_individuals * price_map[sku])
            total_checkout_value += total
        else:
            total_checkout_value += sku_freq * price_map[sku]
    
    print (total_checkout_value)
    return total_checkout_value

checkout("")

def test_checkout_empty():
    assert checkout("") == 0

def test_checkout_valid():
    assert checkout("AAAA") == 180
    assert checkout("ABCD") == 115
    assert checkout("AAAABCD") == 245

def test_checkout_invalid():
    assert checkout("ABCZ1") == -1


#test_checkout_empty()
#test_checkout_valid()
#test_checkout_invalid()

    




