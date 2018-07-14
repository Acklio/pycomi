import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()

    request = Message(code=GET)
    # request.set_request_uri(uri='coap://example.com/c/RFw', set_uri_host=False)

    request.opt.uri_host=('example.com')
    request.opt.uri_path=('c','RFw')
    request.unresolved_remote = '[bbbb::2]:5683' #f-interop address
    request.opt.content_format = 60 #application-cbor

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
