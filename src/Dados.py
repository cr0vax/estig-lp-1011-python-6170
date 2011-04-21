# -*- coding: utf-8 -*-

import sqlite3
from BaseDados import BaseDados

#---------------------------------------
# Classe responsável pelas operacoes de consultas à base de dados
# Autor: Bruno Moreira
# Número: 6170
#---------------------------------------

class Dados:
    
    
    # relação entre as colunas da BD e os parametros passados
    data_translator = {
        'year'                  : ('ano', 'fd.ano'),
        'teacher'               : ('id_docente', 'd.nome_completo'),
        'establishment'         : ('id_estabelecimento', 'e.designacao'),
        'category'              : ('id_categoria', 'ct.designacao'),
        'system'                : ('id_regime', 'r.designacao'),
        'establishment_type'    : ('id_tipo_estabelecimento','te.designacao'),
        'grade'                 : ('id_grau', 'g.designacao'),
        'course'                : ('id_curso', 'c.designacao')}

    # Statistics constructor
    def __init__(self):
        
        try:
            # initialize database connection
            self.conn = sqlite3.connect('rebides.db')
            self.cursor = self.conn.cursor()
            
        except Exception, e:
            print 'Got error %s' % e
        pass
    pass
    
    #---------------------------------------
    # Estatisticas segundo os parametros passados
    #
    #   years       - anos a que se refere a estatistica
    #   groupby     - campos pelos quais a estatistica deve ser agrupada
    #   count       - o que deve ser contado
    #---------------------------------------    
    def get_statistics(self, years, groupby, count):
        
        FD = 'fd.'
        
        sqlcount = FD + self.data_translator.get(count)[0]
        #sqlselect = self.data_translator.get(groupby[len(groupby)-1])[1]
        sqlselect = ','.join([str(FD + self.data_translator.get(i)[1]) for i in groupby])
        sqlgroupby = ','.join([str(FD + self.data_translator.get(i)[0]) for i in groupby])
        sqlwhere = ','.join([str(i) for i in years])
                
        cmd = """SELECT
                    {0}, COUNT(DISTINCT {1}) AS Total
                 FROM
                    Fichas_Docencia fd
                 INNER JOIN estabelecimentos e on
                    fd.id_estabelecimento = e.id_estabelecimento
                 INNER JOIN graus g on
                    fd.id_grau = g.id_grau
                 INNER JOIN tipos_estabelecimento te on
                    fd.id_tipo_estabelecimento = te.id_tipo_estabelecimento
                 INNER JOIN regimes r on
                    fd.id_regime = r.id_regime
                 INNER JOIN cursos c on
                    fd.id_curso = c.id_curso
                 INNER JOIN categorias ct on
                    fd.id_categoria = ct.id_categoria
                 INNER JOIN docentes d on
                    fd.id_docente = d.id_docente
                 WHERE
                    ano in ({2})
                 GROUP BY {3}""".\
                    format(sqlselect,
                           sqlcount,
                           sqlwhere,
                           sqlgroupby)
                        
        try:
            self.cursor.execute(cmd)
            
            r = self.cursor.fetchall()
            
            # retorna os dados
            return r
            
        except Exception, e:
            print 'Got error %s' % e
        pass
    pass
    
    #---------------------------------------
    # TODO: Listas segundo os parametros passados
    #---------------------------------------    
    def get_lists(self, select, where):
        
        FD = 'fd.'
        
        sqlselect = ','.join([str(FD + self.data_translator.get(i)[1]) for i in select])
        sqlwhere = ','.join([str(i) for i in where])
                
        cmd = """SELECT DISTINCT
                    {0}
                 FROM
                    Fichas_Docencia fd
                 INNER JOIN estabelecimentos e on
                    fd.id_estabelecimento = e.id_estabelecimento
                 INNER JOIN graus g on
                    fd.id_grau = g.id_grau
                 INNER JOIN tipos_estabelecimento te on
                    fd.id_tipo_estabelecimento = te.id_tipo_estabelecimento
                 INNER JOIN regimes r on
                    fd.id_regime = r.id_regime
                 INNER JOIN cursos c on
                    fd.id_curso = c.id_curso
                 INNER JOIN categorias ct on
                    fd.id_categoria = ct.id_categoria
                 INNER JOIN docentes d on
                    fd.id_docente = d.id_docente
                 WHERE
                    ano in ({1})""".\
                    format(sqlselect,
                           sqlwhere)
                        
        try:
            self.cursor.execute(cmd)
            
            r = self.cursor.fetchall()
            
            return r
            
        except Exception, e:
            print 'Got error %s' % e
        pass
    pass
    
    #---------------------------------------
    # Retorna os anos únicos da base de dados
    #---------------------------------------
    def get_years(self):
        
        cmd = """
            SELECT DISTINCT(ano) FROM fichas_docencia
            """
        
        try:
            self.cursor.execute(cmd)
            r = self.cursor.fetchall()
            
            return r
            
        except Exception, e:
            print 'An error ocurred while trying to fetch years %s' % e
        pass
        
    pass
    
    #---------------------------------------
    # Retorna os tipos de establecimento por ano
    #
    #   year - ano para o qual vão ser retornados os tipos de establecimento
    #---------------------------------------
    def get_establishment_types(self, year):
        
