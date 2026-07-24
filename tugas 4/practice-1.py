Stack = []
print('Awal:', Stack)

#push
Stack.append ('A')
Stack.append ('B')
Stack.append ('C')
print('setelah Push:', Stack)

#peek
top = Stack[-1]
print('peek:', top)

#pop
popped = Stack.pop()
print('Dipop:', popped)
print('Stack:', Stack)

#IS EMPTY & SIZE
print('kosong?', len(Stack)==0 )
print('ukuran:', len(Stack) )
