from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerUpPickUp(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponsePowerUpPickUp - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_POWER_PICKUP) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_PICKUP) + '] String Response')
            print_exc()
