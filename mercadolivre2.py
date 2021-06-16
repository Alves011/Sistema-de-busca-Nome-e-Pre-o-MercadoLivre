from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

class Navegador:
    def __init__(self):
        options = Options()
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.56 Safari/537.36"
        options.add_argument(f'user-agent={userAgent}')
        options.headless = True
        self.navegador = webdriver.Chrome(options=options, executable_path=r'C:\Users\bruno.alves\Desktop\request\MercadoLivre\chromedriver')

    def pular_cookies(self):
        self.navegador.find_element_by_xpath('//*[@class="nav-cookie-disclaimer__button"]').click()

    def pesquisar_mercadoLivre(self,produto):
        self.url = f"https://lista.mercadolivre.com.br/{str(produto)}_DisplayType_LF"
        self.navegador.get(self.url)

    def PegarDados(self):
        #TITULOS DE PRODUTOS
        self.titulos = self.navegador.find_elements_by_class_name('ui-search-item__title')
        #VALOR DOS PRODUTOS valor total
        self.valores = self.navegador.find_elements_by_xpath('//*[@class="ui-search-layout__item"]/div/div/div/div/div/div/div/div/span/span/span[2]')

        #VALOR DOS PRODUTO (CENTAVOS) não consigui incliuir
        self.centavos = self.navegador.find_elements_by_xpath('//*[@class="ui-search-layout__item"]/div/div/div/div/div/div/div/div/span/span/span[4]')

    
    def manda_infomacao(self):
        date = []
        df = pd.DataFrame(data=date,columns=['NOME PRODUTO','VALOR PRODUTO'])
        for self.titulo,self.valor in zip(self.titulos,self.valores):
            novo = [f'{self.titulo.text}',f'{self.valor.text}']
            df.loc[len(df)] = novo

        df.to_excel('dados_mercadolivre.xlsx',index=False)
        print(df)

    def proxpag(self):
        self.proxPag = self.navegador.find_element_by_xpath('//*[@class="andes-pagination__button andes-pagination__button--next"]/a[1]').click()


    def pegando_info_prox_pag(self,):
        self.url = self.link
        self.navegador.get(self.url)
    def main(self,pesquisa):
        pass

