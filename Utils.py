# -*- coding: utf-8 -*-
#!/usr/bin/python
import time

def get_data():
	data = []	
	year, month, day = time.strftime("%Y,%m,%d").split(',')
	data.append('Dia:'+day)
	data.append(' Mes:'+month)
	data.append(' Ano:'+year)
	str1 = ''.join(data)
	return str1

def get_horas():
	horas = []	
	hour, minute = time.strftime("%H,%M").split(',')
	horas.append(hour+'h')
	horas.append(minute+'m')
	str1 = ''.join(horas)
	return str1

def get_tel(msg):
	i = False
	word = msg.split()
	#print word[4]
	tam = len(word)
	nome = word[tam-1]
	size = len(word[tam-1])
	for lin in open("tel.txt"):
	 if nome[:size-1] in lin:			
		i = True	
		msg = lin
			
	if i == True:
		return msg 
	else:
		return 'Este nome eu desconheço!'
