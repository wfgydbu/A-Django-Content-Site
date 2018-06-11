from ..models import Category, Sticker
from django import template

register = template.Library()

@register.simple_tag
def get_recent_stickers(num=8):
    return Sticker.objects.all().order_by('-views')[:num]


@register.simple_tag
def get_categories(num=4):
    return get_all_categories()[:num]

@register.simple_tag
def get_all_categories():
    return Category.objects.all()

@register.simple_tag
def parser_full_url(full_path, path):
    print (full_path, path)
    if path == '/' or full_path == '/':
        return "Home"

    r = None
    if len(full_path.split('?')) > 1:
        r = full_path.split('?')[1].split('=')[1]

    res = ['Home']
    res += [x for x in path.split('/') if x != '']

    if r:
        res.append(r)

    try:
        idx = res.index('sticker')
        obj = Sticker.objects.all().filter(md5=res[idx+1]).values()[0]
        res[idx+1] = obj['title']
        res[idx] = Category.objects.all().filter(id=obj['category_id']).values()[0]['name']
    except:
        pass

    try:
        idx = res.index('category')
        res.remove(res[idx])
    except:
        pass

    try:
        idx = res.index('about')
        res[idx] = '关于'
    except:
        pass

    res = " > ".join(res)

    return res