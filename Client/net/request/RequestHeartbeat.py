from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestHeartbeat(ServerRequest):


    def send(self, username = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.REQ_HEARTBEAT)
            
            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.REQ_HEARTBEAT) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.REQ_HEARTBEAT) + '] Int Request')
            print_exc()
