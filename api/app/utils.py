from django.db.models import Func


class Round2decimals(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s::numeric, 2)'
