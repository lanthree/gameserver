import struct

a = 20
b = 400

str = struct.pack("ii", a, b)
print(len(str))
print(str)
print(repr(str))

aa,bb = struct.unpack("ii", str)
print(aa,bb)
