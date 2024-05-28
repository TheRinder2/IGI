import pytz
from django import template
register = template.Library()


@register.filter
def convert_time_to_local(dt):
    user_timezone = pytz.timezone('Europe/Moscow')
    user_time = dt.astimezone(user_timezone)
    return user_time.strftime("%Y-%m-%d %H:%M:%S")

@register.filter
def convert_cost_to_discount(cs):
    return int(100 - cs * 100)
