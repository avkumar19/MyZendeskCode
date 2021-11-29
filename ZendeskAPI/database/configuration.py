from typing import List
import json

returnCode = ["FAILURE","SUCCESS"]

class ZendeskConfig():
    def __init__(self):
        file = open('cred.json')
        info = json.load(file)

        self.username = info["username"]+"/token"
        self.password = info["AccessToken"]
        self.allticketsAPI = "https://"+info["Domain"]+".zendesk.com/api/v2/tickets.json?per_page=25&page="
        self.ticketcntAPI = "https://"+info["Domain"]+".zendesk.com/api/v2/tickets/count.json?"
        self.ticketsIdAPI = "https://"+info["Domain"]+".zendesk.com/api/v2/tickets/"

#Some Utility metiods to Validate Inputs and Format the String 
class StringUtils():
    
    # @Method: Add Padding for Shorter String and remove Char for longer String for UI overview
    @staticmethod
    def FormatString(string: str, desired_length: int) -> str:

        if len(string) > desired_length:
            string = string[:desired_length-3]
            string += "..."
        else: 
            no_whitespaces = desired_length - len(string)
            string += " "*no_whitespaces
        return string


class InputUtils():

    # @Method: Validate Input and ask for Input untill its valid
    @staticmethod
    def ValidateInput(Displayoptions: List[int], prompt: str, err_msg: str) -> int:

        is_valid = False
        while not is_valid:
            try:
                command = int(input(prompt))
                if command not in Displayoptions:
                    raise Exception()
                is_valid = True
            except:
                print(err_msg) 
        return command

    # @Method: Validate Ticket ID
    @staticmethod
    def IsValidID(message: str) -> int:
        """ Prompts the user for a valid integer. 
        :param message: the prompting message that is displayed to the user.
        :return: the integer selected by the user.
        """
        is_valid = False
        while not is_valid:
            try:
                input_ = int(input(message))
                is_valid = True
            except ValueError as e:
                print(e) 
        return input_
        
