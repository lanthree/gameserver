#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct


buf_size = 1024 * 1024 * 48
recv_size = 8192
buf = memoryview(bytearray(buf_size))
		head = struct.Struct("!BHBH16s6s")


		s = socket.socket()
		s.bind(('', 41811))
		s.listen(5)

		conn, addr = s.accept()
		print "connected:", addr


		read_idx = 0
		write_idx = 0

		while True:

		    while write_idx < read_idx + head.size:
			        write_idx += conn.recv_into(buf[write_idx:write_idx+recv_size])

		    prefix, length, command, server_id, client_ip, client_mac = head.unpack_from(buf[read_idx:])
		    read_idx += head.size

			    if prefix != 2:
				        raise ValueError("prefix %s != 2" % (prefix,))

						    if command != 1:
							        read_idx += length - head.size
									        continue

											    while write_idx < read_idx + length:
												        write_idx += conn.recv_into(buf[write_idx:write_idx+recv_size])

		    t = struct.unpack_from("!" + "I" * ((length - head.size - 1) / 4) + "B", buf[read_idx:])
			    read_idx += length - head.size

				    if t[-1] != 3:
					        print prefix, length, command, server_id, client_ip, client_mac
							        print t
									        raise ValueError("prefix %s != 3" % (t[-1],))

											    if buf_size - write_idx < recv_size:
												        buf[:write_idx-read_idx] = buf[read_idx:write_idx]
														        write_idx = write_idx - read_idx
																        read_idx = 0

