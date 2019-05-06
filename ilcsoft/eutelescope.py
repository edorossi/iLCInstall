##################################################
#
# EUTelescope module
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG
from util import *

class Eutelescope(MarlinPKG):
    """ Responsible for the Eutelescope installation process. """
    
    def __init__(self, userInput):
        # strip potential 'tags/' or 'branches/' parts from version string
        if os.path.basename(userInput):
            myversion=os.path.basename(userInput)
        else:
            myversion=os.path.dirname(userInput)
        MarlinPKG.__init__(self, "Eutelescope", myversion )

        self.reqmodules = [ "Marlin", "LCIO", "Eigen", "GEAR", "AIDA", "ROOT", "GBL" ]

        self.optmodules = [ "CLHEP", "GSL" ]
        
        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'eutelescope'
        self.download.gitrepo = 'eutelescope'


    def compile(self):
        # build MILLEPDEDEII
        if self.env.get( "MILLEPEDEII_VERSION", "" ):
            os.chdir( self.installPath+"/external" )
            if( os.system( "svn co https://svnsrv.desy.de/public/MillepedeII/%s millepede2/%s" % (self.env["MILLEPEDEII_VERSION"], self.env["MILLEPEDEII_VERSION"]) 
                           + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to build MILLEPEDE2!" )
            os.chdir( self.env[ "MILLEPEDEII" ] ) # needs to be defined in preCheckDeps (so it is written to build_env.sh)
            if( os.system( "make 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to build MILLEPEDE2!" )

        # build EUTELESCOPE
        os.chdir( self.installPath+"/build" )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make install ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

        # build EUDAQ
        if self.env.get( "EUDAQ_VERSION", "" ):
            os.chdir( self.installPath+"/external" )
            if( os.system( "git clone https://github.com/eudaq/eudaq eudaq/%s --branch %s" % (os.path.basename(self.env["EUDAQ_VERSION"]), os.path.basename(self.env["EUDAQ_VERSION"]))
                           + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to clone EUDAQ!" )

            os.chdir( self.env[ "EUDAQ" ] + "/build" ) # needs to be defined in preCheckDeps (so it is written to build_env.sh)

            if( os.system( "cmake -D BUILD_gui=OFF -D BUILD_main=OFF -D BUILD_nreader=ON .." + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to configure EUDAQ!" )

            if( os.system( "make install ${MAKEOPTS}" + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to build EUDAQ!" )


    def preCheckDeps(self):
        MarlinPKG.preCheckDeps(self)

        if self.env.get( "EUDAQ_VERSION", "" ):
            self.env["EUDAQ"] = self.installPath + "/external/eudaq/" + os.path.basename( self.env["EUDAQ_VERSION"] )

        if self.env.get( "MILLEPEDEII_VERSION", "" ):
            self.env["MILLEPEDEII"] = self.installPath + "/external/millepede2/" + self.env["MILLEPEDEII_VERSION"]
            self.envpath["PATH"].append( '$MILLEPEDEII' )


    def postCheckDeps(self):
        MarlinPKG.postCheckDeps(self)

        self.env["EUTELESCOPE"] = self.installPath
        self.envpath["PATH"].append( '$EUTELESCOPE/bin' )
        self.envpath["LD_LIBRARY_PATH"].append( '$EUTELESCOPE/lib' )
        # add libEutelProcessors.so
        self.parent.module('Marlin').envpath["MARLIN_DLL"].append( '$EUTELESCOPE/lib/libEutelProcessors.so' )
        # if EUDAQ is installed, adjust paths and Marlin libraries to be loaded
        if self.env.get( "EUDAQ_VERSION", "" ):
            self.envpath["LD_LIBRARY_PATH"].append( '$EUDAQ/lib' )
            self.parent.module('Marlin').envpath["MARLIN_DLL"].append( '$EUDAQ/lib/libNativeReader.so' )


    def setMode(self, mode):
        MarlinPKG.setMode(self, mode)
        
        self.download.type = "git-clone"
        self.download.svnurl = 'https://github.com/eutelescope/eutelescope'
