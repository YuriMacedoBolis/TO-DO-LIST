# 📝 TO-DO LIST (Lista de Tarefas)

**Autor:** Yuri Macedo Bolis  
**Versão Atual:** 1.0.0  
**Repositório Público:** [https://github.com/YuriMacedoBolis/TO-DO-LIST](https://github.com/YuriMacedoBolis/TO-DO-LIST)

## 🎯 Contexto e Propósito

### O Problema Real
Profissionais que atuam diretamente com o cuidado e a gestão de rotinas, como babás e cuidadores, frequentemente lidam com uma sobrecarga de informações diárias (horários de medicação, refeições, atividades educativas, etc.). A falta de um sistema simples para registrar e acompanhar essas demandas pode gerar esquecimentos, estresse e falhas na gestão do tempo.

### Proposta da Solução
O TO-DO LIST é uma aplicação desktop leve e intuitiva focada em amenizar essa dor. A ferramenta permite o registro e acompanhamento rápido de tarefas diárias, garantindo que as atividades planejadas sejam concluídas e salvas de forma segura. A interface inclui um relógio e calendário integrados, facilitando a visualização dos compromissos no tempo.

### Público-Alvo
Babás, cuidadores, organizadores pessoais e qualquer profissional que necessite de uma gestão de rotina simplificada e visual.

---

## ⚙️ Funcionalidades Principais

* **Adicionar Tarefas:** Insira novas tarefas na lista de forma rápida.
* **Remover Tarefas:** Exclua tarefas concluídas ou indesejadas com a opção de exclusão em massa (removendo todas as tarefas marcadas).
* **Persistência de Dados:** As tarefas e seus status de conclusão são salvos automaticamente em um arquivo CSV (`tarefas.csv`) ao fechar o aplicativo e carregados ao reabrir.
* **Relógio e Calendário:** Exibição em tempo real do relógio, data e mês/ano atual para melhor contextualização da lista.
* **Design Moderno:** Utiliza temas de cores personalizados e a biblioteca CustomTkinter para uma experiência de usuário aprimorada.
* **Modo Claro/Escuro:** Alternância fácil entre temas de cores (Light e Dark) através de um *switch*.

---

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework GUI:** CustomTkinter
* **Módulos Padrão:** `time`, `calendar`, `csv`, `tkinter.messagebox`
* **Qualidade de Código e Testes:** `pytest` (Testes), `flake8` (Linting)

---

## 🚀 Como Instalar e Rodar

### Pré-requisitos
Certifique-se de ter o Python instalado (versão 3.x recomendada).

### 1. Clonar o Repositório

```bash
git clone [https://github.com/YuriMacedoBolis/TO-DO-LIST.git](https://github.com/YuriMacedoBolis/TO-DO-LIST.git)
cd TO-DO-LIST
```

### 2. Instalar as Dependências
As dependências do projeto estão declaradas no arquivo requirements.txt. Instale-as usando:

```
pip install -r requirements.txt
```

### 3. Executar a Aplicação

```
python main.py 
```

### 4. Qualidade e Automação
Instruções para rodar o Lint (Análise Estática)
Para verificar a padronização e qualidade do código, utilizamos o flake8. Para executar, rode no terminal:
```
flake8 main.py
```
Instruções para rodar os Testes
Os testes automatizados foram criados para validar os comportamentos centrais da aplicação. Para executá-los, utilize o pytest:
```
pytest tests/
```