class TextEditor:
    def __init__(self):
        self.content = ''
        self.undo_stack = []

    def write(self, teks):
        #Simpan state SEBELUM perubahan
        self.undo_stack.append(self.content)
        self.content += teks
        print(f'Tulis: {self.content}')

    def undo(self):
        if self.undo_stack:
            #kembalikan ke state sebelumnya
            self.content = self.undo_stack.pop()
            print(f'UNDO --> {self.content}')
        else:
            print('Tidak bisa undo lagi!')

editor = TextEditor()
editor.write('Helo')
editor.write('Dunia')
editor.write('!')
editor.undo()
editor.undo()
