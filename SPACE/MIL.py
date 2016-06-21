#******************************************************************************
# (C) 2016, Stefan Korner, Austria                                            *
#                                                                             *
# The Space Python Library is free software; you can redistribute it and/or   *
# modify it under the terms of the GNU Lesser General Public License as       *
# published by the Free Software Foundation; either version 2.1 of the        *
# License, or (at your option) any later version.                             *
#                                                                             *
# The Space Python Library is distributed in the hope that it will be useful, *
# but WITHOUT ANY WARRANTY; without even the implied warranty of              *
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser     *
# General Public License for more details.                                    *
#******************************************************************************
# MIL Bus Simulation                                                          *
#******************************************************************************
from UTIL.SYS import Error, LOG, LOG_INFO, LOG_WARNING, LOG_ERROR
import SPACE.IF
import UTIL.TASK

###########
# classes #
###########

# =============================================================================
class MILbusImpl(SPACE.IF.MILbus):
  """Implementation of the MIL Bus"""
  # ---------------------------------------------------------------------------
  def __init__(self):
    """Initialise attributes only"""
    pass
  # ---------------------------------------------------------------------------
  def bcWriteSubAddress(self, rtAddress, subAddress, data):
    """
    Bus Controller: writes data to a sub-address
    implementation of SPACE.IF.MILbus.bcWriteSubAddress
    """
    pass
  # ---------------------------------------------------------------------------
  def bcReadSubAddress(self, rtAddress, subAddress):
    """
    Bus Controller: reads data from a sub-address
    implementation of SPACE.IF.MILbus.bcReadSubAddress
    """
    pass
  # ---------------------------------------------------------------------------
  def bcDatablockDistribtionRequest(self, rtAddress, dataBlock):
    """
    Bus Controller: initiate a datablock distribution
    implementation of SPACE.IF.MILbus.bcDatablockDistribtionRequest
    """
    LOG_INFO("MILbusImpl.bcDatablockDistribtionRequest(" + str(rtAddress) + ")", "MIL")
    UTIL.TASK.s_processingTask.notifyGUItask("RT " + str(rtAddress) + " DDB " + dataBlock)
    rts = SPACE.IF.s_milBusRemoteTerminals
    rts.notifyDatablockDistribution(rtAddress, dataBlock)
  # ---------------------------------------------------------------------------
  def rtWriteSubAddress(self, rtAddress, subAddress, data):
    """
    Remote Terminal: writes data to a sub-address
    implementation of SPACE.IF.MILbus.rtWriteSubAddress
    """
    pass
  # ---------------------------------------------------------------------------
  def rtReadSubAddress(self, rtAddress, subAddress):
    """
    Remote Terminal: reads data from a sub-address
    implementation of SPACE.IF.MILbus.rtReadSubAddress
    """
    pass
  # ---------------------------------------------------------------------------
  def rtDatablockAcquisitionRequest(self, rtAddress, dataBlock):
    """
    Remote Terminal: initiate a datablock acquisition
    implementation of SPACE.IF.MILbus.rtDatablockAcquisitionRequest
    """
    LOG_INFO("MILbusImpl.rtDatablockAcquisitionRequest(" + str(rtAddress) + ")", "MIL")
    UTIL.TASK.s_processingTask.notifyGUItask("RT " + str(rtAddress) + " ADB " + dataBlock)
    bc = SPACE.IF.s_milBusController
    bc.notifyDatablockAcquisition(rtAddress, dataBlock)

