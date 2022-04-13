from cmath import pi
import unittest
import met

class Testfunc(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(met.sum(3, 4), 7)
        self.assertEqual(met.sum(3, -4), -1)

    def test_mul(self):
        self.assertEqual(met.mul(3, 3), 9)

    def test_div(self):
        self.assertEqual(met.div(100, 5), 20)
        self.assertRaises(ValueError, met.div, 50, 0)

    def test_sub(self):
        self.assertEqual(met.sub(5, 2), 3)

    def test_leapyear(self):
        self.assertTrue(met.check_leap_year(2004), None)
        self.assertFalse(met.check_leap_year(2003), None)

    def test_area_of_circle(self):
        self.assertEqual(met.area_circle(14), 615.7521601035994)
    
    def test_volume_of_cube(self):
        self.assertAlmostEqual(met.cube_volume(2), 8)
        self.assertAlmostEqual(met.cube_volume(1), 1)
    def test_upper(self):
        self.assertEqual(met.upper_case("ZOO"), "ZOO")

    def test_split(self):
        s = 'Hello Skaehub'
        self.assertEqual(s.split(), ['Hello', 'Skaehub'])
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_concanc_names(self):
        self.assertEqual(met.concanc_names('erick','gege'), 'erick gege')


if __name__=="__main__":
    unittest.main()
        