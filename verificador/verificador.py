#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading
import atexit
from leitorTexto import leitorTexto
from AFN import AFN
from AFD import AFD

if len(sys.argv) == 1:
	print 'Usar: verificador [GR de entrada]'
else:
	lt = leitorTexto(sys.argv[1])
	afn = lt.getAFN()

	afn.toAFD()
	afd = afn.afd
	palavra=""

	while True:
		try:
			palavra = raw_input()
		except EOFError:
			sys.exit(0)
		if afd.verificaPalavra(palavra):
			print "Sim"
		else:
			print "Não"

