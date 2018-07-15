from ydk.providers import CodecServiceProvider
from ydk.services import CodecService

# Instantiate the codec service
codec = CodecService()

# Instantiate codec providers with json and xml options
json_provider = CodecServiceProvider(type='json')

# Declare the JSON configuration
EXAMPLE_YANG_JSON = ''' {
  "Cisco-IOS-XR-ifmgr-cfg:interface-configurations": {
    "interface-configuration": [
      {
        "active": "act",
        "interface-name": "Loopback0",
        "description": "PRIMARY ROUTER LOOPBACK",
        "Cisco-IOS-XR-ipv4-io-cfg:ipv4-network": {
          "addresses": {
            "primary": {
              "address": "172.16.255.1",
              "netmask": "255.255.255.255"
            }
          }
        }
      }
    ]
  }
}
'''

# TODO: fill out
EXAMPLE_YANG_OBJECT = codec.decode(json_provider, EXAMPLE_YANG_JSON)

# TODO: fix to fit our test case
EXAMPLE_YANG_MAP = {
  "Cisco-IOS-XR-ifmgr-cfg:interface-configurations": {
    "interface-configuration": [
      {
        "active": "act",
        "interface-name": "Loopback0",
        "description": "PRIMARY ROUTER LOOPBACK",
        "Cisco-IOS-XR-ipv4-io-cfg:ipv4-network": {
          "addresses": {
            "primary": {
              "address": "172.16.255.1",
              "netmask": "255.255.255.255"
            }
          }
        }
      }
    ]
  }
}

# TODO: implement
EXAMPLE_CBOR_MAP_NO_DELTA = {

}


