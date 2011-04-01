# -*- coding: utf-8 -*-

from BaseDados import BaseDados

class Main:
    
    def __init__(self):
        self.bd = BaseDados()
        pass
    pass    
    
    def collect_data(self, ano):
        self.bd.criar_tabelas()
        self.bd.preencher_tipos_estabelecimento(ano)
        self.bd.preencher_tabelas_gerais(ano)
        pass
    pass