#!python
from rom_to_int import rom_to_int
import unittest

class RomToIntTest(unittest.TestCase):
    def test_rom_to_int(self):
        cases = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
        ans = [3, 4, 9, 58, 1994]
        
        for i, case in enumerate(cases):
            assert rom_to_int(case) == ans[i]

