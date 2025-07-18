from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity



# from django import template

# register = template.Library()


# @register.filter
# def calc_subtotal(price, item):
#     quantity = item.get('quantity', 0)
#     return price * quantity
