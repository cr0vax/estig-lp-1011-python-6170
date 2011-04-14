# -*- coding: utf-8 -*-

from BaseDados import BaseDados
from Statistics import Statistics
from HttpServer import HttpServer

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
        st = Statistics()
        
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
        st.count_teachers(select, group_by, title)
        pass
    pass
    
    #---------------------------
    # Menu HTTP
    #---------------------------
    
    # Inicia o servidor http
    def http_start_server(self):
        self.http_server = HttpServer()
        
        self.http_server.start()
        pass
    pass
    
    # Para o servidor http
    def http_stop_server(self):
        #http_server = HttpServer()
        
        self.http_server.stop()
        pass
    pass
    