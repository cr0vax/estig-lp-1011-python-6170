# -*- coding: utf-8 -*-

import sqlite3
from ObterDados import ObterDados

#---------------------------------------
# Classe responsável pela interação activa na base de dados
# Autor: Jose Jasnau Caeiro
# Alterações: Bruno Moreira
# Número: 6170
#---------------------------------------

class BaseDados:
    
    #---------------------
    # Construtor da classe
    #---------------------
    def __init__(self):
        self.dados = ObterDados()
        pass
    pass


    #---------------------------------
    # Cria as tabelas da base de dados
    #---------------------------------
    def criar_tabelas(self):

        # inicia a conexão à base de dados
        conn = sqlite3.connect('rebides.db')
        cursor = conn.cursor()
        
        # tabela graus
        cursor.execute("""CREATE TABLE IF NOT EXISTS graus
                ("id_grau" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 "designacao" TEXT NOT NULL);
                """)

        # tabela cursos
        cursor.execute("""CREATE TABLE IF NOT EXISTS cursos
                        ("id_curso" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        "designacao" TEXT NOT NULL)
                       """)
                    
        # tabela categorias
        cursor.execute("""CREATE TABLE IF NOT EXISTS categorias
                        ("id_categoria" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        "designacao" TEXT NOT NULL)
                       """)
        
        # tabela regimes
        cursor.execute("""CREATE TABLE IF NOT EXISTS regimes
                          ("id_regime" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          "designacao" TEXT NOT NULL)
                       """)
                    
        # tabela estabelecimentos         
        cursor.execute("""CREATE TABLE IF NOT EXISTS estabelecimentos
                          ("id_estabelecimento" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          "designacao" TEXT NOT NULL)
                       """)
                    
        # tabela tipos_estabelecimentos
        cursor.execute("""CREATE TABLE IF NOT EXISTS tipos_estabelecimento
                          ("id_tipo_estabelecimento" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          "designacao" TEXT NOT NULL)
                       """)
                    
        # tabela docentes
        cursor.execute("""CREATE TABLE IF NOT EXISTS docentes
                          ("nome_completo" TEXT, 
                           "id_docente" INTEGER PRIMARY KEY)
                       """)
        
        # tabela fichas_docencia
        cursor.execute("""CREATE TABLE IF NOT EXISTS fichas_docencia
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           ano INTEGER,
                           id_docente INTEGER REFERENCES docentes (id_docente),
                           id_estabelecimento INTEGER REFERENCES estabelecimentos (id_estabelecimento),
                           id_categoria INTEGER REFERENCES categorias (id_categoria),
                           id_regime INTEGER REFERENCES regimes (id_regime),
                           id_tipo_estabelecimento INTEGER REFERENCES tipos_estabelecimento (id_tipo_estabelecimento),
                           id_grau INTEGER REFERENCES graus (id_grau),
                           id_curso INTEGER REFERENCES cursos (id_curso))
                       """)
                    
        # tabela listas
        cursor.execute("""CREATE TABLE IF NOT EXISTS listas
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             "titulo" TEXT NOT NULL,
                             "tipo" INTEGER NOT NULL)
                        """)

        cursor.close()
        pass
    pass


    #----------------------------------------
    # Preenche os tipos de estabelecimento
    #
    #   ano - número do ano a ser preenchido
    #----------------------------------------
    def preencher_tipos_estabelecimento(self, ano):
        '''
        preenchimento da tabela tipos_estabelecimento
        '''
        conn = sqlite3.connect('rebides.db')
        cursor = conn.cursor()
        
        d_tipos_estabelecimento = self.dados.obter_codigos_tipo_estabelecimento(ano)

        for tipo, codR in d_tipos_estabelecimento.iteritems():
            try:
                cmd = """insert into tipos_estabelecimento (designacao) 
                        values ('{0}')""".format(tipo.replace("'", "''"))
                cursor.execute(cmd)
                conn.commit()
            except:
                pass
            pass
        cursor.close()
        pass

    #----------------------------------------
    # Preenche os estabelecimentos
    #
    #   conn               - conexão à bd
    #   cursor             - cursor com dados
    #   d_estabelecimentos - lista com estabelecimentos
    #----------------------------------------
    def preencher_estabelecimentos(self, conn, cursor, d_estabelecimentos):
        '''
        preenchimento da tabela estabelecimentos
        '''
        for estabelecimento, codP in d_estabelecimentos.iteritems():
            cmd = """insert into {0} (designacao) values ('{1}')""".\
                format('estabelecimentos', estabelecimento.replace("'", "''"))
            
            try:
                cursor.execute(cmd)
            except:
                continue
            pass
        conn.commit()
        pass

    #------------------------------
    # Preenche uma tabela com base no tipo
    #
    #   lista       - lista com os dados a preencher
    #   conn        - conexão à base de dados
    #   cursor      - cursor da base de dados
    #   tipo        - tabela onde inserir os dados
    #------------------------------
    def preencher_geral(self, lista, conn, cursor, tipo):

        for x in lista:
            cmd = """insert into {0} (designacao) values ('{1}')""".\
                format(tipo, x.replace("'", "''"))

            try:
                cursor.execute(cmd)

            except:
                print tipo, x
                pass
            pass
        conn.commit()
        pass
    pass

    #------------------------------
    # Preenche a tabela dos docentes
    #
    #   lista       - lista com os docentes
    #   conn        - conexão à base de dados
    #   cursor      - cursor da base de dados
    #------------------------------
    def preencher_docentes(self, lista, conn, cursor):
        C_CODIGO = 0
        C_DOCENTE = 1

        # uma linha corresponde a uma entrada 
        for linha in lista:
            for x in linha:
                cmd = """insert into {0} (id_docente, nome_completo) values ({1}, '{2}')""".\
                    format('docentes', x[C_CODIGO], x[C_DOCENTE].replace("'", "''"))
                try:
                    cursor.execute(cmd)
                except:
                    continue
                pass
            pass
        conn.commit()
        
        pass

    #------------------------------
    # Filtra os elementos únicos de uma lista
    #
    #   lista_entrada   - lista de dados
    #   tipo            - tipo de informação
    #
    #   retorna a lista filtrada
    #------------------------------
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
    pass                    

    #------------------------------
    # Preenchimento das fichas de docenciatabelas gerais
    #
    #   lista       - lista de dados
    #   conn        - conexão à base de dados
    #   cursor      - curosr da base de dados
    #------------------------------
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
        
        print "Inicio do preenchimento das fichas de docencia"

        # uma linha corresponde a uma entrada 
        for linha in lista:
            for x in linha:
                # selecciona a referência do docente
                cmd = """SELECT id_docente FROM docentes WHERE nome_completo = '{0}'""".\
                    format(x[C_DOCENTE].replace("'", "''"))
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    docente = r[0]
                except:
                    continue

                # selecciona a referência do estabelecimento
                cmd = """SELECT id_estabelecimento FROM estabelecimentos 
                         WHERE designacao = '{0}'""".\
                    format(x[C_ESTABELECIMENTO].replace("'", "''"))
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    estabelecimento = r[0]
                except:
                    continue

                # selecciona a referência da categoria
                cmd = """SELECT id_categoria FROM categorias WHERE designacao = '{0}'""".\
                    format(x[C_CATEGORIA].replace("'", "''"))
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    categoria = r[0]
                except:
                    continue

                # selecciona a referência do regime
                cmd = """SELECT id_regime FROM regimes WHERE designacao = '{0}'""".\
                    format(x[C_REGIME].replace("'", "''"))
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    regime = r[0]
                except:
                    continue

                # selecciona a referência do tipo de estabelecimento
                cmd = """SELECT id_tipo_estabelecimento FROM tipos_estabelecimento 
                         WHERE designacao = '{0}'""".\
                    format(x[C_TIPO_ENSINO].replace("'", "''"))
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    tipo_estabelecimento = r[0]
                except:
                    continue
                
                # selecciona a referência do grau
                cmd = """SELECT id_grau FROM graus WHERE designacao = '{0}'""".\
                    format(x[C_GRAU].replace("'", "''"))
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    grau = r[0]
                except:
                    continue

                # selecciona a referência do curso
                cmd = """SELECT id_curso FROM cursos WHERE designacao = '{0}'""".\
                    format(x[C_CURSO].replace("'", "''"))
                try:
                    cursor.execute(cmd)
                    r = cursor.fetchone()
                    curso = r[0]
                except:
                    continue

                # insere na base de dados
                cmd = """INSERT INTO fichas_docencia 
                         (ano, 
                          id_docente, 
                          id_estabelecimento, 
                          id_categoria,
                          id_regime, 
                          id_tipo_estabelecimento,
                          id_grau,
                          id_curso)
                         VALUES 
                         ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}') 
                      """.format(x[C_ANO], docente, estabelecimento, categoria, 
                                 regime, tipo_estabelecimento, grau, curso)
                         
                try:
                    cursor.execute(cmd)
                except:
                    continue
                pass
            pass

        print "Conclusão do preenchimento das fichas de docencia"
        conn.commit()
        pass

    #------------------------------
    # Preenchimento das tabelas gerais
    #
    #   ano - ano do preenchimento
    #------------------------------
    def preencher_tabelas_gerais(self, ano):
        
        self.preencher_tipos_estabelecimento(ano)

        conn = sqlite3.connect('rebides.db')
        cursor = conn.cursor()
        print "Preencher tabelas gerais", "ANO: 200{0}".format(ano)
        d_tipos_estabelecimento = self.dados.obter_codigos_tipo_estabelecimento(ano)

        lista = []
        for tipo, codR in d_tipos_estabelecimento.iteritems():
            #print tipo, ' ', codR

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

        # preencher fichas docencia
        self.preencher_fichas_docencia(lista, conn, cursor)
        cursor.close()

        pass
    
    #------------------------------
    # Inserção de uma list costumizada
    #
    #   title   - título da consulta
    #   type    - tipo de consulta
    #               0 - listas
    #               1 - estatisticas
    #
    #   retorna o id da página
    #------------------------------
    def insert_custom_list(self, title, type):
        #inicia variaveis
        file_name = ''
        
        # cria conexão à bd
        conn = sqlite3.connect('rebides.db')
        cursor = conn.cursor()
        
        title = title.encode('utf-8').replace("'", "''")
        
        # adicionar comando
        cmd = """INSERT INTO listas
                    (titulo, tipo)
                VALUES ('{0}',{1})""".\
                format(\
                    title,\
                    type)

        # executa o comando
        try:
            cursor.execute(cmd)
            conn.commit()
            
            # valida o ID da página inserida
            cmd = """SELECT MAX(ID) FROM listas"""
            cursor.execute(cmd)
            r = cursor.fetchall()
            
            # constroi o nome do ficheiro com base no ID
            file_name = str(r[0][0]) + '.html'
        except:
            print "Erro:", cmd
        pass
        
        cursor.close
        
        # retorna o nome do ficheiro
        return file_name
    pass
    