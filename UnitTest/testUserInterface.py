import unittest
from unittest import main, TestCase
from unittest.mock import patch
import os
import sys
from io import StringIO
sys.path.insert(0, os.path.abspath('ZendeskAPI'))
from application import *

class TestUserInterface(unittest.TestCase):

    def testIndex(self):
        mock_input = ["1","0","2","13","3"]
        testdisplay = UserInterface()
        with patch('builtins.input', side_effect=mock_input),patch('sys.stdout', new=StringIO()) as fake_out:
            testdisplay.Index()
            self.assertIn("OPTIONS", fake_out.getvalue().strip())


    def testShowAllTicketsS(self):
        mock_input = ["2","1","0"]
        testdisplay = UserInterface()
        with patch('builtins.input', side_effect=mock_input):
            rtCode = testdisplay.ShowAllTickets()
            self.assertEqual(returnCode[1],rtCode)

    def testShowAllTicketsF(self):
        testdisplay = UserInterface()
        Config = ZendeskConfig()
        testdisplay = UserInterface(Config)
        Config.allticketsAPI = "https://zcccavkumar.zendesk.com/api/v2/tickets.json?per_page=25&page="
        rtCode = testdisplay.ShowAllTickets()
        self.assertEqual(returnCode[0],rtCode)
    

    def testShowTicketsWithIdS(self):
        mock_input = ["12"]
        testdisplay = UserInterface()
        with patch('builtins.input', side_effect=mock_input):
            rtCode = testdisplay.ShowTicketsWithId()
            self.assertEqual(returnCode[1],rtCode)
    def testShowTicketsWithIdF(self):
        mock_input = ["110"]
        testdisplay = UserInterface()
        with patch('builtins.input', side_effect=mock_input):
            rtCode = testdisplay.ShowTicketsWithId()
            self.assertEqual(returnCode[0],rtCode)

if __name__ == "__main__":
    unittest.main(buffer=True)



