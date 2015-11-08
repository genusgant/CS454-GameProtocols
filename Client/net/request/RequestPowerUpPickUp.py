from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestPowerUpPickUp(ServerRequest):


    def send(self, username = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_POWER_PICKUP)
            
            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.CMSG_POWER_PICKUP) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_POWER_PICKUP) + '] Int Request')
            print_exc()
