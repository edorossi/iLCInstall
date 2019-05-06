##################################################
#
# LCCD module
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class LCCD(BaseILC):
    """ Responsible for the LCCD software installation process. """

    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "LCCD", "lccd")

        self.reqfiles = [ ["lib/liblccd.a", "lib/liblccd.so", "lib/liblccd.dylib"] ]

        self.reqmodules = [ "LCIO" ]

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'LCCD'

    def compile(self):
        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["LCCD"] = self.installPath

