# -*- coding: utf-8 -*-

import sqlite3

class Dados:
    
    
    # relação entre as colunas da BD e os parametros passados
    data_translator = {
        'year'                  : 'ano',
        'teacher'               : 'id_docente',
        'establishment'         : 'id_estabelecimento',
        'category'              : 'id_categoria',
        'system'                : 'id_regime',
        'establishment_type'    : 'id_tipo_estabelecimento',
        'grade'                 : 'id_grau',
        'course'                : 'id_curso'}

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
    # Estatisticas sobre professores
    #---------------------------------------    
    def count_teachers(self, select, group_by):
        
        group_by = group_by.replace(" ", "")
        group_by = group_by.replace(",", ",fd.")
        
        cmd = """SELECT 		{0}, COUNT(DISTINCT id_docente) AS TotalDocentes
                 FROM		    Fichas_Docencia fd
                    INNER JOIN estabelecimentos on
                        estabelecimentos.id_estabelecimento = fd.id_estabelecimento
                    INNER JOIN graus on
                        graus.id_grau = fd.id_grau
                 GROUP BY {1}""".\
                    format(select,
                           group_by)
                
        try:
            self.cursor.execute(cmd)
            
            r = self.cursor.fetchall()
            
            return r
            
        except Exception, e:
            print 'Got error %s' % e
        pass
    pass
    
    #---------------------------------------
    # Estatisticas segundo os parametros passados
    #---------------------------------------    
    def statistics(self, years, groupby, count):
        
        select = self.data_translator.get(count)
        group_by = ','.join([str('fd.' + self.data_translator.get(i)) for i in groupby])
        
        cmd = """SELECT
                    {0}, COUNT(DISTINCT {1}) AS Total
                 FROM
                    Fichas_Docencia fd
                 INNER JOIN estabelecimentos on
                    estabelecimentos.id_estabelecimento = fd.id_estabelecimento
                 INNER JOIN graus on
                    graus.id_grau = fd.id_grau
                 WHERE
                    ano in ({2})
                 GROUP BY {3}""".\
                    format('fd.ano',
                           'fd.' + select,
                           ','.join([str(i) for i in years]),
                           group_by)
                        
        print cmd
        
        try:
            self.cursor.execute(cmd)
            
            r = self.cursor.fetchall()
            
            return r
            
        except Exception, e:
            print 'Got error %s' % e
        pass
    pass
    