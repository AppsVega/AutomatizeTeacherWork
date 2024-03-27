import customtkinter
from chromeDo import really_do

janela = customtkinter.CTk()
janela.geometry("600x500")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def obter_valores_e_executar(choice):
    CPF = cpf1.get()
    SENHA = senha1.get()
    DESC = desc1.get()
    PONTOS = pontos1.get()
    ALUNOSQNT = alunosqnt1.get()
    TURMA = choice
    WORKBOOK = workbook1.get()
    PAGINA = pagina1.get()
    really_do(CPF, SENHA, DESC, PONTOS, ALUNOSQNT, TURMA, WORKBOOK, PAGINA)

texto1 = customtkinter.CTkLabel(janela, text="Lembre que caso os dados preenchidos não estiverem\n corretos o programa pode não funcionar!", font=("Arial", 20, "bold"))
cpf1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui seu cpf: ", width=300)
senha1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui sua senha: ", width=300)
desc1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui o nome da avaliação: ", width=300)
pontos1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui a quantidade de pontos: ", width=300)
alunosqnt1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui a quantidade de Alunos: ", width=300)
options1 = customtkinter.CTkOptionMenu(janela, values=["OPT1","OPT2","OPT3","OPT4","OPT5","OPT6"], command=obter_valores_e_executar, width=600)
workbook1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui o caminho do arquivo XLSX: ", width=300)
pagina1 = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui o nome da Página do arquivo XLSX: ", width=300)
start1 = customtkinter.CTkButton(janela, text="COMEÇAR", command=obter_valores_e_executar, width=600)

texto1.pack(padx=10,pady=10)
cpf1.pack(padx=10,pady=10)
senha1.pack(padx=10,pady=10)
desc1.pack(padx=10,pady=10)
pontos1.pack(padx=10,pady=10)
alunosqnt1.pack(padx=10,pady=10)
workbook1.pack(padx=10,pady=10)
pagina1.pack(padx=10,pady=10)
start1.pack(padx=10,pady=10)
options1.pack(padx=10,pady=10)

janela.mainloop()
