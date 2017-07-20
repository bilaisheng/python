import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
# loop参数 针对1个用户访问并没有什么用,
# 针对多个用户才会体现效果
def init(loop):
    # 定义为可以循环的http响应
    app = web.Application(loop=loop)
    # http响应表头
    app.router.add_route('GET', '/', index)
    # 采用异步IO开启服务器连接
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000....')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()