import unittest
import calc

class testclass(unittest.TestCase):

     def test_add(self):
         
         self.assertEqual(calc.add(11,12),23)
         self.assertEqual(calc.add(-11,12),1)
         self.assertEqual(calc.add(-11,-12),-23)
         self.assertEqual(calc.add(11,-12),-1)
         self.assertEqual(calc.add(0.1,0.5),0.6)
         


     def test_subtract(self):
         
         self.assertEqual(calc.subtract(10,2),8)
         self.assertEqual(calc.subtract(-10,2),-12)
         self.assertEqual(calc.subtract(-11,-12),1)
         self.assertEqual(calc.subtract(11,-12),23)
         self.assertEqual(calc.subtract(0.1,0.5),-0.4)
         


    

     def test_multiply(self):
         
         self.assertEqual(calc.multiply(11,12),13)
         self.assertEqual(calc.multiply(-11,12),-132)
         self.assertEqual(calc.multiply(-11,-12),132)
         self.assertEqual(calc.multiply(11,-12),-132)
         self.assertEqual(calc.add(0.1,0.5),0.6)
         


     def test_divide(self):
         
         self.assertEqual(calc.divide(4,2),2)
         self.assertEqual(calc.divide(-4,2),-2)
         self.assertEqual(calc.divide(-4,-2),2)
         self.assertEqual(calc.divide(4,-2),-2)

if __name__ =='__main__':
    unittest.main()
