from ydk.providers import CodecServiceProvider
from ydk.services import CodecService
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ifmgr_cfg

# Instantiate the codec service
codec = CodecService()

# Instantiate the interface configuration class to configure the IPv4 loopback
interface_configurations =  Cisco_IOS_XR_ifmgr_cfg.InterfaceConfigurations()

# Instantiate the InterfaceConfiguration list instance
interface_configuration = interface_configurations.InterfaceConfiguration()
interface_configuration.active = "act"
interface_configuration.interface_name = "Loopback0"
interface_configuration.description = "PRIMARY ROUTER LOOPBACK"

# Instantiate the Primary presence node
interface_configuration.ipv4_network.addresses.primary = interface_configuration.ipv4_network.addresses.Primary()
interface_configuration.ipv4_network.addresses.primary.address = "172.16.255.1"
interface_configuration.ipv4_network.addresses.primary.netmask = "255.255.255.255"

# Append the list instance to the parent list
interface_configurations.interface_configuration.append(interface_configuration)

# TODO: fill out
EXAMPLE_YANG_OBJECT = interface_configurations

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


