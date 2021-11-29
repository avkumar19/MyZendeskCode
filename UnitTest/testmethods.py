import unittest
from unittest import main, TestCase
from unittest.mock import patch
import os
import sys
sys.path.insert(0, os.path.abspath('ZendeskAPI'))
from database.configuration import *

#These set of Tescase Verify all the Validation check methods and String Format method
class TestValidationMethods(TestCase):

    def testFormatString(self):

        Space = 20*" "
        self.assertEqual("0123456789"+Space, StringUtils.FormatString("0123456789", 30))

        self.assertEqual("012345678901234567890123456789", StringUtils.FormatString("012345678901234567890123456789", 30))

        self.assertEqual("012345678901234567890123456...", StringUtils.FormatString("0123456789012345678901234567890123456789", 30))
        
        self.assertEqual(30, len(StringUtils.FormatString("0123456789012345678901234567890123456789", 30)))
    
    def testValidateInput(self):
        
        
        mock_input = ["2", "-1", "4"]
        with patch('builtins.input', side_effect=mock_input):
            dummy_options = [0, 4, 10]
            dummy_text = "A prompt message and an error message."
            result = InputUtils.ValidateInput(dummy_options, dummy_text, dummy_text)
            self.assertEqual(4, result)
        
        
        mock_input = ["2", "3", "4"]
        with patch('builtins.input', side_effect=mock_input):
            dummy_options = [2, 4, 10]
            dummy_text = "A prompt message and an error message."
            result = InputUtils.ValidateInput(dummy_options, dummy_text, dummy_text)
            self.assertEqual(2, result)

    def testIsValidID(self):

        
        mock_input = ["y", "7"]
        with patch('builtins.input', side_effect=mock_input):
            result = InputUtils.IsValidID("Mocking an input: ")
            self.assertEqual(7, result)

        
        mock_input = ["4.4", "9"]
        with patch('builtins.input', side_effect=mock_input):
            result = InputUtils.IsValidID("Mocking an input: ")
            self.assertEqual(9, result)
    
    def testIsValidPageNo(self):

        
        mock_input = ["y", "7","3"]
        err = "Please select a valid Page No"
        with patch('builtins.input', side_effect=mock_input):
            result = InputUtils.IsValidPageNo("Mocking an input: ",100,err)
            self.assertEqual(3, result)

        
        mock_input = ["4.4", "9"]
        with patch('builtins.input', side_effect=mock_input):
            result = InputUtils.IsValidPageNo("Mocking an input: ",1000,err)
            self.assertEqual(9, result)

if __name__ == "__main__":
    unittest.main(buffer=True)