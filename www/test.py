__author__ = 'apple'

import orm,sys,asyncio
from models import User,Blog,Comment


def test(loop):
    yield from orm.create_pool(loop=loop, user='root',password='root',db='awesome')
    users = yield from User.findAll()
    for user in users:
        print(user.name+'   '+user.email+'\n')


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)