import PySimpleGUI as sg

class Telapy:
    def __init__(self):
        #layout
        sg.theme('Reddit')
        layout = [
            [sg.Image(r"C:\Users\bruno.alves\Desktop\request\MercadoLivre\logo_ml.jpg")],
            [[sg.Text('Paginas:'),sg.Spin([i for i in range(1,50)], initial_value=1,size=(10,15),key="pagina")]],
            [sg.Text("Pesquisa Item:"),sg.Input(key='pesquisa')],
            [sg.Button("ir !")]
        ]

        #janela
        self.janela = sg.Window("Mercado livre INFO",layout,size=(400,320),element_justification='center')
        #extrair dados
        self.evento, self.values  = self.janela.read()


    


    def pagina(self):
        self.pagina = self.values['pagina']
        return self.pagina

    def pesquisa(self):
        self.pesquisa = self.values['pesquisa']
        return self.pesquisa

class janelaOK:
    def janela(self):
            sg.theme('Reddit')
            layout1 = [
                [sg.Text("PESQUISA DE PRODUTOS CONCLUIDO !")],
                [sg.Button("OK")]

            ]
            self.janela = sg.Window("FINALIZADO !").layout(layout1)
            self.evento, self.valores = self.janela.read()
                    
#janelaOK().janelaOk()