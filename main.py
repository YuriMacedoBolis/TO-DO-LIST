import customtkinter as custom
from time import strftime , localtime
import calendar
import csv
from tkinter import messagebox 


custom.set_default_color_theme("color_theme.json")

class App(custom.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("600x450")
        self.resizable(False , False)
        self._set_appearance_mode("dark")
        self.title("Lista de Tarefas")
        self.lista_tarefas=[]
        self.widget_tarefas() # cria o lado das tarefas
        self.widget_calendario() # cria o lado do calendário e do horário
        self.carregar_csv()
        self.protocol("WM_DELETE_WINDOW", self.on_closing) #salva o csv ao fechar o app
        self.horario()
        
        #config modo claro/escuro
        self.switch_tema = custom.CTkSwitch(self , width=50,text="",command=self.alterar_tema)
        self.switch_tema.place(relx=0.95,rely=0.07,anchor="center")
        if custom.get_appearance_mode()=="dark":
            self.switch_tema.deselect()
        else:
            self.switch_tema.select()
     
     
    #FUNÇÕES DA CLASSE   
    def alterar_tema(self):
        if self.switch_tema.get()==1:
            custom.set_appearance_mode("dark")
        else:
            custom.set_appearance_mode("light")
     
    def carregar_csv(self):
        self.lista_tarefas = []   
        try:
            with open("tarefas.csv" , "r" , newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                
                try:
                    next(reader)
                except StopIteration:
                    messagebox.showinfo("Carregamento de Tarefas" , "Arquivo de Tarefas está vazio.")
                    return
                
                
                for linha in reader:
                    if len(linha)<2:
                        continue
                    
                    tarefa_texto = linha[0]
                    
                    status_concluida = int(linha[1])
                    
                    check = custom.CTkCheckBox(self.frame1, text=tarefa_texto)
                    check.pack(anchor="w", padx=10, pady=10)
                
                # Define o status de conclusão
                    if status_concluida == 1:
                        check.select()
                
                    self.lista_tarefas.append(check)
                
        except FileNotFoundError:
            messagebox.showerror("Erro de Arquivo" , "Arquivo tarefas.csv não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro ao Carregar",f"Ocorreu um erro ao carregar o CSV:\n{e}")
         
    def salvar_tarefas_csv(self):
        dados_para_salvar = []
        for check in self.lista_tarefas:
            tarefa_texto = check.cget("text")
            status_concluida = check.get()
            dados_para_salvar.append((tarefa_texto, status_concluida))
        
        try:
            with open("tarefas.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
            
                writer.writerow(["texto_da_tarefa", "status"]) 
            
                writer.writerows(dados_para_salvar)
            
        except Exception as e:
            messagebox.showerror("Erro ao Salvar" , f"Ocorreu um erro ao salvar o CSV:\n{e}")   
        
    def widget_tarefas(self):
        self.frame1 = custom.CTkScrollableFrame(self,width=250,height=250)
        self.frame1.place(relx=0.73,rely=0.4,anchor="center")
        
        self.caixa_entrada = custom.CTkEntry(self,width=270,height=40,font=("Arial",15),placeholder_text="tarefa...")
        self.caixa_entrada.place(relx=0.73 , rely=0.75 , anchor="center")
        
        self.botao_add = custom.CTkButton(self,width=100,height=40,text="Adicionar",command=self.adicionar)
        self.botao_add.place(relx=0.6, rely=0.9 , anchor="center")
        
        self.botao_remove = custom.CTkButton(self,width=100,height=40,text="Remover",command=self.excluir)
        self.botao_remove.place(relx=0.85, rely=0.9 , anchor="center")
    
    def adicionar(self):
        tarefa = self.caixa_entrada.get().strip()
        if tarefa:
            check = custom.CTkCheckBox(self.frame1,text=tarefa)
            check._text_label.configure(wraplength=220)
            check.pack(anchor="w",padx=10,pady=10) 
            self.lista_tarefas.append(check)
            self.caixa_entrada.delete(0,custom.END)
            
    def excluir(self):
        for check in self.lista_tarefas[:]:
            if check.get() == 1:
                check.destroy()
                self.lista_tarefas.remove(check)
            
    def widget_calendario(self):
        #RELOGIO , DATA E HORA
        self.label_relogio = custom.CTkLabel(self , width=250 , height=100 ,font=("Arial",40, "bold"))
        self.label_relogio.place(relx=0.25 , rely=0.23 , anchor="center")
        self.horario()

        self.brasilia = localtime()
        self.label_dia_mes_ano = custom.CTkLabel(self , width=250 , height=35,text=(strftime("%A %d/%m", self.brasilia)))
        self.label_dia_mes_ano.place(relx=0.25 , rely=0.4 , anchor="center")
        #CALENDARIO

        self.frame2 = custom.CTkFrame(self,width=250 , height=215)
        self.frame2.place(relx=0.25 , rely=0.7 , anchor="center")

        self.calendario = custom.CTkLabel(self.frame2,width=200 , height=200 ,text=(calendar.month(2025,(self.brasilia.tm_mon))),font=("Consolas" , 20 , "bold"))
        self.calendario.place(relx=0.5 , rely=0.5 , anchor="center")
        
    def horario(self):
        string = strftime("%H:%M:%S %p")
        self.label_relogio.configure(text=string)
        self.after(1000, self.horario)
        
    def on_closing(self):
        self.salvar_tarefas_csv()
        self.destroy()
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()