##        cmd = """
##            SELECT DISTINCT e.designacao, fd.id_tipo_estabelecimento
##            FROM fichas_docencia fd
##                INNER JOIN tipos_estabelecimento e on
##                fd.id_tipo_estabelecimento = e.id_tipo_estabelecimento
##            WHERE ano = {0}
##            """.format(year)

        #TODO: apagar o debaixo e descomentar o de cima
        cmd = """
            SELECT DISTINCT e.designacao, fd.id_tipo_estabelecimento
            FROM fichas_docencia fd
                INNER JOIN tipos_estabelecimento e on
                fd.id_tipo_estabelecimento = e.id_tipo_estabelecimento
            WHERE fd.id_tipo_estabelecimento = 1
            """
        
        try:
            self.cursor.execute(cmd)
            r = self.cursor.fetchall()
            
            return r
            
        except Exception, e:
            print 'An error ocurred while trying to fetch establishment types %s' % e
        pass
        
    pass
    
    #---------------------------------------
    # Retorna os establecimentos por ano e por tipo
    #
    #   year          - ano para o qual vão ser retornados os establecimentos
    #   establishment - código do establecimento
    #---------------------------------------
    def get_establishments(self, year, establishment):
        
        cmd = """
            SELECT DISTINCT e.designacao, fd.id_estabelecimento
            FROM fichas_docencia fd
                INNER JOIN estabelecimentos e on
                fd.id_estabelecimento = e.id_estabelecimento
            WHERE ano = {0} and id_tipo_estabelecimento = {1}
            """.format(year, establishment)
            
        try:
            self.cursor.execute(cmd)
            r = self.cursor.fetchall()
            
            return r
            
        except Exception, e:
            print 'An error ocurred while trying to fetch establishments %s' % e
        pass
        
    pass
    
    #---------------------------------------
    # Retorna os docentes por ano e estabelecimento
    #
    #   year          - ano para o qual vão ser retornados os docentes
    #   establishment - código do establecimento
    #---------------------------------------
    def get_teachers(self, year, establishment):
        
        cmd = """
            SELECT DISTINCT 
                    docente.nome_completo, 
                    grau.designacao, 
                    curso.designacao,
                    categoria.designacao,
                    regime.designacao
            FROM fichas_docencia fd
                INNER JOIN docentes docente on
                    fd.id_docente = docente.id_docente
                INNER JOIN graus grau on
                    fd.id_grau = grau.id_grau
                INNER JOIN cursos curso on
                    fd.id_curso = curso.id_curso
                INNER JOIN categorias categoria on
                    fd.id_categoria = categoria.id_categoria
                INNER JOIN regimes regime on
                    fd.id_regime = regime.id_regime
            WHERE fd.ano = {0} and fd.id_estabelecimento = {1}
            """.format(year, establishment)
        
        try:
            self.cursor.execute(cmd)
            r = self.cursor.fetchall()
            
            return r
            
        except Exception, e:
            print 'An error ocurred while trying to fetch teachers %s' % e
        pass
        
    pass
    
    #---------------------------------------
    # Pesquisa na base de dados as últimas 20 páginas do tipo desejado
    #
    #   type          - ano para o qual vão ser retornados os docentes
    #
    #   retorna um array com as páginas
    #---------------------------------------
    def get_pages(self, type):
        
        cmd = """
            SELECT * 
            FROM listas 
            WHERE tipo = {0}
            ORDER BY id
            LIMIT 20
            """.format(type)
        
        try:
            self.cursor.execute(cmd)
            r = self.cursor.fetchall()
            
            return r
            
        except Exception, e:
            print 'An error ocurred while trying to fetch pages %s' % e
        pass
        
    pass
    