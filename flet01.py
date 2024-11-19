 #Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.
import flet as ft

tarefas = []

def main(page: ft.page):
    page.bgcolor = ft.colors.LIGHT_BLUE
    page.title = 'Minha Agenda'

    def add_lista(evento):
        nova = nova_tarefa.value.strip()
        if nova:
            if nova not in tarefas:
                tarefas.append(nova)
                aprovacao.value = 'Tarefa adicionada com sucesso'
                lista.value = '\n'.join(tarefas)
            else:
                aprovacao.value = 'Esta tarefa ja foi adicionada' 
        else:
            aprovacao.value = 'Insira uma tarefa valida'              
        page.update()        
    
    

    nova_tarefa = ft.TextField(label=' Nova Terefa! ', color='#000000')
    
    aprovacao = ft.Text(value='', color='black')
    lista = ft.Text(value='',color='black')

    adicionar = ft.ElevatedButton(text='Adicionar', on_click=add_lista)



    page.add(nova_tarefa, adicionar, aprovacao,ft.Text('Tarefas', size=20, weight='bold'), lista)
ft.app(target=main)    