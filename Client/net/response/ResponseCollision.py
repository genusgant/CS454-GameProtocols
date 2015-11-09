from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCollision(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseCollision - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_COLLISION) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_COLLISION) + '] String Response')
            print_exc()
