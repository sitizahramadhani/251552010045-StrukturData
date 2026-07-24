import heapq
pq = []

#heappush (heap, (prioritas, data)) prioritas kecil paling penting
heapq.heappush(pq, (3, 'Task C -Rendah'))
heapq.heappush(pq, (1, 'Task A - URGENT'))
heapq.heappush(pq, (2, 'Task B - Medium'))

print('Pririty Queue:', pq)
#[(1, 'Task A-URGENT'), (3, 'Task C-Rendah'), (2, 'Task B-Medium')]
#Proses berdasarkan prioritas (terkecil keluar pertama)

while pq:
    prioritas, task = heapq.heappop(pq)
    print(f' [Prioritas {prioritas}] Proses: {task}')
    