#!/usr/bin/env python3

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

# TODO: implement
def yang_map_to_cbor_map_no_delta(yang_map):
    return {}

# TODO: implement
def cbor_map_no_delta_to_cbor_map_with_delta(cbor_map_no_delta):
    return cbor_map_no_delta

# TODO: implement
def cbor_map_with_delta_to_cbor_object(cbor_map_with_delta):
    return cbor_map_with_delta

if __name__ == "__main__":
    pass
