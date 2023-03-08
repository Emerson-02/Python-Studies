import PySimpleGUI as sg 

# Criar as janelas e estilos(layout)
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)
def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox(
            'Pizza Calabresa', key='pizza2')],
            [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)
# Criar as janelas iniciais
janela1, janela2 = janela_login(), None
# Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para a próxima 
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza Calabresa')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado uma Pizza Pepperoni')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza Calabresa')

    # Quando queremos voltar para a janela anterior
# Lógica do que deve acontecer ao clicar os botões