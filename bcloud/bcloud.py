from pwn import *
context(arch='i386', os='linux')

sh = remote('127.0.0.1', 4000)
print s.recv()