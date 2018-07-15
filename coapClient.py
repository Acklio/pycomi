import logging
import asyncio

from aiocoap import *

from cbor2 import dumps, loads

logging.basicConfig(level=logging.INFO)

def set_req_params(request):
    request.opt.uri_host=('example.com')
    request.opt.uri_path=('c','RFy')
    request.unresolved_remote = '[bbbb::2]:5683'
    request.opt.content_format = 60

async def make_req_and_parse_ans(protocol, request):
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, loads(response.payload)))

async def send_get():
    protocol = await Context.create_client_context()

    request = Message(code=GET)
    # request.set_request_uri(uri='coap://example.com/c/RFw', set_uri_host=False)

    set_req_params(request)
    await make_req_and_parse_ans(protocol, request)

async def send_fetch():
    protocol = await Context.create_client_context()

    request = Message(code=FETCH, payload=b'\x82\x1A\x00\x01\x11\x73\x01')

    set_req_params(request)
    await make_req_and_parse_ans(protocol, request)

async def main():
    await send_fetch()
    await send_get()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
