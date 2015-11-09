from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRenderCharacter(ServerResponse):

    def execute(self, conn, data):

        try:
            self.msg = data.getString()

            print "ResponseRenderCharacter - ", self.msg

            #self.log('Received [' + str(Constants.SMSG_RENDER_CHARACTER) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_RENDER_CHARACTER) + '] String Response')
            print_exc()
