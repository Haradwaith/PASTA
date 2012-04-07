# Copyright (C) 2012 The PASTA team.
# See the README file for the exhaustive list of authors.
#
# This file is part of PASTA.
#
# PASTA is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PASTA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PASTA.  If not, see <http://www.gnu.org/licenses/>.



import connection as c

class PcapParser:
    """Parser for pcap files"""

    def __init__(self, keep_datagrams = True):
        # TODO: Add options

        self.keep_datagrams = keep_datagrams # Boolean

    def parse(self, file):
        """Parse the given pcap file and create Connection objects"""

        connections = []
        # TODO: Parse file

        return connections



if __name__ == '__main__':
    # TODO: Tests + logging
    pass
