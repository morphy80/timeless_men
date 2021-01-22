from django.shortcuts import render, redirect


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    warranty = None
    if 'product_warranty' in request.POST:
        warranty = request.POST['product_warranty']
    cart = request.session.get('cart', {})

    if warranty:
        if item_id in list(cart.keys()):
            if warranty in cart[item_id]['items_by_warranty'].keys():
                cart[item_id]['items_by_warranty'][warranty] += quantity
            else:
                cart[item_id]['items_by_warranty'][warranty] = quantity
        else:
            cart[item_id] = {'items_by_warranty': {warranty: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
