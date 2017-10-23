from test_celery import hello
import datetime

a = {
    'id': 'bf3042262d0e0a8f7d2cc0af7d1a11e84e526836c833fb559e771c4f0d77007f_sell',
    'amount': '-53984600000',
    'price': '0.00305888',
    'tokenGet': '0x0000000000000000000000000000000000000000',
    'amountGet': '1651324132480000000',
    'tokenGive': '0x226bb599a12c826476e3a771454697ea52e9e220',
    'amountGive': '53984600000',
    'expires': '4309925',
    'nonce': '1669585874',
    'v': 27,
    'r': '0xb63724fe13a70dc25a7eee9a2396080ecfd5389f96086bd77427ce35894da492',
    's': '0x39629a2f7bfad066faf1b0ee7fb856bd57990941006d9d79ead3c87c7a66c92b',
    'user': '0x4f2862CB1cd0958D977F266Cb03c4566e2CEdfAC',
    'updated': '2017-09-21T22:52:11.541Z',
    'availableVolume': '53984600000',
    'ethAvailableVolume': '539.846',
    'availableVolumeBase': '1651324132480000000',
    'ethAvailableVolumeBase': '1.65132413248',
    'amountFilled': None
}


print(datetime.datetime.now())

hello.delay(a)
