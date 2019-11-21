#------------------------------------------------------------------------------
"""

Driver for a VersaTenn III Environmental Chamber Controller

"""
#------------------------------------------------------------------------------

import serial

#------------------------------------------------------------------------------

ENQ = 5 # Enquiry
ACK = 6 # Acknowledge
NAK = 21 # Neg. Acknowledge
STX = 02 # Start of Text
ETX = 03 # End of Text
EOT = 04 # End of Transmission
DLE = 16 # Data Link Escape
LF = 10 # Line Feed
CR = 13 # Carriage Return
XON = 17 # X-On
XOFF = 19 # X-Off

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
      return self.serial.readline().strip()
    return None

  def get_sw_version(self):
    rsp = self.command(b'? MDL')












#------------------------------------------------------------------------------
