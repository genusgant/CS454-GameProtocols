from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestPrizes(ServerRequest):


    def send(self, username = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_PRIZES)
            
            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.CMSG_PRIZES) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_PRIZES) + '] Int Request')
            print_exc()
