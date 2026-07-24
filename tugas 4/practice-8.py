from collections import deque

queue = deque()

#pelanggan datang (Enqueue dari belakang)
queue.append('Andi')
queue.append('Budi')
queue.append('Citra')
queue.append('Dina')
deque(['Andi','Budi', 'Citra', 'Dina'])

print('Antian awal:', list(queue))
print ('Yang pertama di layani:', queue[0])
print ('--- Mulai melayani ---')

nomor = 1
while queue:
    pelanggan = queue.popleft()
    print(f'[{nomor}] Melayani: {pelanggan}')
    if queue:
        print(f'   Antrian: {list(queue)}')
    nomor += 1

print('Semua pelanggan telah dilayani!')
