# This file is part of cclib (http://cclib.github.io), a library for parsing
# and interpreting the results of computational chemistry packages.
#
# Copyright (C) 2006-2015 the cclib development team
#
# The library is free software, distributed under the terms of
# the GNU Lesser General Public version 2.1 or later. You should have
# received a copy of the license along with cclib. You can also access
# the full license online at http://www.gnu.org/copyleft/lgpl.html.

"""A library for parsing and interpreting results from computational chemistry packages.

The goals of cclib are centered around the reuse of data obtained from various
computational chemistry programs and typically contained in output files. Specifically,
cclib extracts (parses) data from the output files generated by multiple programs
and provides a consistent interface to access them.

Currently supported programs:
    ADF, Firefly, GAMESS(US), GAMESS-UK, Gaussian,
    Jaguar, Molpro, NWChem, ORCA, Psi, Q-Chem

Another aim is to facilitate the implementation of algorithms that are not specific
to any particular computational chemistry package and to maximise interoperability
with other open source computational chemistry and cheminformatic software libraries.
To this end, cclib provides a number of bridges to help transfer data to other libraries
as well as example methods that take parsed data as input.
"""

__version__ = "1.3.1"

from . import parser
from . import progress
from . import method
from . import bridge

# The test module can be imported if it was installed with cclib.
try:
    from . import test
except ImportError:
    pass
