from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(
                    request, f'Updated warranty {warranty.upper()} {product.name} quantity to {cart[item_id]["items_by_warranty"][warranty]}')
            else:
                cart[item_id]['items_by_warranty'][warranty] = quantity
                messages.success(
                    request, f'Added warranty {warranty.upper()} {product.name} to your cart.')
        else:
            cart[item_id] = {'items_by_warranty': {warranty: quantity}}
            messages.success(
                request, f'Added warranty {warranty.upper()} {product.name} to your cart.')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    warranty = None
    if 'product_warranty' in request.POST:
        warranty = request.POST['product_warranty']
    cart = request.session.get('cart', {})

    if warranty:
        if quantity > 0:
            cart[item_id]['items_by_warranty'][warranty] = quantity
            messages.success(
                    request, f'Updated warranty {warranty.upper()} {product.name} quantity to {cart[item_id]["items_by_warranty"][warranty]}')
        else:
            del cart[item_id]['items_by_warranty'][warranty]
            if not cart[item_id]['items_by_warranty']:
                cart.pop(item_id)
            messages.success(request, f'Removed warranty {warranty.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        warranty = None
        if 'product_warranty' in request.POST:
            warranty = request.POST['product_warranty']
        cart = request.session.get('cart', {})

        if warranty:
            del cart[item_id]['items_by_warranty'][warranty]
            if not cart[item_id]['items_by_warranty']:
                cart.pop(item_id)
            messages.success(request, f'Removed warranty {warranty.upper()} {product.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
