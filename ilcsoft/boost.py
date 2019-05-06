##################################################
#
# Boost module
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class Boost(BaseILC):
    """ Responsible for the Boost configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Boost", "boost")

        self.installSupport = False
        self.hasCMakeBuildSupport = False

        self.reqfiles = [ ["include/boost/version.hpp", "include/boost/spirit.hpp",
                           "boost/version.hpp", "boost/spirit.hpp"] ]

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "BOOST_ROOT" ]
        self.env["BOOST_ROOT"] = self.installPath

