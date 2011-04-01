# -*- coding: utf-8 -*-

import sqlite3
from ObterDados import ObterDados

########################################
# operacoes com base de dados
########################################

class BaseDados:
    
    def __init__(self):
        self.dados = ObterDados()
        pass
    pass

    def criar_tabelas(self):
        '''
        criacao das tabelas da base de dados
        '''
        conn = sqlite3.connect('rebides.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS graus 
                          (designacao TEXT PRIMARY KEY)
                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS cursos
                          (designacao TEXT PRIMARY KEY)
                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS categorias
                          (designacao TEXT PRIMARY KEY)
                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS regimes
                          (designacao TEXT PRIMARY KEY)
                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS estabelecimentos
                          (designacao TEXT PRIMARY KEY)
                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS tipos_estabelecimento
                          (designacao TEXT PRIMARY KEY)
                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS docentes
                          (nome_completo TEXT PRIMARY KEY, 
                           codigo INTEGER UNIQUE)
                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS fichas_curso
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           ano INTEGER,
                           docente REFERENCES docentes (nome_completo),
                           grau REFERENCES graus (designacao),
                           curso REFERENCES cursos (designacao))
                       """)
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS fichas_docencia
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           ano INTEGER,
                           docente REFERENCES docentes (nome_completo),
                           estabelecimento REFERENCES estabelecimentos (designacao),
                           categoria REFERENCES categorias (designacao),
                           regime REFERENCES regimes (designacao),
                           tipo_estabelecimento REFERENCES 
                           tipos_estabelecimento (designacao))
                       """)


        cursor.close()
        pass


    def preencher_tipos_estabelecimento(self, ano):
        '''
        preenchimento da tabela tipos_estabelecimento
        '''
        conn = sqlite3.connect('rebides.db')
        cursor = conn.cursor()
        print "ANO: 200{0}".format(ano)

        d_tipos_estabelecimento = self.dados.obter_codigos_tipo_estabelecimento(ano)

        for tipo, codR in d_tipos_estabelecimento.iteritems():
            try:
                cmd = """insert into tipos_estabelecimento (designacao) values ('{0}')""".format(tipo)
                cursor.execute(cmd)
                conn.commit()
            except:
                pass
            pass
        cursor.close()
        pass

    def preencher_estabelecimentos(self, conn, cursor, d_estabelecimentos):
        '''
        preenchimento da tabela estabelecimentos
        '''
        for estabelecimento, codP in d_estabelecimentos.iteritems():
            cmd = """insert into {0} (designacao) values ('{1}')""".\
                format('estabelecimentos', estabelecimento)
            
            try:
                cursor.execute(cmd)
            except:
                continue
            pass
        conn.commit()
        pass

    def preencher_geral(self, lista, conn, cursor, tipo):
        d_informacao = {}
        d_informacao['graus'] = 2
        d_informacao['cursos'] = 3
        d_informacao['categorias'] = 4
        d_informacao['regimes'] = 5
        d_informacao['estabelecimentos'] = 8

        for x in lista:
            cmd = """insert into {0} (designacao) values ('{1}')""".\
                format(tipo, x)

            try:
                cursor.execute(cmd)

            except:
                print tipo, x
                pass
            pass
        conn.commit()
        pass

    def preencher_docentes(self, lista, conn, cursor):
        C_CODIGO = 0
        C_DOCENTE = 1

        # uma linha corresponde a uma entrada 
        for linha in lista:
            for x in linha:
                cmd = """insert into {0} (codigo, nome_completo) values ({1}, '{2}')""".\
                    format('docentes', x[C_CODIGO], x[C_DOCENTE])
                print cmd
                try:
                    cursor.execute(cmd)
                except:
                    print x[C_DOCENTE]
                    continue
                pass
            pass
        conn.commit()
        
        pass

    def organizar_conjuntos_unicos(self, lista_entrada, tipo):
        d_informacao = {}
        d_informacao['graus'] = 2
        d_informacao['cursos'] = 3
        d_informacao['categorias'] = 4
        d_informacao['regimes'] = 5
        d_informacao['estabelecimentos'] = 8

        conjunto_unico = set()
        lista = []
        for ld in lista_entrada:
            for x in ld:
                conjunto_unico.add(x[d_informacao[tipo]])
                pass
            pass
        
        for y in conjunto_unico:
            lista.append(y)
            pass

        return lista
                         
    def preencher_fichas_curso(self, lista, conn, cursor):
        C_CODIGO = 0
        C_DOCENTE = 1
        C_GRAU = 2
        C_CURSO = 3
        C_ANO = 6

        # uma linha corresponde a uma entrada 
        for linha in lista:
            for x in linha:
                # selecciona a referência do grau
                cmd = """SELECT designacao FROM graus WHERE designacao = '{0}'""".\
                    format(x[C_GRAU])
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    grau = r[0]
                except:
                    continue

                # selecciona a referência do curso
                cmd = """SELECT designacao FROM cursos WHERE designacao = '{0}'""".\
                    format(x[C_CURSO])
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    curso = r[0]
                except:
                    continue

                # selecciona a referência do docente
                cmd = """SELECT nome_completo FROM docentes where nome_completo = '{0}'""".\
                    format(x[C_DOCENTE])
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    docente = r[0]
                except:
                    continue

                # insere na base de dados
                cmd = """INSERT INTO fichas_curso 
                         (ano, docente, grau, curso)
                         VALUES 
                         ('{0}','{1}','{2}','{3}') """.\
                    format(x[C_ANO], 
                           docente.encode('utf-8'), 
                           grau.encode('utf-8'), 
                           curso.encode('utf-8'))
                try:
                    cursor.execute(cmd)
                except:
                    continue
                pass

            
            pass

        conn.commit()
        
        
        pass

    def preencher_fichas_docencia(self, lista, conn, cursor):
        C_CODIGO = 0
        C_DOCENTE = 1
        C_GRAU = 2
        C_CURSO = 3
        C_CATEGORIA = 4
        C_REGIME = 5
        C_ANO = 6
        C_TIPO_ENSINO = 7
        C_ESTABELECIMENTO = 8

        # uma linha corresponde a uma entrada 
        for linha in lista:
            for x in linha:
                # selecciona a referência do docente
                cmd = """SELECT nome_completo FROM docentes WHERE nome_completo = '{0}'""".\
                    format(x[C_DOCENTE])
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    docente = r[0].encode('utf-8')
                except:
                    continue

                # selecciona a referência do estabelecimento
                cmd = """SELECT designacao FROM estabelecimentos 
                         WHERE designacao = '{0}'""".\
                    format(x[C_ESTABELECIMENTO])
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    estabelecimento = r[0].encode('utf-8')
                except:
                    continue

                # selecciona a referência da categoria
                cmd = """SELECT designacao FROM categorias WHERE designacao = '{0}'""".\
                    format(x[C_CATEGORIA])
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    categoria = r[0].encode('utf-8')
                except:
                    continue

                # selecciona a referência do regime
                cmd = """SELECT designacao FROM regimes WHERE designacao = '{0}'""".\
                    format(x[C_REGIME])
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    regime = r[0].encode('utf-8')
                except:
                    continue

                # selecciona a referência do tipo de estabelecimento
                cmd = """SELECT designacao FROM tipos_estabelecimento 
                         WHERE designacao = '{0}'""".\
                    format(x[C_TIPO_ENSINO])
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    tipo_estabelecimento = r[0].encode('utf-8')
                except:
                    continue

                # insere na base de dados
                cmd = """INSERT INTO fichas_docencia 
                         (ano, 
                          docente, 
                          estabelecimento, 
                          categoria,
                          regime, 
                          tipo_estabelecimento)
                         VALUES 
                         ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}') 
                      """.format(x[C_ANO], docente, estabelecimento, categoria, 
                                 regime, tipo_estabelecimento)
                print cmd
                         
                         
                try:
                    cursor.execute(cmd)
                except:
                    continue
                pass
            pass

        conn.commit()
        pass

    def preencher_tabelas_gerais(self, ano):
        
        self.preencher_tipos_estabelecimento(ano)

        conn = sqlite3.connect('rebides.db')
        cursor = conn.cursor()
        print "ANO: 200{0}".format(ano)
        d_tipos_estabelecimento = self.dados.obter_codigos_tipo_estabelecimento(ano)

        lista = []
        for tipo, codR in d_tipos_estabelecimento.iteritems():
            print tipo, ' ', codR

            d_estabelecimentos = self.dados.obter_codigos_estabelecimentos(ano, codR)
            
            # coloca na base de dados 
            self.preencher_estabelecimentos(conn, cursor, d_estabelecimentos)

            for estabelecimento, codP in d_estabelecimentos.iteritems():
                # obtem a informação de um docente
                ld = self.dados.obter_informacao_docentes(ano, tipo, 
                                               codR, estabelecimento, codP)
                lista.append(ld)
                pass
            pass

        # preenche a informação geral comum
        lista_unica = self.organizar_conjuntos_unicos(lista, 'graus')
        self.preencher_geral(lista_unica, conn, cursor, 'graus')

        lista_unica = self.organizar_conjuntos_unicos(lista, 'cursos')
        self.preencher_geral(lista_unica, conn, cursor, 'cursos')

        lista_unica = self.organizar_conjuntos_unicos(lista, 'regimes')
        self.preencher_geral(lista_unica, conn, cursor, 'regimes')

        lista_unica = self.organizar_conjuntos_unicos(lista, 'categorias')
        self.preencher_geral(lista_unica, conn, cursor, 'categorias')

        # preenchimento da informação de cada docente
        self.preencher_docentes(lista, conn, cursor)

        # preencher ficha de cursos
        self.preencher_fichas_curso(lista, conn, cursor)
        cursor.close()

        # preencher fichas docencia
        self.preencher_fichas_docencia(lista, conn, cursor)
        cursor.close()

        pass