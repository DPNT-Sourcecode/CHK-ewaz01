

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict

def checkout(skus):
    # Individual default prices for each SKU
    # All SKUs in this map are assumed to be valid and vice-versa
    price_map = {
        "A" : 50,
        "B" : 30,
        "C" : 20,
        "D" : 15
    }

    # for each deal/tuple corresponding to a SKU this map takes the form of:
    # tuple[0]SKU for tuple[1]
    offer_map = {
        "A" : (3, 130),
        "B" : (2, 45)
    }

    # for each deal/tuple corresponding to a SKU this makes takes the form of:
    # tuple[0]SKU get tuple[1] tuple[2] free
    offer_map_free = {
        "E" : [(2, 1, "B")]
    }

    sku_freq = defaultdict(int)

    # create frequency mapping logging how many times each SKU was seen in our input
    # returns -1 if SKU not in our price_map
    for sku in skus:
        if sku not in price_map:
            return -1
        sku_freq[sku] += 1

    
    # apply savings in the case of buy x to get y free
    for sku, deals in offer_map_free.items():
        get_sku_freq = sku_freq[sku]
        for deal in deals:
            x = deal[0]
            y = deal[1]
            y_sku = deal[2]
            num_free = get_sku_freq // x
            if sku_freq[y_sku] >= num_free * y:
                sku_freq[y_sku] -= num_free * y
            else:
                sku_freq[y_sku] = 0
            get_sku_freq -= num_free * x

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
    
    return total_checkout_value

checkout("BBBB")
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

    






