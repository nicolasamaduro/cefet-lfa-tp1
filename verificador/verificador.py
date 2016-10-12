#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from leitorTexto import leitorTexto

if len(sys.argv) == 1:
	print 'Usar: verificador [GR de entrada]'
else:
    lt=leitorTexto(sys.argv[1])
    afn=lt.getGR()
    print afn