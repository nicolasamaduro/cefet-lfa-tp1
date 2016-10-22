#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from leitorTexto import leitorTexto
from afn_to_afd import afn_to_afd

if len(sys.argv) == 1:
	print 'Usar: verificador [GR de entrada]'
else:
	lt = leitorTexto(sys.argv[1])
	estadosAFN, alfabeto, estadosIniciaisAFN, estadosFinaisAFN, afn = lt.getGR()

	print '**** AFN ****'
	print 'estados: ',estadosAFN
	print 'estadosIniciais: ',estadosIniciaisAFN
	print 'estadosFinais: ',estadosFinaisAFN
	print 'afn: ',afn,'\n'

	estadosAFD, estadoInicialAFD, estadosFinaisAFD, afd = afn_to_afd(estadosAFN, alfabeto, estadosIniciaisAFN, estadosFinaisAFN, afn)

	print '**** AFD ****'
	print 'estados: ',estadosAFD
	print 'estadoInicial: ',estadoInicialAFD
	print 'estadosFinais: ',estadosFinaisAFD
	print 'afd: ',afd