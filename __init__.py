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
the display driver TM1637 controlling up to 6 pcs of 7-segment digital tubes
with decimal points or one or two colons.
The decode is compatible with TM1636 driver. However, it supports just 4 tubes
and does not have the keyboard scanning interface implemented.

NOTE:
The decoder has been tested on display modules with following configurations:
- 4 digital tubes with active decimal points for each tube without active colon
- 4 digital tubes with active colon with inactive decimal points

Althoug the driver TM1637 has keyboard scanning capability, it is not utilized
on display modules, which have no switches mounted.

"""

from .pd import Decoder
