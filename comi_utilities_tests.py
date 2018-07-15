from comi_utilities import *
from comi_constants import *
import unittest

class TestYangObjectToMap(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            yang_object_to_map(EXAMPLE_YANG_OBJECT),
            EXAMPLE_YANG_MAP
        )

class TestYangMapToCborMapNoDelta(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            yang_map_to_cbor_map_no_delta(EXAMPLE_YANG_MAP),
            EXAMPLE_CBOR_MAP_NO_DELTA
        )

if __name__ == '__main__':
    unittest.main()
