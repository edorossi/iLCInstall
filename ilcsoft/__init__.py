##################################################
#
# Initalisation
#
##################################################

# python looks in sys.path when importing modules
# sys.path[0] is the directory containing the script that was used to invoke the Python interpreter (where ilcsoft-install lives)
import sys
sys.path.append( sys.path[0] + '/ilcsoft' )

from ilcsoft import ILCSoft

# core software
from ilcutil import ILCUTIL
from lcio import LCIO
from lccd import LCCD
from gear import GEAR
from raida import RAIDA
from gbl import GBL

# marlin & friends
from marlinpkg import MarlinPKG
from marlinpkg import ConfigPKG
from marlin import Marlin

# EUTelescope
from eutelescope import Eutelescope

# cmake
from cmake import CMake

# external (with install support)
from clhep import CLHEP
from gsl import GSL

# external (without install support)
from root import ROOT
from java import Java
from eigen import Eigen
