## Find PI to the Nth Digit 
# Enter a number and have the program generate π (pi) up to that many decimal places.
# Keep a limit to how far the program will go.
##
import unittest
import math

def pi_to_n_digits(digits):
    if digits < 0 or digits > 19:
        return False

    n = int(math.pi * (10 ** digits))
    n = n / (10 ** digits)

    return n

## TEST
class Test(unittest.TestCase):
    def test_pi_to_n_digits(self):
        self.assertEqual(pi_to_n_digits(10), 3.1415926535)
        self.assertEqual(pi_to_n_digits(5), 3.14159)
        self.assertEqual(pi_to_n_digits(0), 3)
        self.assertEqual(pi_to_n_digits(19), 3.1415926535897932384)

    def test_with_invalid_values(self):
        self.assertFalse(pi_to_n_digits(-1))
        self.assertFalse(pi_to_n_digits(20))

if __name__ == "__main__":
    unittest.main()