# -*- coding: utf-8 -*-

from BaseDados import BaseDados
#from HttpServer import HttpServer

class Main:
    
    def __init__(self):
        self.bd = BaseDados()
        pass
    pass
    
    '''
    Collects data from a specified year
    
        ano - year of the data to be collected
    '''
    def collect_data(self, ano):
        print "STARTED COLLECTING DATA FOR YEAR", ano
        self.bd.criar_tabelas()
        self.bd.preencher_tipos_estabelecimento(ano)
        self.bd.preencher_tabelas_gerais(ano)
        print "FINISHED COLLECTING DATA FOR YEAR", ano
        pass
    pass