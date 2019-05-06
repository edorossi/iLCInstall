##################################################
#
# Eigen module
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class Eigen(BaseILC):
    """ Responsible for the Eigen configuration process. """

    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Eigen", "eigen")

        self.installSupport = True
        self.hasCMakeBuildSupport = True

        self.reqfiles = [ ["include/eigen3/Eigen/src/Core/Matrix.h", "include/eigen3/Eigen/Core","Eigen/src/Core/Matrix.h", "Eigen/Core" ] ]
	
        self.download.supportedTypes = [ "GitHub" ]
        self.download.gituser = 'eigenteam'
        self.download.gitrepo = 'eigen-git-mirror'


    def compile(self):
        """ compile EIGEN """
        os.chdir( self.installPath+'/build' )
	
	self.envcmake['CMAKE_INSTALL_PREFIX'] = self.installPath

        if self.rebuild:
            tryunlink( "CMakeCache.txt" )
	    
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
