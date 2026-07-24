from collections import deque

# __Buat queue kosong_____________________
queue = deque()

# __ENQUEUE - tambah ke belakang (REAR)__________
queue.append('A')
queue.append('B')
queue.append('C')
print('Peek:', queue)

# __PEEK - lihat elemen DEPAN tanpa hapus_________
front = queue[0]
print('Peek:', front)

# __DEQUEUE - hapus dari DEPAN tanpa hapus_________
keluar = queue.popleft()
print('Dequeue:', keluar)
print('Queue:', queue)

# __IS EMPTY & SIZE___________________
print('Kosong?', len(queue) ==0)
print('Ukuran:', len(queue))
