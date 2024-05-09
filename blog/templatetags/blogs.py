from django import template

register = template.Library()

@register.filter
def is_publish(blog_status):
    if blog_status == 'Pub':
        return True
    return False
