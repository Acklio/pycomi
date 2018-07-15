import logging
import asyncio

from aiocoap import *

from cbor2 import dumps, loads

logging.basicConfig(level=logging.INFO)

COMMANDS = {
   GET,
   FETCH,
   PUT
}

def set_req_params(request, *path):
  request.opt.uri_host=('example.com')
  request.opt.uri_path=('c',) + path
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

async def send(command, payload_object='', *path):
  assert command in COMMANDS

  protocol = await Context.create_client_context()

  # Convert payload object to json (cbor?)
  payload = _object_to_payload(payload_object)

  request = Message(code=command, payload=payload)
  set_req_params(request, *path)
  await make_req_and_parse_ans(protocol, request)

def _object_to_payload(payload_object):
  return payload_object

async def main():
  await send(GET, b'', "RFy")

  await send(FETCH, b'\x82\x1A\x00\x01\x11\x73\x01')

if __name__ == "__main__":
  asyncio.get_event_loop().run_until_complete(main())