# =============================================================================
class MILbusControllerImpl(SPACE.IF.MILbusController):
  """Implementation of the MIL Bus Controller"""
  # ---------------------------------------------------------------------------
  def __init__(self):
    """Initialise attributes only"""
    pass
  # ---------------------------------------------------------------------------
  # external methods that are invoked via telecommands,
  # implementation of SPACE.IF.MILbusController
  def identify(self):
    LOG_INFO("MILbusControllerImpl.identify", "MIL")
    return True
  def selfTest(self):
    LOG_INFO("MILbusControllerImpl.selfTest", "MIL")
    return True
  def getSelfTestReport(self):
    LOG_INFO("MILbusControllerImpl.getSelfTestReport", "MIL")
    return True
  def reset(self):
    LOG_INFO("MILbusControllerImpl.reset", "MIL")
    return True
  def configure(self):
    LOG_INFO("MILbusControllerImpl.configure", "MIL")
    return True
  def configureFrame(self):
    LOG_INFO("MILbusControllerImpl.configureFrame", "MIL")
    return True
  def addInterrogation(self):
    LOG_INFO("MILbusControllerImpl.addInterrogation", "MIL")
    return True
  def discover(self):
    LOG_INFO("MILbusControllerImpl.discover", "MIL")
    return True
  def setupDistDatablock(self):
    LOG_INFO("MILbusControllerImpl.setupDistDatablock", "MIL")
    return True
  def start(self):
    LOG_INFO("MILbusControllerImpl.start", "MIL")
    return True
  def stop(self):
    LOG_INFO("MILbusControllerImpl.stop", "MIL")
    return True
  def forceFrameSwitch(self):
    LOG_INFO("MILbusControllerImpl.forceFrameSwitch", "MIL")
    return True
  def send(self):
    LOG_INFO("MILbusControllerImpl.send", "MIL")
    return True
  def setData(self):
    LOG_INFO("MILbusControllerImpl.setData", "MIL")
    return True
  def forceBusSwitch(self):
    LOG_INFO("MILbusControllerImpl.forceBusSwitch", "MIL")
    return True
  def injectError(self):
    LOG_INFO("MILbusControllerImpl.injectError", "MIL")
    return True
  def clearError(self):
    LOG_INFO("MILbusControllerImpl.clearError", "MIL")
    return True
  def activate(self):
    LOG_INFO("MILbusControllerImpl.activate", "MIL")
    return True
  def deactivate(self):
    LOG_INFO("MILbusControllerImpl.deactivate", "MIL")
    return True
  def dtd(self):
    LOG_INFO("MILbusControllerImpl.dtd", "MIL")
    return True
  # SPACE.IF.s_milBus.bcDatablockDistribtionRequest(0, "***BC***")
  # ---------------------------------------------------------------------------
  def notifyWriteSubAddress(self, rtAddress, subAddress, data):
    """
    A Remote Terminal has writen data to a sub-address
    implementation of SPACE.IF.MILbusController.notifyWriteSubAddress
    """
    pass
  # ---------------------------------------------------------------------------
  def notifyDatablockAcquisition(self, rtAddress, dataBlock):
    """
    A Remote Terminal has performed a datablock acquisition
    implementation of SPACE.IF.MILbusController.notifyDatablockAcquisition
    """
    LOG_INFO("MILbusControllerImpl.notifyDatablockAcquisition(" + str(rtAddress) + ")", "MIL")
    asw = SPACE.IF.s_applicatonSoftware
    asw.notifyMILdatablockAcquisition(rtAddress, dataBlock)

# =============================================================================
class MILbusRemoteTerminalsImpl(SPACE.IF.MILbusRemoteTerminals):
  """Implementation of the MIL Bus Remote Terminals"""
  # ---------------------------------------------------------------------------
  def __init__(self):
    """Initialise attributes only"""
    pass
  # ---------------------------------------------------------------------------
  # external methods that are invoked via telecommands,
  # implementation of SPACE.IF.MILbusRemoteTerminals
  def identify(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.identify", "MIL")
    return True
  def selfTest(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.selfTest", "MIL")
    return True
  def getSelfTestReport(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.getSelfTestReport", "MIL")
    return True
  def configure(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.configure", "MIL")
    return True
  def addResponse(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.addResponse", "MIL")
    return True
  def reset(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.reset", "MIL")
    return True
  def saEnable(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.saEnable", "MIL")
    return True
  def setupAcquDatablock(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.setupAcquDatablock", "MIL")
    return True
  def start(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.start", "MIL")
    return True
  def stop(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.stop", "MIL")
    return True
  def injectError(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.injectError", "MIL")
    return True
  def clearError(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.clearError", "MIL")
    return True
  def activate(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.activate", "MIL")
    return True
  def deactivate(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.deactivate", "MIL")
    return True
  def atr(self):
    LOG_INFO("MILbusRemoteTerminalsImpl.atr", "MIL")
    return True
  # SPACE.IF.s_milBus.rtDatablockAcquisitionRequest(1, "***RT***")
  # ---------------------------------------------------------------------------
  def notifyWriteSubAddress(self, rtAddress, subAddress, data):
    """
    The Bus Controller has writen data to a sub-address
    implementation of SPACE.IF.MILbusRemoteTerminals.notifyWriteSubAddress
    """
    pass
  # ---------------------------------------------------------------------------
  def notifyDatablockDistribution(self, rtAddress, dataBlock):
    """
    The Bus Controller has performed a datablock distribution
    implementation of SPACE.IF.MILbusRemoteTerminals.notifyDatablockDistribution
    """
    LOG_INFO("MILbusRemoteTerminalsImpl.notifyDatablockDistribution(" + str(rtAddress) + ")", "MIL")
    asw = SPACE.IF.s_applicatonSoftware
    asw.notifyMILdatablockDistribution(rtAddress, dataBlock)

#############
# functions #
#############
def init():
  # initialise singleton(s)
  SPACE.IF.s_milBus = MILbusImpl()
  SPACE.IF.s_milBusController = MILbusControllerImpl()
  SPACE.IF.s_milBusRemoteTerminals = MILbusRemoteTerminalsImpl()
