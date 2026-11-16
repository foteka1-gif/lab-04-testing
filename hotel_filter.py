def filter_hotels(hotels, max_price=None, min_stars=1, only_available=True):
    if max_price is not None and max_price < 0:
        raise ValueError("Максимальна ціна не може бути від'ємною")
    if min_stars < 1 or min_stars > 5:
        raise ValueError("Кількість зірок має бути від 1 до 5")

    result = []
    for hotel in hotels:
        if only_available and not hotel.get("available", False):
            continue
        if hotel.get("stars", 0) < min_stars:
            continue
        if max_price is not None and hotel.get("price", 0) > max_price:
            continue
        result.append(hotel)

    return result
