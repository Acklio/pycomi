#!/usr/bin/env python3
from cisco_sid import cisco_sid_map

# TODO: implement
def yang_object_to_map(yang_obj):
  return {
    yang_obj.path(): yang_obj_children_to_map(yang_obj)
  }

def yang_obj_children_to_map(yang_obj):
  if not hasattr(yang_obj, "children"):
    return yang_obj

  res = {}
  for (k, v) in yang_obj._leafs.items():
    if v is None:
      continue
    if hasattr(v, "get") and v.get() != u'':
      res[v.name] = v.get()
    if hasattr(v, "getYLeafs") and len(v.getYLeafs()) > 0:
      res[v.name] = v.getYLeafs()

  for (k, c) in yang_obj.children().items():
    v = yang_obj_children_to_map(c)
    if v is not None and k.find("[") >= 0 and k.find("]") >= 0:
      v = [v]
    if v is not None:
      res[c.yang_name] = v

  if len(res) == 0:
    return None

  return res

def yang_map_to_cbor_map_no_delta(yang_map):

    # Get a map that goes from an identifier to an sid
    sid_map = _sid_items_to_id_to_sid_map(cisco_sid_map["items"])

    cbor_map = _yang_map_to_cbor_map_no_delta(yang_map, sid_map)

    return cbor_map

def _yang_map_to_cbor_map_no_delta(yang_map, sid_map, prefix=''):

    if isinstance(yang_map, dict):
        cbor_map = {}
        for k,v in yang_map.items():
            path = prefix + "/" + k
            sid = sid_map[path]
            cbor_map[sid] = _yang_map_to_cbor_map_no_delta(v, sid_map, prefix=path)

        return cbor_map

    if isinstance(yang_map, list):
        cbor_list = []
        for v in yang_map:
            cbor_map = _yang_map_to_cbor_map_no_delta(v, sid_map, prefix=prefix)
            cbor_list.append(cbor_map)
        return cbor_list

    return yang_map

# TODO: implement
def cbor_map_no_delta_to_cbor_map_with_delta(cbor_map_no_delta):
    return cbor_map_no_delta

# TODO: implement
def cbor_map_with_delta_to_cbor_object(cbor_map_with_delta):
    return cbor_map_with_delta

def _sid_items_to_id_to_sid_map(sid_file_map):
    '''
    Convert from list of the form:
    [
        {
            "namespace": "module", 
            "identifier": "Cisco-IOS-XR-ifmgr-cfg", 
            "sid": 7000
        }, 
        {
            "namespace": "data", 
            "identifier": "/Cisco-IOS-XR-ifmgr-cfg:global-interface-configuration", 
            "sid": 7001
        }
    ]

    to a map of the form:
    {
      "Cisco-IOS-XR-ifmgr-cfg": 7000,
      "/Cisco-IOS-XR-ifmgr-cfg:global-interface-configuration": 7001
    }
    '''

    id_to_sid_map = {}
    for item in sid_file_map:
        identifier      = item["identifier"]
        sid             = item["sid"]

        id_to_sid_map[identifier] = sid

    return id_to_sid_map


if __name__ == "__main__":
    pass
