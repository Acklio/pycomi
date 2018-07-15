from ydk.providers import CodecServiceProvider
from ydk.services import CodecService

# Instantiate the codec service
codec = CodecService()

# Instantiate codec providers with json and xml options
json_provider = CodecServiceProvider(type='json')
xml_provider = CodecServiceProvider(type='xml')

# Declare the JSON configuration
if_json = ''' {
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

# Invoke the decode method  to decode the JSON payload to a YDK python object
interface_configurations = codec.decode(json_provider, if_json)

# Invoke the encode method to encode the YDK python object to an XML string
if_xml = codec.encode(xml_provider, interface_configurations)
print(if_xml)
