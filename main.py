import customtkinter
from tkinter import filedialog
from threading import Thread
from chromeDo import really_do

janela = customtkinter.CTk()
janela.geometry("600x500")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

listaT = ["1° DESENVOLVIMENTO DE SITEMAS-NIVELAMENTO","1° DESENVOLVIMENTO DE SITEMAS-MATEMÁTICA","1° EM INT 1-NIVELAMENTO","1° EM INT 1-MATEMÁTICA","2° EM INT 1-NIVELAMENTO","3° EM INT 1-NIVELAMENTO","3° EM INT 1-MATEMÁTICA"]

def import_file():
    return filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx"), ("Todos os Arquivos", "*.*")])

def obter_valores_e_executar(choice):
    CPF = cpf1.get()
    SENHA = senha1.get()
    DESC = desc1.get()
    PONTOS = pontos1.get()
    ALUNOSQNT = alunosqnt1.get()
    TURMA = choice
    WORKBOOK = import_file()

    t = Thread(target=really_do, args=(CPF, SENHA, DESC, PONTOS, ALUNOSQNT, TURMA, WORKBOOK))
    t.start()

texto1 = customtkinter.CTkLabel(janela, text="Lembre que caso os dados preenchidos não estiverem\n corretos o programa pode não funcionar!", font=("Arial", 20, "bold"))
cpf1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui seu cpf: ", width=300)
senha1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui sua senha: ", width=300)
desc1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui o nome da avaliação: ", width=300)
pontos1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui a quantidade de pontos: ", width=300)
alunosqnt1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui a quantidade de Alunos: ", width=300)
options1 = customtkinter.CTkOptionMenu(janela, values=listaT, command=obter_valores_e_executar, width=300)

texto1.pack(padx=10,pady=10)
cpf1.pack(padx=10,pady=10)
senha1.pack(padx=10,pady=10)
desc1.pack(padx=10,pady=10)
pontos1.pack(padx=10,pady=10)
alunosqnt1.pack(padx=10,pady=10)
options1.pack(padx=10,pady=10)

janela.mainloop()
