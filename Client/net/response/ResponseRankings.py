from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRankings(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseRankings - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_RANKINGS) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_RANKINGS) + '] String Response')
            print_exc()
