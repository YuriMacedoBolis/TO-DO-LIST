import customtkinter as custom
from time import strftime, localtime
import calendar
import csv
import os
from tkinter import messagebox

custom.set_default_color_theme("color_theme.json")


def ler_tarefas_csv(caminho_arquivo):
    tarefas = []
    if not os.path.exists(caminho_arquivo):
        return tarefas

    with open(caminho_arquivo, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            next(reader)  # Pula o cabeçalho
        except StopIteration:
            return tarefas

        for linha in reader:
            if len(linha) >= 2:
                # A LÓGICA CORRETA AQUI: linha é o texto, linha[1] é o número
                texto = str(linha[0])
                status = int(linha[1])
                tarefas.append((texto, status))

    return tarefas


def salvar_tarefas_csv_logica(caminho_arquivo, dados):
    with open(caminho_arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["texto_da_tarefa", "status"])
        writer.writerows(dados)


class App(custom.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x450")
        self.resizable(False, False)
        self._set_appearance_mode("dark")
        self.title("Lista de Tarefas")
        self.lista_tarefas = []
        self.widget_tarefas()
        self.widget_calendario()
        self.carregar_csv()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.horario()

        self.switch_tema = custom.CTkSwitch(
            self, width=50, text="", command=self.alterar_tema
        )
        self.switch_tema.place(relx=0.95, rely=0.07, anchor="center")

        if custom.get_appearance_mode() == "dark":
            self.switch_tema.deselect()
        else:
            self.switch_tema.select()

    def alterar_tema(self):
        if self.switch_tema.get() == 1:
            custom.set_appearance_mode("dark")
        else:
            custom.set_appearance_mode("light")

    def carregar_csv(self):
        self.lista_tarefas = []
        try:
            dados = ler_tarefas_csv("tarefas.csv")
            for tarefa_texto, status_concluida in dados:
                check = custom.CTkCheckBox(self.frame1, text=tarefa_texto)
                check.pack(anchor="w", padx=10, pady=10)
                if status_concluida == 1:
                    check.select()
                self.lista_tarefas.append(check)
        except Exception as e:
            msg = f"Ocorreu um erro ao carregar o CSV:\n{e}"
            messagebox.showerror("Erro ao Carregar", msg)

    def salvar_tarefas_csv(self):
        dados_para_salvar = []
        for check in self.lista_tarefas:
            dados_para_salvar.append((check.cget("text"), check.get()))
        try:
            salvar_tarefas_csv_logica("tarefas.csv", dados_para_salvar)
            print(f"""
                  Tarefas salvas com sucesso: {len(dados_para_salvar)} itens.
                  """)
        except Exception as e:
            msg = f"Ocorreu um erro ao salvar o CSV:\n{e}"
            messagebox.showerror("Erro ao Salvar", msg)

    def widget_tarefas(self):
        self.frame1 = custom.CTkScrollableFrame(self, width=250, height=250)
        self.frame1.place(relx=0.73, rely=0.4, anchor="center")

        self.caixa_entrada = custom.CTkEntry(
            self, width=270, height=40, font=("Arial", 15),
            placeholder_text="tarefa..."
        )
        self.caixa_entrada.place(relx=0.73, rely=0.75, anchor="center")

        self.botao_add = custom.CTkButton(
            self, width=100, height=40, text="Adicionar",
            command=self.adicionar
        )
        self.botao_add.place(relx=0.6, rely=0.9, anchor="center")

        self.botao_remove = custom.CTkButton(
            self, width=100, height=40, text="Remover", command=self.excluir
        )
        self.botao_remove.place(relx=0.85, rely=0.9, anchor="center")

    def adicionar(self):
        tarefa = self.caixa_entrada.get().strip()
        if tarefa:
            check = custom.CTkCheckBox(self.frame1, text=tarefa)
            check._text_label.configure(wraplength=220)
            check.pack(anchor="w", padx=10, pady=10)
            self.lista_tarefas.append(check)
            self.caixa_entrada.delete(0, custom.END)
            self.salvar_tarefas_csv()

    def excluir(self):
        for check in self.lista_tarefas[:]:
            if check.get() == 1:
                check.destroy()
                self.lista_tarefas.remove(check)
        self.salvar_tarefas_csv()

    def widget_calendario(self):
        self.label_relogio = custom.CTkLabel(
            self, width=250, height=100, font=("Arial", 40, "bold")
        )
        self.label_relogio.place(relx=0.25, rely=0.23, anchor="center")

        self.brasilia = localtime()
        texto_data = strftime("%A %d/%m", self.brasilia)
        self.label_dia_mes_ano = custom.CTkLabel(
            self, width=250, height=35, text=texto_data
        )
        self.label_dia_mes_ano.place(relx=0.25, rely=0.4, anchor="center")

        self.frame2 = custom.CTkFrame(self, width=250, height=215)
        self.frame2.place(relx=0.25, rely=0.7, anchor="center")

        ano_atual = self.brasilia.tm_year
        mes_atual = self.brasilia.tm_mon
        texto_cal = calendar.month(ano_atual, mes_atual)

        self.calendario = custom.CTkLabel(
            self.frame2, width=200, height=200, text=texto_cal,
            font=("Consolas", 20, "bold")
        )
        self.calendario.place(relx=0.5, rely=0.5, anchor="center")

    def horario(self):
        string_hora = strftime("%H:%M:%S %p")
        self.label_relogio.configure(text=string_hora)

        string_data = strftime("%A %d/%m")
        self.label_dia_mes_ano.configure(text=string_data)

        self.after(1000, self.horario)

    def on_closing(self):
        self.salvar_tarefas_csv()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
