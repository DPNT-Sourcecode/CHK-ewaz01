

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict

# Individual default prices for each SKU
# All SKUs in this map are assumed to be valid and vice-versa
price_map = {
    "A" : 50,
    "B" : 30,
    "C" : 20,
    "D" : 15,
    "E" : 40,
    "F" : 10,
    "G" : 20,
    "H" : 10,
    "I" : 35,
    "J" : 60,
    "K" : 80,
    "L" : 90,
    "M" : 15,
    "N" : 40,
    "O" : 10,
    "P" : 50,
    "Q" : 30,
    "R" : 50,
    "S" : 30,
    "T" : 20,
    "U" : 40,
    "V" : 50,
    "W" : 20,
    "X" : 90,
    "Y" : 10,
    "Z" : 50
}

# for each deal/tuple corresponding to a SKU this map takes the form of:
# tuple[0]SKU for tuple[1]
offer_map = {
    "A" : [(5, 200),(3, 130)],
    "B" : [(2, 45)],
    "H" : [(10, 80), (5, 45)],
    "K" : [(2, 150)],
    "P" : [(5, 200)],
    "Q" : [(3, 80)],
    "V" : [(3, 130), (2, 90)],
}

# for each deal/tuple corresponding to a SKU this makes takes the form of:
# tuple[0]SKU get tuple[1] tuple[2] free
offer_map_free = {
    "E" : [(2, 1, "B")],
    "F" : [(2, 1, "F")],
    "N" : [(3, 1, "M")],
    "R" : [(3, 1, "Q")],
    "U" : [(3, 1, "U")],
}

def checkout(skus):
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
            if sku == y_sku:
                    num_free = get_sku_freq // (x+y)
                    sku_freq[y_sku] -= num_free
            else:
                if sku_freq[y_sku] >= num_free * y:
                        sku_freq[y_sku] -= num_free * y
                else:
                    sku_freq[y_sku] = 0
            get_sku_freq -= num_free * x

    # calculate checkout fees with deals
    total_checkout_value = 0
    for sku, sku_freq in sku_freq.items():
        if sku in offer_map:
            deals = offer_map[sku]
            temp_sku_freq = sku_freq
            for deal in deals:
                group_quantity = deal[0]
                group_cost = deal[1]
                groups = temp_sku_freq // group_quantity
                temp_sku_freq -= groups * group_quantity
                total = groups * group_cost
                total_checkout_value += total
            total_checkout_value += temp_sku_freq * price_map[sku]
        else:
            total_checkout_value += sku_freq * price_map[sku]
    
    return total_checkout_value

def test_checkout_empty():
    assert checkout("") == 0

def test_checkout_valid_basic():
    assert checkout("AAAA") == 180
    assert checkout("ABCD") == 115
    assert checkout("AAAABCD") == 245

def test_checkout_r2_deals():
    assert checkout("AAAAAAAA") == 330
    assert checkout("AAAAAAAAA") == 380
    assert checkout("AAAAAAAAAEE") == checkout("AAAAAAAAABEE")

def test_checkout_invalid():
    assert checkout("ABCZ1") == -1

def test_checkout_r3_deals():
    assert checkout("F") == 10
    assert checkout("FF") == 20
    assert checkout ("FFF") == 20
    assert checkout ("FFFF") == 30
    assert checkout ("FFFFFF") == 40

"""
test_checkout_empty()
test_checkout_valid_basic()
test_checkout_invalid()
test_checkout_r2_deals()
test_checkout_r3_deals()
"""
    





