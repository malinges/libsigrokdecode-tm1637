# -*- coding: utf-8 -*-
"""This file is part of the libsigrokdecode project.

Copyright (C) 2019 Libor Gabaj <libor.gabaj@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

DECODER:
This decoder stacks on top of the ``tmc`` protocol decoder and decodes
the display driver TM1637 controlling up to 6 pcs of 7-segment digits with
decimal points or one or two colons.

"""

from .pd import Decoder
