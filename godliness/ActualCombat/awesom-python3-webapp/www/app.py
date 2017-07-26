import logging;

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


def index(request):
    # 此处为了兼容 增加content_type='text/html'
    # 若不增加可能部分浏览器不识别,会提示下载文件
    return web.Response(body=b'<h1>Awesome</h1>',  content_type='text/html')

# loop参数 针对1个用户访问并没有什么用,
# 针对多个用户才会体现效果
@asyncio.coroutine
def init(loop):
    # 定义为可以循环的http响应
    app = web.Application(loop=loop)

    # http响应表头
    app.router.add_route('GET', '/', index)

    # 采用异步IO开启服务器连接
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)

    # 打印日志信息到控制台
    logging.info('server started at http://127.0.0.1:9000....')
    return srv

# async def init(loop): # async 替代 @asyncio.coroutine装饰器,代表这个是要异步运行的函数
#     app=web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     srv = await loop.create_server(app.make_handler(), '0.0.0.0', 5000)  #await 代替yield from ,表示要放入asyncio.get_event_loop中进行的异步操作
#     logging.info('server started at http://127.0.0.1:5000...')
#     return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
