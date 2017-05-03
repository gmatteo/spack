##############################################################################
# Copyright (c) 2017, Los Alamos National Security, LLC
# Produced at the Los Alamos National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *


class Pstreams(Package):
    """C++ wrapper for the POSIX.2 functions popen(3) and pclose(3)"""

    homepage = "http://pstreams.sourceforge.net/"
    url      = "https://superb-sea2.dl.sourceforge.net/project/pstreams/pstreams/Release%201.0/pstreams-1.0.1.tar.gz"

    version('1.0.1', '23199e3d12a644a2a0c66ec889d4c064')

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        install('pstream.h', prefix.include)
