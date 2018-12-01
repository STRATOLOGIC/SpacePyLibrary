#******************************************************************************
# (C) 2018, Stefan Korner, Austria                                            *
#                                                                             *
# The Space Python Library is free software; you can redistribute it and/or   *
# modify it under under the terms of the MIT License as published by the      *
# Massachusetts Institute of Technology.                                      *
#                                                                             *
# The Space Python Library is distributed in the hope that it will be useful, *
# but WITHOUT ANY WARRANTY; without even the implied warranty of              *
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the MIT License    *
# for more details.                                                           *
#******************************************************************************
# Monitoring and Control (M&C) - Interface                                    *
#******************************************************************************
import string
from UTIL.SYS import Error, LOG, LOG_INFO, LOG_WARNING, LOG_ERROR
import UTIL.SYS

###########
# classes #
###########
# =============================================================================
class Configuration(object):
  """Configuration"""
  # ---------------------------------------------------------------------------
  def __init__(self):
    """Initialise the M&C relevant informations"""
    pass
  # ---------------------------------------------------------------------------
  def dump(self):
    """Dumps the status of the configuration attributes"""
    LOG_INFO("Monitoring an Control configuration", "CFG")

# =============================================================================
class TMmodel(object):
  """Telemetry model"""
  # ---------------------------------------------------------------------------
  def pushTMpacket(self, tmPacketDu, ertUTC):
    """consumes a telemetry packet"""
    pass

# =============================================================================
class TCmodel(object):
  """Telecommand model"""
  # ---------------------------------------------------------------------------
  def pushTCpacket(self, tcPacketDu):
    """consumes a telecommand packet"""
    pass

####################
# global variables #
####################
# configuration is a singleton
s_configuration = None
# telemetry model is a singleton
s_tmModel = None
# telecommand model is a singleton
s_tcModel = None
