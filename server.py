# -*- coding: utf-8 -*-

import socket
import thread
from Utils import get_tel,get_horas,get_data

HOST = ''             
PORT = 6666           

def conectado(con,cliente):
	print 'Conectado por', cliente
	msg = con.send('Em que posso ajudar?')
	while True:
		msg = con.recv(1024)
		if not msg: break
		print cliente, msg

		if 'tel' in msg:
			ans = get_tel(msg)
			msg = con.send(ans)
			print ans

		elif 'num' in msg:
			ans = get_tel(msg)
			msg = con.send(ans)
			print ans
		
		elif 'núm' in msg:
			ans = get_tel(msg)
			msg = con.send(ans)
			print ans
	
		elif 'celu' in msg:
			ans = get_tel(msg)
			msg = con.send(ans)
			print ans

		elif 'horas' in msg:
			ans = get_horas()
			msg = con.send(ans)
			print ans

		elif 'data' in msg:
			ans = get_data()
			msg = con.send(get_data())
			print ans

		else:
			msg = con.send('Não compreendi sua solicitação!')
			print 'Palavra-chave não encontrada!'
					
	print 'Finalizando conexao do cliente', cliente
	con.close()
	thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
#print 'Esperando conexão Cliente Servidor'
while True:
	con, cliente = tcp.accept()
	thread.start_new_thread(conectado,tuple([con,cliente]))
	
tcp.close()


