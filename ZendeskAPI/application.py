from database.ZendeskAPI import ZendeskAPI
from TicketData.ticket import TicketData
from database.configuration import *
import requests
from typing import List
import textwrap as tw

#Methods used for User Interface and service options from the Application
class UserInterface():

    def __init__(self, *args):

        if len(args)==0:
            self.ApiCaller = ZendeskAPI()
        else:
            self.ApiCaller = ZendeskAPI(args[0])
            
    # @Method: The default User view 
    def Index(self):

        Displayoptions = [1, 2, 3]
        DisplayService = ["Show all Tickets","Show ID based Ticket","Quit"]
        command = -1
        while command != Displayoptions[2]:
            print("SERVICE OPTIONS")
            print('─ ' * 53)
            for i in range(0,3):
                print("{0}. {1}\n".format(i+1,DisplayService[i]))
            
            print('─ ' * 53)

            prompt = "Select Service option: "
            err_msg = "Service not available please choose correct service option"
            command = InputUtils.ValidateInput(Displayoptions, prompt, err_msg)

            if command == Displayoptions[0]:
                self.ShowAllTickets()
            elif command == Displayoptions[1]:
                self.ShowTicketsWithId()

    # @Method: Displays all the tickest present in a page view by Calling Zendesk API's
    def ShowAllTickets(self):

        #Display Tickets on First Page (Max = 25)
        try: 
            TicketCnt = self.ApiCaller.GetTicketsCount()
            PageNo = 1
            TicketsData, CheckPrevPage, CheckNextPage = self.ApiCaller.GetPageWiseTickets(PageNo)
        except requests.exceptions.HTTPError as e:
            print(e)
            return returnCode[0]
        except requests.exceptions.RequestException:
            print("Zendesk API not reachable")
            return returnCode[0]

        if not TicketCnt: 
            print("No Tickets in Database")
            return "No Tickets in Database"
        
        print("\nTotal Ticktes in Database "+str(TicketCnt)+".")
        self.PrintOverviewHelper(TicketsData)
        print("Current Page No: "+str(PageNo)+", No of Tickets on Page: "+str(len(TicketsData))+".")
        print('─ ' * 53)
        
        #Navigation Logic
        PageNavigation = [0,1,2,3]
        while CheckPrevPage or CheckNextPage :
            SelectedNavigation = [PageNavigation[0],PageNavigation[3]]
            if CheckPrevPage:
                SelectedNavigation.append(PageNavigation[1])
                print("Select 1 to Navigate to previous Page")
            if CheckNextPage:
                SelectedNavigation.append(PageNavigation[2])
                print("Select 2 to Navigate to next Page")
            print("Select 3 to jump to specific Page")
            print("Select 0 to quit Navigation.")
            print('─ ' * 53)
            InputNav = InputUtils.ValidateInput(SelectedNavigation, "\nEnter a navigation option: ", "Please select a valid option.")
            try:
                if InputNav == PageNavigation[0]:
                    break
                elif InputNav == PageNavigation[1]:
                    PageNo -= 1
                    TicketsData, CheckPrevPage, CheckNextPage = self.ApiCaller.GetPageWiseTickets(PageNo)
                elif InputNav == PageNavigation[2]:
                    PageNo += 1
                    TicketsData, CheckPrevPage, CheckNextPage = self.ApiCaller.GetPageWiseTickets(PageNo)
                elif InputNav == PageNavigation[3]:
                    PageNo = InputUtils.IsValidPageNo("\nEnter Page No: ", TicketCnt, "Please select a valid Page No\n")
                    TicketsData, CheckPrevPage, CheckNextPage = self.ApiCaller.GetPageWiseTickets(PageNo)

            except requests.exceptions.HTTPError as e:
                print(e)
                return returnCode[0]
            except requests.exceptions.RequestException:
                print("Zendesk API is unavailable")
                return returnCode[0]
            print("\nTotal Ticktes in Database "+str(TicketCnt)+".")
            self.PrintOverviewHelper(TicketsData)
            print("Current Page No: "+str(PageNo)+", No of Tickets on Page: "+str(len(TicketsData))+".")
            print('─ ' * 53)
        
        return returnCode[1]

    # @Method: Displays all the tickest present in a page view by Calling Zendesk API's
    def ShowTicketsWithId(self):
        Id = InputUtils.IsValidID("Enter ticket id: ")   
        try:
            ticket = self.ApiCaller.GetTicketsWithId(Id)
        except requests.exceptions.HTTPError as e:
            print(e)
            return returnCode[0]
        except requests.exceptions.RequestException:
            print("Zendesk API not reachable")
            return returnCode[0]
        else:
            Info, discription = ticket.indepth()
            print('─ ' * 53)
            print(Info)
            print("Discription:")
            print(tw.fill(discription,70))
            return returnCode[1]

    def PrintOverviewHelper(self, TicketsData: List[TicketData]):
        
        #"|| ID: {ID}, Status: {status} || Subject: {sub} || Requested at: {date_req}"
        print('─ ' * 53)
        Header = "| {:^10} | {:^10} \t | {:^30} \t | {:^20} \t |"
        print(Header.format("ID","Status","Subject","Requested at"))
        print('─ ' * 53)
        for ticket in TicketsData:
            print(ticket.overview())
        print('─ ' * 53)

class Application():

    @staticmethod
    def main():
        print("\nWELCOME TO UW MADISON's ZENDESK TICKET VIEWER SYSTEM")
        print("@Developer : Avinash Kumar\n")
        display = UserInterface()
        display.Index()
        print("\nThanks for using the service!\n")

if __name__ == "__main__":
    Application.main()