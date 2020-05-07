from test import Calculation
import unittest

class TestСalculation(unittest.TestCase):

    def test_1_function_1(self):
        F = Calculation(4)
        res = F.function_1()
        self.assertEqual(res, None )
    def test_1_function_2(self):
        Functions = Calculation(4)
        res = Functions.function_2()
        self.assertEqual(res, None)

    def test_1_function_3(self):
        Functions = Calculation(4)
        res = Functions.function_3()
        self.assertEqual(res, None)

    def test_1_function_4(self):
        Functions = Calculation(4)
        res = Functions.function_4()
        self.assertEqual(res, None)

    def test_2_function_1(self):
        Functions = Calculation('5 5')
        res = Functions.function_1()
        self.assertEqual(res, 20713429.495)

    def test_2_function_2(self):
        Functions = Calculation('5 5')
        res = Functions.function_2()
        self.assertEqual(res, 779598.985)
        
    def test_2_function_3(self):
        Functions = Calculation('5 5')
        res = Functions.function_3()
        self.assertEqual(res, 6367.4985)

    def test_2_function_4(self):
        Functions = Calculation('5 5')
        res = Functions.function_4()
        self.assertEqual(res, 385.65999999999997)

    def test_3_function_1(self):
        Functions = Calculation(' 7 5')
        res = Functions.function_1()
        self.assertEqual(res, 71318906.175)

    def test_3_function_2(self):
        Functions = Calculation(' 7 5')
        res = Functions.function_2()
        self.assertEqual(res, 1981601.025)

    def test_3_function_3(self):
        Functions = Calculation(' 7 5')
        res = Functions.function_3()
        self.assertEqual(res, 11715.952499999998)

    def test_3_function_4(self):
        Functions = Calculation(' 7 5')
        res = Functions.function_4()
        self.assertEqual(res, 525.9)

    def test_4_function_1(self):
        Functions = Calculation('-123')
        res = Functions.function_1()
        self.assertEqual(res, 'None')

    def test_4_function_2(self):
        Functions = Calculation('-123')
        res = Functions.function_2()
        self.assertEqual(res, 'None')

    def test_4_function_3(self):
        Functions = Calculation('-123')
        res = Functions.function_3()
        self.assertEqual(res, 'None')

    def test_4_function_4(self):
        Functions = Calculation('-123')
        res = Functions.function_4()
        self.assertEqual(res, 'None')
    
    def test_5_function_1(self):
        Functions = Calculation(- 34)
        res = Functions.function_1()
        self.assertEqual(res, "Введені некоректні дані!!!!!")

    def test_5_function_2(self):
        Functions = Calculation(- 34)
        res = Functions.function_2()
        self.assertEqual(res, "Введені некоректні дані!!!!!")

    def test_5_function_3(self):
        Functions = Calculation(- 34)
        res = Functions.function_3()
        self.assertEqual(res, "Введені некоректні дані!!!!!")

    def test_5_function_4(self):
        Functions = Calculation(- 34)
        res = Functions.function_4()
        self.assertEqual(res, "Введені некоректні дані!!!!!")

    def test_6_function_1(self):
        Functions = Calculation('-3 4')
        res = Functions.function_1()
        self.assertEqual(res, "Введені некоректні данні!!!!!")

    def test_6_function_2(self):
        Functions = Calculation('-3 4')
        res = Functions.function_2()
        self.assertEqual(res, "Введені некоректні данні!!!!!")

    def test_6_function_3(self):
        Functions = Calculation('-3 4')
        res = Functions.function_3()
        self.assertEqual(res, "Введені некоректні данні!!!!!")

    def test_6_function_4(self):
        Functions = Calculation('-3 4')
        res = Functions.function_4()
        self.assertEqual(res, "Введені некоректні данні!!!!!")

    def test_7_function_1(self):
        Functions = Calculation('-7')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_7_function_2(self):
        Functions = Calculation('-7')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_7_function_3(self):
        Functions = Calculation('-7')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_7_function_4(self):
        Functions = Calculation('-7')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_8_function_1(self):
        Functions = Calculation(55.7)
        res = Functions.function_1()
        self.assertEqual(res, 21783959.169380605)

    def test_8_function_2(self):
        Functions = Calculation(55.7)
        res = Functions.function_2()
        self.assertEqual(res, 809837.7238870001)

    def test_8_function_3(self):
        Functions = Calculation(55.7)
        res = Functions.function_3()
        self.assertEqual(res, 6527.37717)

    def test_8_function_4(self):
        Functions = Calculation(55.7)
        res = Functions.function_4()
        self.assertEqual(res, 390.5684)

    def test_9_function_1(self):
        Functions = Calculation('56,7')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_9_function_2(self):
        Functions = Calculation('56,7')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_9_function_3(self):
        Functions = Calculation('56,7')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_9_function_4(self):
        Functions = Calculation('56,7')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_10_function_1(self):
        Functions = Calculation('78. ')
        res = Functions.function_1()
        self.assertEqual(res, 83394828.348)

    def test_10_function_2(self):
        Functions = Calculation('78. ')
        res = Functions.function_2()
        self.assertEqual(res, 2229604.338)

    def test_10_function_3(self):
        Functions = Calculation('78. ')
        res = Functions.function_3()
        self.assertEqual(res, 12657.738599999999)

    def test_10_function_4(self):
        Functions = Calculation('78. ')
        res = Functions.function_4()
        self.assertEqual(res, 546.9359999999999)

    def test_11_function_1(self):
        Functions = Calculation('78. 1')
        res = Functions.function_1()
        self.assertEqual(res, 83822085.80938058)

    def test_11_function_2(self):
        Functions = Calculation('78. 1')
        res = Functions.function_2()
        self.assertEqual(res, 2238209.1523989993)

    def test_11_function_3(self):
        Functions = Calculation('78. 1')
        res = Functions.function_3()
        self.assertEqual(res, 12689.758289999996)

    def test_11_function_4(self):
        Functions = Calculation('78. 1')
        res = Functions.function_4()
        self.assertEqual(res, 547.6371999999999)

    def test_12_function_1(self):
        Functions = Calculation('32.,1')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_12_function_2(self):
        Functions = Calculation('32.,1')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_12_function_3(self):
        Functions = Calculation('32.,1')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_12_function_4(self):
        Functions = Calculation('32.,1')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_13_function_1(self):
        Functions = Calculation('asd')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_13_function_2(self):
        Functions = Calculation('asd')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_13_function_3(self):
        Functions = Calculation('asd')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_13_function_4(self):
        Functions = Calculation('asd')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_14_function_1(self):
        Functions = Calculation('>')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_14_function_2(self):
        Functions = Calculation('>')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_14_function_3(self):
        Functions = Calculation('>')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_14_function_4(self):
        Functions = Calculation('>')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_15_function_1(self):
        Functions = Calculation('q ')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_15_function_2(self):
        Functions = Calculation('q ')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_15_function_3(self):
        Functions = Calculation('q ')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_15_function_4(self):
        Functions = Calculation('q ')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_16_function_1(self):
        Functions = Calculation('6*')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_16_function_2(self):
        Functions = Calculation('6*')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_16_function_3(self):
        Functions = Calculation('6*')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_16_function_4(self):
        Functions = Calculation('6*')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_17_function_1(self):
        Functions = Calculation('*9')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_17_function_2(self):
        Functions = Calculation('*9')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_17_function_3(self):
        Functions = Calculation('*9')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_17_function_4(self):
        Functions = Calculation('*9')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_18_function_1(self):
        Functions = Calculation(' ')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_18_function_2(self):
        Functions = Calculation(' ')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_18_function_3(self):
        Functions = Calculation(' ')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_18_function_4(self):
        Functions = Calculation(' ')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_19_function_1(self):
        Functions = Calculation('   ')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_19_function_2(self):
        Functions = Calculation('   ')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_19_function_3(self):
        Functions = Calculation('   ')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_19_function_4(self):
        Functions = Calculation('   ')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_20_function_1(self):
        Functions = Calculation('   a')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_20_function_2(self):
        Functions = Calculation('   a')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_20_function_3(self):
        Functions = Calculation('   a')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_20_function_4(self):
        Functions = Calculation('   a')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_21_function_1(self):
        Functions = Calculation(45)
        res = Functions.function_1()
        self.assertEqual(res, 15332406.063000001)

    def test_21_function_2(self):
        Functions = Calculation(45)
        res = Functions.function_2()
        self.assertEqual(res, 621136.497)

    def test_21_function_3(self):
        Functions = Calculation(45)
        res = Functions.function_3()
        self.assertEqual(res, 5491.9196999999995)

    def test_21_function_4(self):
        Functions = Calculation(45)
        res = Functions.function_4()
        self.assertEqual(res, 357.61199999999997)

    def test_22_function_1(self):
        Functions = Calculation('-5')
        res = Functions.function_1()
        self.assertEqual(res, "None")

    def test_22_function_2(self):
        Functions = Calculation('-5')
        res = Functions.function_2()
        self.assertEqual(res, "None")

    def test_22_function_3(self):
        Functions = Calculation('-5')
        res = Functions.function_3()
        self.assertEqual(res, "None")

    def test_22_function_4(self):
        Functions = Calculation('-5')
        res = Functions.function_4()
        self.assertEqual(res, "None")

    def test_23_function_1(self):
        Functions = Calculation(1)
        res = Functions.function_1()
        self.assertEqual(res, 1.0630000000000006)

    def test_23_function_2(self):
        Functions = Calculation(1)
        res = Functions.function_2()
        self.assertEqual(res, 5.197)

    def test_23_function_3(self):
        Functions = Calculation(1)
        res = Functions.function_3()
        self.assertEqual(res, 6.5847)

    def test_23_function_4(self):
        Functions = Calculation(1)
        res = Functions.function_4()
        self.assertEqual(res, 7.012)

    def test_24_function_1(self):
        Functions = Calculation(1.5)
        res = Functions.function_1()
        self.assertEqual(res, 8.329875)

    def test_24_function_2(self):
        Functions = Calculation(1.5)
        res = Functions.function_2()
        self.assertEqual(res, 14.840625000000001)

    def test_24_function_3(self):
        Functions = Calculation(1.5)
        res = Functions.function_3()
        self.assertEqual(res, 11.393550000000001)

    def test_24_function_4(self):
        Functions = Calculation(1.5)
        res = Functions.function_4()
        self.assertEqual(res, 10.517999999999999)

    def test_25_function_1(self):
        Functions = Calculation('-1.5')
        res = Functions.function_1()
        self.assertEqual(res, 'None')

    def test_25_function_2(self):
        Functions = Calculation('-1.5')
        res = Functions.function_2()
        self.assertEqual(res, 'None')

    def test_25_function_3(self):
        Functions = Calculation('-1.5')
        res = Functions.function_3()
        self.assertEqual(res, 'None')

    def test_25_function_4(self):
        Functions = Calculation('-1.5')
        res = Functions.function_4()
        self.assertEqual(res, 'None')



if __name__ == '__main__':
    unittest.main()
