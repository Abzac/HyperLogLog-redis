from HLL import HyperLogLog
import unittest

class TestRegisterFunctions(unittest.TestCase):

    def setUp(self):
        self.k = 5
        self.hll = HyperLogLog(5)

    def test_set_last_register(self):
        self.hll.set_register(self.k - 1, 1)
        self.assertTrue(self.hll.registers()[self.k - 1] == 1)

    def test_set_first_register(self):
        self.hll.set_register(0, 1)
        self.assertTrue(self.hll.registers()[0] == 1)

    def test_registers_returns_bytesarray(self):
        self.assertTrue(type(self.hll.registers()) is bytearray)

    def test_registesr_returns_correct_length_bytearray(self):
        self.assertTrue(len(self.hll.registers()) == pow(2, self.k))

class TestCardinalityEstimation(unittest.TestCase):

    def setUp(self):
        """ """

    def test_add_adds_an_element_to_a_random_register(self):
        """ """

    def test_small_range_correction(self):
        """ """

    def test_medium_range_no_correction(self):
        """ """

    def test_large_range_correction(self):
        """ """

    def test_the_larger_rank_is_used_when_comparing_elements(self):
        """ """

class TestHyperLogLogConstructor(unittest.TestCase):

    def test_one_is_invalid_size(self):
        with self.assertRaises(ValueError):
            HyperLogLog(0)

    def test_negative_size_is_invalid(self):
        with self.assertRaises(ValueError):
            HyperLogLog(-1)

    def test_minimum_size_is_valid(self):
        try:
            HyperLogLog(2)
        except Exception:
            self.fail()
    
    def test_maximum_size_is_valid(self):
        try:
            HyperLogLog(16)
        except Exception:
            self.fail()
    
    def test_greater_than_the_maximum_size_is_invalid(self):
        with self.assertRaises(ValueError):
            HyperLogLog(17)           
                 
    def test_all_registers_initialized_to_zero(self):
        hll = HyperLogLog(5)
        registers = hll.registers()
        for register in registers:
            self.assertEqual(register, 0)

    def test_k_param_correctly_determines_the_number_of_registers(self):
        hll = HyperLogLog(5)
        self.assertEqual(len(hll.registers()), 32)
        self.assertEqual(hll.size(), 32)

    def test_seed_parameter_sets_seed(self):
        hll = HyperLogLog(5, seed=4)
        self.assertEqual(4, 4)

class TestMerging(unittest.TestCase):

    def test_only_same_size_HyperLogLogs_can_be_merged(self):
        """ """

    def test_merge(self):
        """ """

if __name__ == '__main__':
    unittest.main()

"""
import HLL
n = HLL.HyperLogLog(12, 314)

path='/usr/share/dict/words'
f = open(path, 'r')
i = 0
for line in f.readlines():
    tokens = line.split(' ')
    for token in tokens:
        if i % 100 is 0:
            print n.murmur3_hash(token)
        n.add(token)

print dir(n)
print n.cardinality()
n.set_register(100,0)
n.set_register(200,0)
n.set_register(300,0)
n.set_register(300,0)

print n.cardinality()

# intersection(hyperloglog)
# hash(data)
# fold()
# union(hyperloglog)
# set all registers(val)
# check to see is VARARGS has a single arg component for hyperloglog_methods
"""
