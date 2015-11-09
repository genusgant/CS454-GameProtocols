from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseDead(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseDead - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_DEAD) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_DEAD) + '] String Response')
            print_exc()
