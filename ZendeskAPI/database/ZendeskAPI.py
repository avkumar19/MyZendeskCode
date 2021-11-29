import requests
from TicketData.ticket import TicketData
from typing import List, Tuple
from database.configuration import ZendeskConfig

#Methods used to Call Zendesk API's and Process 
class ZendeskAPI():

    def __init__(self, *args):

        if len(args)==0:
            self.config = ZendeskConfig()
        else:
            self.config = args[0]

    def GetPageWiseTickets(self, PageNo: int) -> Tuple[List[TicketData], bool, bool]:
        """ Returns the tickets on a specific page and checks whether there is are previous/next pages. 
        :param PageNo: the page number 1-indexed of the page of tickets.
        :raises HTTPError: if a http error is encountered in the request, i.e. 401, 404, etc.
        :raises RequestException: a catch all exception for a request.
        :return: a tuple that contains the list of tickets, two booleans determining if there are previous/next pages.
        """

        tickets_url = self.config.allticketsAPI+str(PageNo)
        try:
            response = requests.get(tickets_url, auth=(self.config.username, self.config.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise

        response_json = response.json()
        tickets = []
        for entry in response_json["tickets"]:
            tickets.append(TicketData(entry))

        return tickets, response_json["previous_page"], response_json["next_page"]

    def GetTicketsCount(self) -> int:
        """ Returns the number of tickets in the account. 
        :raises HTTPError: if a http error is encountered in the request, i.e. 401, 404, etc.
        :raises RequestException: a catch all exception for a request.
        """

        tickets_url = self.config.ticketcntAPI
        try:
            response = requests.get(tickets_url, auth=(self.config.username, self.config.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise

        response_json = response.json()
        count = response_json["count"]["value"]
        return count

    def GetTicketsWithId(self, id_: int) -> TicketData:
        """ Returns the ticket from sending a get request to Zendesk API's tickets endpoint.
        This request will only fetch a ticket of specific id.
        :param id_: the id of the target ticket.
        :raises HTTPError: if the request encounters a 404, 401, etc. type error.
        :raises RequestException: a catch all for request exceptions.
        :return: a ticket representing the JSON data of the response.
        """
        
        ticket_url = self.config.ticketsIdAPI+str(id_)+".json"
        try:
            response = requests.get(ticket_url, auth=(self.config.username, self.config.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise

        response_json = response.json()
        entry = response_json["ticket"]
        
        return TicketData(entry)
        
