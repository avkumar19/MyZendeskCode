import unittest
from testmethods import TestValidationMethods
from testUserInterface import TestUserInterface
from testticketData import TestTicket

class Tester(unittest.TestCase):
    """ Aggregates tests -- does not implement any additional itself. """

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestValidationMethods())
        suite.addTest(TestTicket())
        suite.addTest(TestUserInterface())
        return suite

if __name__ == "__main__":
    unittest.main(buffer=True)

