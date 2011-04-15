# -*- coding: utf-8 -*-

import sqlite3

class Statistics:

    # Statistics constructor
    def __init__(self):
        
        # initialize database connection
        self.conn = sqlite3.connect('rebides.db')
        self.cursor = self.conn.cursor()
        
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
    