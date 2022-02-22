import httpretty

from client_level0.core import place_order, BASE_URL


@httpretty.activate
def test_place_order():
    httpretty.register_uri(
        httpretty.GET,
        f'{BASE_URL}/PlaceOrder',
        'Order=1'
    )
    assert place_order('latte', 'whole', 'large', 'takeAway') == '1'
