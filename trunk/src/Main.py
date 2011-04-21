# -*- coding: utf-8 -*-

from BaseDados import BaseDados
from Dados import Dados
from HttpServer import HttpServer
from Graphs import Graphs
from Html import Html
from CriarCSV import CriarCSV

#---------------------------------------
# Classe responsável pela ponta da GUI à camada aplicacional
# Autor: Bruno Moreira
# Número: 6170
#---------------------------------------
class Main:
    '''
    Collects data from a specified year
    
        ano - year of the data to be collected
    '''
    
    def collect_data(self, ano):
        bd = BaseDados()
        
        print "STARTED COLLECTING DATA FOR YEAR", ano
        bd.criar_tabelas()
        bd.preencher_tipos_estabelecimento(ano)
        bd.preencher_tabelas_gerais(ano)
        print "FINISHED COLLECTING DATA FOR YEAR", ano
        pass
    pass    
    
    #---------------------------------
    # Constroi as estatisticas
    #
    #   years       - anos para gerar estatisticas
    #   groupby     - campos pelos quais são agrupadas
    #   count       - o que contar
    #---------------------------------
    def get_statistics(self, years, groupby, count):
        bd = Dados()
        
        # transforma os elementos de years activos em string
        filtered_years = self.filter_active(years)

        # transforma os elementos de groupby activos em string
        filtered_groupby = self.filter_active(groupby)
        
        # constroi o título a dar ao gráfico
        title = """Total number of {0} for years {1} grouped by {2}""".\
                    format(count + 's',
                           ','.join(['200' + str(i) for i in filtered_years]),
                           ','.join([str(i) for i in filtered_groupby]))
        
        # se tudo estiver bem gera gráfico
        data = bd.get_statistics(filtered_years, filtered_groupby, count)
        
        # adiciona a página à bd
        db = BaseDados()
        file_name = db.insert_custom_list(title, 1)
        
        # Cria a página HTML com a estatistica
        html = Html()
        html.create_statistics_page(title, data, filtered_groupby, file_name)
        
        # cria o ficheiro CSV
        csv = CriarCSV()
        csv.escrita_csv(title, file_name, data)
            
        # gera o gráfico
        graph = Graphs(data, title)
        
        pass
    pass
    
    #--------------------------
    # Retorna uma lista com os itens que tenham a segunda posição a True
    #
    #   list_to_be_filtered - lista a ser filtrada
    #--------------------------
    def filter_active(self, list_to_be_filtered):
        
        # cria a lista a ser devolvida
        filtered_list = []
        
        # se o item for True adiciona à lista a ser devolvida
        for l in list_to_be_filtered:
            if l[1] == True:
                filtered_list.append(l[0])
            pass
        pass
        
        # altera a ordem da lista
        filtered_list.reverse()
            
        # retorna a lista filtrada
        return filtered_list
    pass
    
    #---------------------------
    # Menu estatisticas
    #---------------------------
    
    def get_lists(self, select, years):
        print "get_lists"
        # transforma os elementos de years activos em string
        filtered_years = self.filter_active(years)

        # transforma os elementos de groupby activos em string
        filtered_select = self.filter_active(select)
        
        # constroi o título a dar à lista
        title = """List of {0} for years {1}""".\
                    format(','.join([str(i) for i in filtered_select]),
                           ','.join(['200' + str(i) for i in filtered_years]))
        
        # retorna os dados da base de dados
        bd = Dados()
        data = bd.get_lists(filtered_select, filtered_years)
        
        # adiciona a página à bd
        db = BaseDados()
        file_name = db.insert_custom_list(title, 0)
        
        # cria o ficheiro CSV
        csv = CriarCSV()
        csv.escrita_csv(title, file_name, data)
        
        # Cria a página HTML com a estatistica
        html = Html()
        html.create_lists_page(title, data, filtered_select, file_name)
        pass
    pass
    
    
    #---------------------------
    # Menu HTTP
    #
    #   generate_html   - if true generates HTML
    #---------------------------
    
    # Inicia o servidor http
    def http_start_server(self, generate_html):
        
        # inicia o servidor
        self.http_server = HttpServer()
        self.http_server.start()
        
        if generate_html == True:
            
            # cria páginas
            html = Html()
            html.create_index()
        pass
    pass
    
    # Pára o servidor http
    def http_stop_server(self):
        self.http_server.stop()
        pass
    pass
    