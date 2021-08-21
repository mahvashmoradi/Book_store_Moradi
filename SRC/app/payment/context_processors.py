# from app.cart.cart import Cart
from app.payment.views import cart_detail


def cart(request):
    return {'cart': cart_detail}
