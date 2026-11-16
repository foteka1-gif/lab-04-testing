import pytest
from hotel_filter import filter_hotels

SAMPLE_HOTELS = [
    {"name": "Grand Hotel", "price": 2500, "stars": 5, "available": True},
    {"name": "City Inn", "price": 1200, "stars": 3, "available": True},
    {"name": "Budget Stay", "price": 800, "stars": 2, "available": False},
    {"name": "Sea View", "price": 1800, "stars": 4, "available": True},
]

def test_filter_default_only_available():
    res = filter_hotels(SAMPLE_HOTELS)
    assert len(res) == 3

def test_filter_by_max_price():
    res = filter_hotels(SAMPLE_HOTELS, max_price=1800)
    assert [h["name"] for h in res] == ["City Inn", "Sea View"]

def test_filter_by_min_stars():
    res = filter_hotels(SAMPLE_HOTELS, min_stars=4)
    assert [h["name"] for h in res] == ["Grand Hotel", "Sea View"]

def test_filter_include_unavailable():
    res = filter_hotels(SAMPLE_HOTELS, max_price=1000, only_available=False)
    assert [h["name"] for h in res] == ["Budget Stay"]

def test_empty_hotels_list():
    assert filter_hotels([]) == []

def test_invalid_inputs_raise_error():
    with pytest.raises(ValueError):
        filter_hotels(SAMPLE_HOTELS, max_price=-100)
    with pytest.raises(ValueError):
        filter_hotels(SAMPLE_HOTELS, min_stars=6)
