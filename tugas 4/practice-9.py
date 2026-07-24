from collections import deque
d = deque([1, 2, 3])

#Tambah Ke kanan (seperti Queue enqqueue)
d.append(4)
#Hapus dari kiri (sperti Stack pop)
d.appendleft(0)
#Hapus daei kanan (sepertim Stack pop)
print(d.pop())
#Hapus dari kiri (seperti Queue dequeue)
print(d.popleft())

#ROTATE - geser semua elemen
d2 = deque([1,2,3,4,5])
d2.rotate(2)
print(d2)
d2.rotate(-1)
print(d2)
