import unittest
from TicketData.ticket import TicketData
from database.configuration import *
import sys
import os
sys.path.insert(0, os.path.abspath('ZendeskAPI'))

import textwrap as tw

class TestTicket(unittest.TestCase):
    """ A group of unit tests for the methods contained within TicketData. """

    JsonTicketData1 = {
        "id": 125,
        "status": "open",
        "subject": "Valid Test Ticket Data 1",
        "created_at": "2019-12-31T07:31:06Z",
        "updated_at":"2021-11-23T16:40:16Z",
        "requester_id": "1549",
        "description": "This is the temp Discription of Test tickets used for Unit Testing",
        "tags":["est","incididunt","nisi"]
    }
    Ticket1 = TicketData(JsonTicketData1)

    JsonTicketData2 = {
        "id": 109,
        "status": "open",
        "subject": "Valid Test Ticket Data 2",
        "created_at": "2019-12-31T07:31:06Z",
        "updated_at":"2021-11-23T16:40:16Z",
        "requester_id": "23854720435",
        "description": "Temp Test Discription",
        "tags":["est","incididunt","nisi"]
    }
    Ticket2 = TicketData(JsonTicketData2)

    JsonErrorTicketData = {
        "id": 125,
        "created_at": "2019-12-31T07:31:06Z",
        "description": "This is the temp Discription of Test tickets used for Unit Testing ",
        "updated_at":"2021-11-23T16:40:16Z",
        "tags":["est","incididunt","nisi"]
    }

    def test_overview(self):

        output = self.Ticket1.overview()
        testCheck = "| {:^10} | {:^10} \t | {:^20} \t | {:^10} \t |"        
        resized_subject = StringUtils.FormatString(self.Ticket1.subject, 35) 
        testCheck = testCheck.format("125", "open", resized_subject, "31 Dec 2019 07:31:06")
        self.assertEqual(output, testCheck)

        output = self.Ticket2.overview()
        testCheck = "| {:^10} | {:^10} \t | {:^20} \t | {:^10} \t |"  
        resized_subject = StringUtils.FormatString(self.Ticket2.subject, 35) 
        testCheck = testCheck.format("109", "open", resized_subject, "31 Dec 2019 07:31:06")
        self.assertEqual(output,testCheck)

    def test_indepth(self):
        
        Info, discription = self.Ticket1.indepth()
        testCheck = "ID: {0}\nStatus: {1}\nSubject: {2}\nDate: {3}\nRequester: {4}\nTags: {5}\n"
        test1 = testCheck.format("125", "open", "Valid Test Ticket Data 1", "31 Dec 2019 07:31:06", "1549",["est","incididunt","nisi"])
        tempDis = "This is the temp Discription of Test tickets used for Unit Testing "
        self.assertEqual(Info,test1)
        self.assertEqual(discription,tw.fill(tempDis,70))
        
        Info, discription = self.Ticket2.indepth()
        test2 = testCheck.format("109", "open", "Valid Test Ticket Data 2", "31 Dec 2019 07:31:06", "23854720435",["est","incididunt","nisi"])
        tempDis = "Temp Test Discription"
        self.assertEqual(Info,test2)
        self.assertEqual(discription,tw.fill(tempDis,70))        
        
    def test_constructor(self):
        self.assertRaises(KeyError, TicketData, self.JsonErrorTicketData)

if __name__ == "__main__":
    unittest.main()