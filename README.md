# iLCInstall

Installation script that enable a fully automated installation of EUTelescope and its dependencies, based on the installation of iLCSoft.

iLCInstall is distributed under the [GPLv3 License](http://www.gnu.org/licenses/gpl-3.0.en.html)

[![License](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)


## General Usage

The script can be called with the following syntax:
```
ilcsoft-install install.cfg [ -p, -i ]
```
options description:
* -p to preview installation environment
* -i to install the software

If called without options a summary of the installation is displayed. Examples of configuration files can be found under releases.


## Usage for EUTelescope:

* prerequisites: boost, mysql, java and cernlib installations are not supported in ilcinstall, these packages need to be available on the system, 
* paths can be changed in releases/release-versions.py

* for debian/ubuntu distributions you may need to install a few packages beforehand such as (TO BE CHECKED):
* apt-get install build-essential cmake subversion libmysqlclient-dev freeglut3-dev zlib1g-dev libqt4-dev cernlib-core-dev 
* default-jdk libxpm-dev libxmu-dev lesstif2-dev doxygen latex2html

STEPS TO FOLLOW...


## License and Copyright
Copyright (C), iLCInstall Authors

iLCInstall is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License long with this program.  If not, see <http://www.gnu.org/licenses/>.
