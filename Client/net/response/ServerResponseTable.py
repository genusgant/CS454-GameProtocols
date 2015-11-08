from common.Constants import Constants

from net.response.ResponseRandomInt import ResponseRandomInt
from net.response.ResponseRandomString import ResponseRandomString
from net.response.ResponseRandomShort import ResponseRandomShort
from net.response.ResponseRandomFloat import ResponseRandomFloat
from net.response.ResponseLogin import ResponseLogin

class ServerResponseTable:
    """
    The ServerResponseTable contains a mapping of all responses for use
    with the networking component.
    """
    responseTable = {}

    def __init__(self):
        """Initialize the response table."""
        self.add(Constants.RAND_INT, 'ResponseRandomInt')
        self.add(Constants.RAND_STRING, 'ResponseRandomString')
        self.add(Constants.RAND_SHORT, 'ResponseRandomShort')
        self.add(Constants.RAND_FLOAT, 'ResponseRandomFloat')
        self.add(Constants.SMSG_AUTH, 'ResponseLogin')
        self.add(Constants.SMSG_DISCONNECT, 'ResponseLogin')
        self.add(Constants.SMSG_REGISTER, 'ResponseLogin')
        self.add(Constants.SMSG_FORGOT_PASSWORD, 'ResponseLogin')
        self.add(Constants.SMSG_CREATE_CHARACTER,'ResponseLogin')
        self.add(Constants.SMSG_CHAT, 'ResponseLogin')
        self.add(Constants.SMSG_MOVE, 'ResponseLogin')
        self.add(Constants.SMSG_POWER_UP, 'ResponseLogin')
        self.add(Constants.SMSG_POWER_PICKUP, 'ResponseLogin')
        self.add(Constants.SMSG_HEALTH, 'ResponseLogin')
        self.add(Constants.SMSG_ENTER_LOBBY, 'ResponseLogin')
        self.add(Constants.SMSG_ENTER_GAME_LOBBY, 'ResponseLogin')
        self.add(Constants.SMSG_ENTER_GAME_NAME, 'ResponseLogin')
        self.add(Constants.SMSG_CREATE_LOBBY, 'ResponseLogin')
        self.add(Constants.SMSG_PRIVATE_CHAT, 'ResponseLogin')
        self.add(Constants.SMSG_INVITE, 'ResponseLogin')
        self.add(Constants.SMSG_CAR_CHOICE, 'ResponseLogin')
        self.add(Constants.SMSG_CAR_PAINT, 'ResponseLogin')
        self.add(Constants.SMSG_CAR_TIRES, 'ResponseLogin')
        self.add(Constants.SMSG_GARAGE_PURCHASE, 'ResponseLogin')
        self.add(Constants.SMSG_RESULTS, 'ResponseLogin')
        self.add(Constants.SMSG_RANKINGS, 'ResponseLogin')
        self.add(Constants.SMSG_PRIZES, 'ResponseLogin')
        self.add(Constants.SMSG_COLLISION, 'ResponseLogin')
        self.add(Constants.SMSG_DEAD, 'ResponseLogin')
        self.add(Constants.SMSG_READY, 'ResponseLogin')
        self.add(Constants.SMSG_RENDER_CHARACTER, 'ResponseLogin')
        self.add(Constants.SMSG_REMOVE_CHARACTER, 'ResponseLogin')

    def add(self, constant, name):
        """Map a numeric response code with the name of an existing response module."""
        if name in globals():
            self.responseTable[constant] = name
        else:
            print 'Add Response Error: No module named ' + str(name)

    def get(self, responseCode):
        """Retrieve an instance of the corresponding response."""
        serverResponse = None

        if responseCode in self.responseTable:
            serverResponse = globals()[self.responseTable[responseCode]]()
        else:
            print 'Bad Response Code: ' + str(responseCode)

        return serverResponse
