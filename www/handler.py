__author__ = 'apple'

from coroweb import get,post

from models import User

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p


@get('/')
def index(request):
    users = yield from User.findAll()
    return{
        '__template__': 'test.html',
        'users': users
    }
