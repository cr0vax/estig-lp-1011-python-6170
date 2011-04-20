# -*- coding: utf-8 -*-

from BaseDados import BaseDados
from Dados import Dados
from HttpServer import HttpServer
from Graphs import Graphs
from Html import Html

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
    
    
    #---------------------------------------
    # Define os parametros para consultar na BD
    # as stats relativas aos professores
    #
    #   which_stat - 
    def get_teacher_stats(self, which_stat):
        st = Dados()
        
        consultas = {
            'tnotithespy'   : ["ano", "ano", "Total number of teachers in the higher education system per year"],
            'tnotpiapy'     : ["ano, estabelecimentos.designacao", "ano, id_estabelecimento", "Total number of teachers per institution and per year"],
            'tnotpdapy'     : ["ano, graus.designacao", "ano, id_grau", "Total number of teachers per degree and per year"],
            'tnotpdpeapy'   : ["ano, estabelecimentos.designacao, graus.designacao", "ano, id_estabelecimento, id_grau", "Total number of teachers per degree, per establishment and per year"]
        }
        
        # valida quais os parametros para a stat escolhida
        #select, group_by = consultas[which_stat]()
        select, group_by, title = consultas.get(which_stat)
        
        # retorna os dados da consulta efectuada
        data = st.count_teachers(select, group_by)
        
        return data, title
    
        pass
    pass

    #---------------------------------
    # Constroi as estatisticas
    #---------------------------------
    def get_statistics(self, years, groupby, count):
        print "get_statistics"
        bd = Dados()
        
        # transforma os elementos de years activos em string
        filtered_years = self.filter_active(years)

        # transforma os elementos de groupby activos em string
        filtered_groupby = self.filter_active(groupby)
        
        # se tudo estiver bem gera gráfico
        data = bd.statistics(filtered_years, filtered_groupby, count)
        
        # constroi o título a dar ao gráfico
        title = """Total number of {0} for years {1} groupped by {2}""".\
                    format(count + 's',
                           ','.join(['200' + str(i) for i in filtered_years]),
                           ','.join([str(i) for i in filtered_groupby]))
        
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
    def make_teachers_graph(self, which_stat):
        
        # trata os dados
        data, title = self.get_teacher_stats(which_stat)
        
        # gera gráfico com os dados
        graph = Graphs(data, title)
        
        pass
    pass
    
    def get_lists(self):
        lists(self, select, where)
        pass
    pass
    
    
    #---------------------------
    # Menu HTTP
    #---------------------------
    
    # Inicia o servidor http
    def http_start_server(self):
        
        # inicia o servidor
        self.http_server = HttpServer()
        self.http_server.start()
        
        # cria páginas
        html = Html()
        html.create_pages()
        pass
    pass
    
    # Pára o servidor http
    def http_stop_server(self):
        self.http_server.stop()
        pass
    pass
    