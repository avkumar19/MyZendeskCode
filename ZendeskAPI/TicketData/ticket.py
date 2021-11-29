from datetime import datetime
from typing import TypeVar, Generic, Dict
from database.configuration import *

T = TypeVar("T")

#DataStructure and Methods Used to Store and Display Tickets Information. 
class TicketData(Generic[T]):
    

    #Process Json and store in Structure
    def __init__(self, data: Dict[str, T]):
        try:
            self.id = data["id"] 
            self.created_at = data["created_at"]
            self.updated_at = data["updated_at"]
            self.subject = data["subject"]
            self.status = data["status"]
            self.requester_id = data["requester_id"]
            self.description = data["description"]
            self.tags = data["tags"]
        except KeyError:
            raise KeyError("Ticket Data could not get decoded properly.")

    #@Method: Concise Display of Ticket Information 
    def overview(self):
        output = "| {:^10} | {:^10} \t | {:^20} \t | {:^10} \t |"
        #output = "|| ID: {id_}, Status: {status} || Subject: {sub} || Requested at: {date_req}"
        subject = StringUtils.FormatString(self.subject, 35)
        try:
            creation_date = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y %H:%M:%S")
        except:
            creation_date = self.created_at
        formatted_output = output.format(self.id, self.status, subject, creation_date)
        return formatted_output

    #@Method: Detailed Display of Ticket Information
    def indepth(self):
        output = "ID: {0}\nStatus: {1}\nSubject: {2}\nDate: {3}\nRequester: {4}\nTags: {5}\n"
        try:
            creation_date = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y %H:%M:%S")
        except:
            creation_date = self.created_at
        Info = output.format(self.id, self.status, self.subject, creation_date, self.requester_id,self.tags)
        return Info, self.description
