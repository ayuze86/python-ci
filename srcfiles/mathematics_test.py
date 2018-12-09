# import importlib
# import mathematics 
# importlib.reload(mathematics)

import unittest
from mathematics import Math
#from src.math import Math
#from src import math

    
class MathTest(unittest.TestCase):
    
    
    def test_addition(self):
        out_addi = Math.addition(self, 3, 4)
        self.assertEqual(out_addi, 8)
 
  
#     def test_subtraction(self):
#         out_subtra = Math.subtraction(self, 10, 8)
#         self.assertEqual(out_subtra, 2) 
#               
# if __name__ == '__main__':
#     unittest.main()