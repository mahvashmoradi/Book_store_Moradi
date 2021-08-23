# from app.cart.cart import Cart
from app.payment.views import Cart


def cart(request):
    return {'cart': Cart}
