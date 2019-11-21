#------------------------------------------------------------------------------
"""

Driver for a VersaTenn III Environmental Chamber Controller

"""
#------------------------------------------------------------------------------

import serial

#------------------------------------------------------------------------------

class vt3:
  """VersaTenn III Driver"""

  def __init__(self, port, baud=1200, timeout=1):
    """connect to and identify the versatenn 3 controller"""
    self.serial = serial.Serial(port, baud, timeout=timeout)



#------------------------------------------------------------------------------
