# 📝 TO-DO LIST (Lista de Tarefas)

##  Visão Geral do Projeto

Este projeto é uma aplicação desktop de Lista de Tarefas (To-Do List) construída em Python utilizando a biblioteca **CustomTkinter** para uma interface gráfica moderna e responsiva. O objetivo é fornecer uma ferramenta simples e visualmente agradável para gerenciar tarefas diárias, com recursos de persistência de dados, visualização de calendário e alternância de temas.

##  Funcionalidades Principais

* **Adicionar Tarefas:** Insira novas tarefas na lista de forma rápida.
* **Remover Tarefas:** Exclua tarefas concluídas ou indesejadas com a opção de exclusão em massa (removendo todas as tarefas marcadas).
* **Persistência de Dados:** As tarefas e seus status de conclusão são salvos automaticamente em um arquivo CSV (`tarefas.csv`) ao fechar o aplicativo e carregados ao reabrir.
* **Relógio e Calendário:** Exibição em tempo real do relógio, data e mês/ano atual para melhor contextualização da lista.
* **Design Moderno:** Utiliza temas de cores personalizados e a biblioteca CustomTkinter para uma experiência de usuário aprimorada.
* **Modo Claro/Escuro:** Alternância fácil entre temas de cores (Light e Dark) através de um *switch*.

##  Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework GUI:** CustomTkinter
* **Módulos Padrão:** `time`, `calendar`, `csv`, `tkinter.messagebox`

##  Como Instalar e Rodar

Para executar este projeto localmente, siga os passos abaixo.

### Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.x recomendada).

### 1. Clonar o Repositório

```bash
git clone [https://github.com/YuriMacedoBolis/TO-DO-LIST.git](https://github.com/YuriMacedoBolis/TO-DO-LIST.git)
cd TO-DO-LIST
```
2. Instalar as DependênciasA principal dependência é o CustomTkinter.Bashpip install customtkinter
3. Configuração de Cores (Opcional)Este projeto utiliza um arquivo color_themes.json para definir cores personalizadas. Certifique-se de que este arquivo esteja no mesmo diretório que o main.py.
4. Executar a AplicaçãoBashpython main.py
