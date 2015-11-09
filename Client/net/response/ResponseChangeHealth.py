from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeHealth(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseChangeHealth - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_HEALTH) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_HEALTH) + '] String Response')
            print_exc()
