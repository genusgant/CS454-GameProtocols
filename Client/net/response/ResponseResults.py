from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseResults(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseResults - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_RESULTS) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_RESULTS) + '] String Response')
            print_exc()
