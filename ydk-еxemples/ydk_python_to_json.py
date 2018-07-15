from ydk.providers import CodecServiceProvider
from ydk.services import CodecService
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ifmgr_cfg

# Instantiate the codec service
codec = CodecService()

# Instantiate the provider with json option
json_provider = CodecServiceProvider(type='json')

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

# Invoke the encode method to encode the YDK python object to a JSON payload
json = codec.encode(json_provider, interface_configurations)
print(json)
