#------------------------------------------------------------------------------
"""

Driver for a VersaTenn III Environmental Chamber Controller

"""
#------------------------------------------------------------------------------

import serial
import time

#------------------------------------------------------------------------------

ENQ = b'\x05' # Enquiry
ACK = b'\x06' # Acknowledge
NAK = b'\x15' # Neg. Acknowledge
STX = b'\x02' # Start of Text
ETX = b'\x03' # End of Text
EOT = b'\x04' # End of Transmission
DLE = b'\x10' # Data Link Escape
LF = b'\x0a' # Line Feed
CR = b'\x0d' # Carriage Return
XON = b'\x11' # X-On
XOFF = b'\x13' # X-Off

#------------------------------------------------------------------------------

def dump(msg, x):
  s = ['%02x' % c for c in x]
  print("%s: %s" % (msg, " ".join(s)))

#------------------------------------------------------------------------------

MINIMAL_TIME = 0.05 # 50ms

class vt3:
  """VersaTenn III Driver"""

  def __init__(self, port, baud=1200):
    """connect to and identify the versatenn 3 controller"""
    self.serial = serial.Serial(
      port=port,
      baudrate=baud,
      bytesize=serial.SEVENBITS,
      parity=serial.PARITY_ODD,
      stopbits=serial.STOPBITS_ONE,
      timeout=1.0)
    self.last_time = None

  def command(self, cmd, rsp=True):
    """send a command, receive a response"""
    dump("tx", cmd)
    # wait a minimal amount of time between commands
    if self.last_time is not None:
      delta = MINIMAL_TIME + self.last_time - time.time()
      if delta > 0.0:
        time.sleep(delta)
    self.last_time = time.time()
    # send the command to the serial port
    self.serial.write(cmd)
    # get a response if required
    if rsp:
      x = self.serial.read_until(terminator=ACK)
      dump("rx", x)
      return x
    return None

  def enquire(self):
    rsp = self.command(b'0' + ENQ)

  def get_sw_version(self):
    rsp = self.command(STX + b'? MDL' + ETX)


#------------------------------------------------------------------------------
