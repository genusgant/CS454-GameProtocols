from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRemoveUser(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseRemoveUser - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_REMOVE_CHARACTER) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_REMOVE_CHARACTER) + '] String Response')
            print_exc()
