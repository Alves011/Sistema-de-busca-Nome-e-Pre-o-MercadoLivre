from mercadolivre2 import Navegador
from tela import Telapy
from tela import janelaOK

#DEFININDO INICIO das pagina
pagina = 2
#INICIANDO A TELA DO PY
tela = Telapy()
ok = janelaOK()
#FUNCAO DO PYSIMPLEGUI
pesquisa = str(tela.pesquisa())
paginas = int(tela.pagina())

#INICIANDO NAVEGADOR
navegador = Navegador()

#FUNCAO
navegador.pesquisar_mercadoLivre(pesquisa)
navegador.PegarDados()
navegador.pular_cookies()
print("\n PAGINA 1\n")
navegador.manda_infomacao()

while(pagina <= paginas):
    print(f"\n PAGINA {pagina}\n")
    navegador.proxpag()
    navegador.PegarDados()
    navegador.manda_infomacao()
    pagina += 1

ok.janela()


