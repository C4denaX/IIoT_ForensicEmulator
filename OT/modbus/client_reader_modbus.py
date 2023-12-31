#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read_bit
# read 10 bits and print result on stdout

from pyModbusTCP.client import ModbusClient
import time
import random
SERVER_HOST = "10.0.0.2"
SERVER_PORT = 502
SERVER_U_ID = 1

c = ModbusClient()

# uncomment this line to see debug message
# c.debug(True)

# define modbus server host, port and unit_id
c.host(SERVER_HOST)
c.port(SERVER_PORT)
c.unit_id(SERVER_U_ID)

while True:
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, read coils (modbus function 0x01)
    if c.is_open():
        # read 10 bits at address 0, store result in regs list
        bits = c.read_coils(0, 4)
        # if success display registers
        if bits:
            print("bit ad #0 to 3: "+str(bits))

    # sleep Xs before next polling
    time.sleep(random.randint(1,6))

