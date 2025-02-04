import tkinter as tk
from tkinter import filedialog, messagebox

class BlocoDeNotas:
    def _init_(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        self.root.geometry("600x400")

        # campo de texto
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")

        # barra de menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Menu Arquivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.file_menu.add_command(label="Novo", command=self.novo_arquivo, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Abrir", command=self.abrir_arquivo, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Salvar", command=self.salvar_arquivo, accelerator="Ctrl+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.root.quit, accelerator="Ctrl+Q")
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)

        # Menu Editar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.edit_menu.add_command(label="Desfazer", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Refazer", command=self.text_area.edit_redo, accelerator="Ctrl+Y")
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)

        # Atalhos de teclado que eu nunca vou usar 
        self.root.bind("<Control-n>", lambda event: self.novo_arquivo())
        self.root.bind("<Control-o>", lambda event: self.abrir_arquivo())
        self.root.bind("<Control-s>", lambda event: self.salvar_arquivo())
        self.root.bind("<Control-q>", lambda event: self.root.quit())

        # Variável para armazenar o caminho do arquivo
        self.file_path = None

    def novo_arquivo(self):
        self.text_area.delete("1.0", tk.END)
        self.file_path = None

    def abrir_arquivo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", ".txt"), ("Todos os Arquivos", ".*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, file.read())
            self.file_path = file_path

    def salvar_arquivo(self):
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get("1.0", tk.END))
        else:
            self.salvar_como()

    def salvar_como(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Arquivos de Texto", ".txt"), ("Todos os Arquivos", ".*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get("1.0", tk.END))
            self.file_path = file_path

if __name__ == "_main_":
    root = tk.Tk()
    app = BlocoDeNotas(root)
    root.mainloop()





