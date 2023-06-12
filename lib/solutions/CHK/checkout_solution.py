

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

    total_checkout_value = 0
    for sku, sku_freq in sku_freq.items():
        i

    





