##################################################
#
# LCIO module
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class LCIO(BaseILC):
    """ Responsible for the LCIO software installation process. """

    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "LCIO", "lcio")
        
        self.reqfiles = [ ["lib/liblcio.a", "lib/liblcio.so", "lib/liblcio.dylib"] ]
        
        self.optmodules = [ "ROOT" ]

        # supported download types
        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'eutelescope'
        self.download.gitrepo = 'LCIO'

        self.envcmake["INSTALL_JAR"]="OFF"


    def compile(self):
        os.chdir( self.installPath+'/build' )
        
        if self.rebuild:
            tryunlink( "CMakeCache.txt" )

        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

        # execute ctests
        if( self.makeTests ):          
            if( os.system( "make tests && make test" ) != 0 ):
                self.abort( "failed to execute lcio tests" )


    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.svnurl = 'svn://svn.freehep.org/lcio'

        if( self.version  == 'HEAD' ):
            self.download.svnurl += '/trunk'
        elif '-pre' in self.version or '-dev' in self.version:
            self.download.svnurl += '/branches/' + self.version
        else:
            self.download.svnurl += '/tags/' + self.version


    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)
       
        if( self.mode == "install" ):
            # tests
            if( self.makeTests ):
                self.envcmake.setdefault("BUILD_LCIO_EXAMPLES","ON")
                self.envcmake.setdefault("BUILD_F77_TESTJOBS","ON")
              
        # check if java's required
        if ( self.cmakeBoolOptionIsSet( "LCIO_GENERATE_HEADERS" ) or self.cmakeBoolOptionIsSet( "INSTALL_JAR" ) ):
            self.addExternalDependency( ["Java"] )
                

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        self.env["LCIO"] = self.installPath
        # PATH
        self.envpath["PATH"].append( "$LCIO/tools" )
        if self.installPath != "/usr":
            self.envpath["PATH" ].append( "$LCIO/bin" )
            self.envpath["LD_LIBRARY_PATH"].append( "$LCIO/lib" )
        self.envpath["PYTHONPATH"].append( "$LCIO/python" )
        self.envpath["PYTHONPATH"].append( "$LCIO/python/examples" )
