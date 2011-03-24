# -*- coding: utf-8 -*-
'''
projecto- classe destinada a leitura da informação no sistema rebides
autor- Jose Jasnau Caeiro
data de criação do módulo- 7/03/2011
observações-

'''

# processamento de HTML através do parser BeautifulSoup
from BeautifulSoup import BeautifulSoup
import re

# biblioteca para acesso através de protocolos de Internet
import urllib2

# escrita em csv
import csv
import sqlite3
import time

def obter_codigos_tipo_estabelecimento(ano):
    '''
    a funcao obtem os codigos dos tipos de estabelecimento
    de ensino superior
    
    ano - ano a que se referem os dados
    '''
    # url base do sistema Rebides
    URL_REBIDES = 'http://www.rebides.oces.mctes.pt/Rebides'

    # formacao do Universal Resource Locator
    # a partir do ano
    url = URL_REBIDES + '0' + str(ano)

    try:
        # abre a conexao para o site
        ficheiro = urllib2.urlopen( url )
    except:
        print "ERRO DE CONEXAO", url
        pass


    try:
        # leitura dos dados da pagina
        dados = ficheiro.read()
    except:
        print "ERRO de LEITURA"
        pass
    else:
        ficheiro.close()

    # processamento dos dados da página
    soup = BeautifulSoup(dados)

    # os codigos vao estar associados ao
    # tipo de estabelecimento
    d_tipos_estabelecimentos = {}

    lista = soup.findAll('a', )
    for x in lista:
        # href vai ter o conteudo da referencia em HTML
        href = x['href']

        # remove de href tudo menos o codigo
        href = re.sub('rebid\_m1\.asp\?codr\=', '', href)
        
        # o conteudo encontra-se do tag encontra-se aqui
        contents = x.contents
        
        # converte para utf-8
        tipo_estabelecimento = contents[0].encode('utf-8')

        d_tipos_estabelecimentos[ tipo_estabelecimento ] = href
        pass
    return d_tipos_estabelecimentos


"""
# exemplo de obtenção dos codigos dos tipos de estabelecimento
for ano in range(0,10):
    print "ANO: 200{0}".format(ano)
    d_tipos_estabelecimentos = obter_codigos_tipo_estabelecimento(ano)

    for key, value in d_tipos_estabelecimentos.iteritems():
        print key, ':', value
        pass
"""

def obter_codigos_estabelecimentos(ano, codigo_tipo_estabelecimento):
    '''
    a funcao obtem os codigos dos tipos de estabelecimento
    de ensino superior
    
    ano - ano a que se referem os dados
    '''
    # url base do sistema Rebides
    URL_REBIDES = 'http://www.rebides.oces.mctes.pt/Rebides'

    # formacao do Universal Resource Locator
    # a partir do ano
    url = URL_REBIDES + '0' + str(ano)
    url = url + '/rebid_m1.asp?codr=' + codigo_tipo_estabelecimento

    try:
        # abre a conexao para o site
        ficheiro = urllib2.urlopen( url )
    except:
        print "ERRO DE CONEXAO", url
        pass


    try:
        # leitura dos dados da pagina
        dados = ficheiro.read()
    except:
        print "ERRO de LEITURA"
        pass
    else:
        ficheiro.close()

    # processamento dos dados da página
    soup = BeautifulSoup(dados)

    # os codigos vao estar associados ao
    # tipo de estabelecimento
    d_estabelecimentos = {}

    lista = soup.findAll('a', )
    for x in lista:
        # href vai ter o conteudo da referencia em HTML
        href = x['href']

        # remove de href tudo menos o codigo
        chave_procura = \
            'rebid\_m2\.asp\?CodR\={0}\&CodP\='.\
            format(codigo_tipo_estabelecimento)

        href = re.sub(chave_procura, '', href)

        # o conteudo encontra-se do tag encontra-se aqui
        contents = x.contents
        
        # converte para utf-8
        estabelecimento = contents[0].encode('utf-8')

        d_estabelecimentos[ estabelecimento ] = href
        pass

    return d_estabelecimentos

"""
# exemplo de pesquisa de codigos de estabelecimentos        
for ano in range(0,10):
    d_tipos_estabelecimento = obter_codigos_tipo_estabelecimento(ano)
    for tipo_estabelecimento, codigo_tipo_estabelecimento \
            in d_tipos_estabelecimento.iteritems():
        d_estabelecimentos = \
            obter_codigos_estabelecimentos(ano, codigo_tipo_estabelecimento)
        contador = 0
        for key, value in d_estabelecimentos.iteritems():
            contador += 1
            pass
        print ano, \
            tipo_estabelecimento,'numero de estabelecimentos: ', contador
        pass
    pass
"""

def obter_informacao_docentes(ano, tipo, codR, estabelecimento, codP):
    '''
    codR - codigo do tipo de estabelecimento
    codP - codigo do estabelecimento
    '''
    C_NOME_COMPLETO = 1
    C_GRAU = 3
    C_CURSO = 5
    C_CATEGORIA = 7
    C_REGIME = 9

    # url base do sistema Rebides
    URL_REBIDES = 'http://www.rebides.oces.mctes.pt/Rebides'

    # formacao do Universal Resource Locator
    # a partir do ano
    url = URL_REBIDES + '0' + str(ano)
    url = url + '/rebid_m2.asp?CodR=' + codR + '&CodP=' + codP 

    try:
        # abre a conexao para o site
        ficheiro = urllib2.urlopen( url )
    except:
        print "ERRO DE CONEXAO", url
        pass

    try:
        # leitura dos dados da pagina
        dados = ficheiro.read()
    except:
        print "ERRO de LEITURA"
        pass
    else:
        ficheiro.close()

    # processamento dos dados da página
    soup = BeautifulSoup(dados)
    
    lista = soup.findAll('tr', )
    
    lista_docentes = []

    for x in lista:
        nome = x.contents[C_NOME_COMPLETO].contents[0]
        
        grau = x.contents[C_GRAU].contents[0]
        grau = grau.lstrip()
        
        curso = x.contents[C_CURSO].contents[0]
        curso = curso.lstrip()

        categoria = x.contents[C_CATEGORIA].contents[0]

        regime = x.contents[C_REGIME].contents[0]

        conteudo = x.contents[11].findAll('a')
        for y in conteudo:
            # href vai ter o conteudo da referencia em HTML
            href = y['href']


            chave_procura = 'rebid\_m3\.asp\?CodD\='
            href = re.sub(chave_procura, '', href)

            chave_procura = '\&CodP\={0}'.format(codP)
            codigo_docente = re.sub(chave_procura, '', href)
            pass

        if nome != "NOME COMPLETO":
            if nome.encode('utf-8') != '&nbsp;':
                nome_completo = nome
                nome_completo = nome_completo.expandtabs()
                novo_completo = re.sub('\015', '', nome_completo)
                nome_completo = novo_completo.lstrip()
                nome_completo = nome_completo.encode('utf-8')
                
                categoria_completo = categoria.lstrip()
                categoria_completo = categoria_completo.encode('utf-8')

                regime_completo = regime.lstrip()
                regime_completo = regime_completo.encode('utf-8')
                
                codigo_docente_completo = codigo_docente
                pass

            grau_completo = grau.encode('utf-8')
            curso_completo = curso.encode('utf-8')

            informacao_docente = [ codigo_docente_completo,
                                   nome_completo,
                                   grau_completo,
                                   curso_completo,
                                   categoria_completo,
                                   regime_completo,
                                   ano,
                                   tipo,
                                   estabelecimento]
            lista_docentes.append(informacao_docente)
            pass
        pass
    return lista_docentes

def escrita_csv(ano):
    '''
    escrita dos dados em ficheiro csv
    '''
    ficheiro = open('reb{0}.csv'.format(ano),"wb")
    csvwriter = csv.writer( ficheiro, delimiter=',')

    print "ANO: 200{0}".format(ano)
    d_tipos_estabelecimento = obter_codigos_tipo_estabelecimento(ano)

    for tipo, codR in d_tipos_estabelecimento.iteritems():
        print tipo, ' ', codR
        d_estabelecimentos = \
            obter_codigos_estabelecimentos(ano, codR)
        for estabelecimento, codP in d_estabelecimentos.iteritems():
            ld = obter_informacao_docentes(ano, tipo, 
                                           codR, estabelecimento, codP)

            for x in ld:
                csvwriter.writerow(x)
            pass
        pass
    ficheiro.close()
    pass


########################################
# operacoes com base de dados
########################################

def criar_tabelas():
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


def preencher_tipos_estabelecimento(ano):
    '''
    preenchimento da tabela tipos_estabelecimento
    '''
    conn = sqlite3.connect('rebides.db')
    cursor = conn.cursor()
    print "ANO: 200{0}".format(ano)
    d_tipos_estabelecimento = obter_codigos_tipo_estabelecimento(ano)

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

def preencher_estabelecimentos(conn, cursor, d_estabelecimentos):
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

def preencher_geral(lista, conn, cursor, tipo):
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

def preencher_docentes(lista, conn, cursor):
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

def organizar_conjuntos_unicos(lista_entrada, tipo):
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
                     
def preencher_fichas_curso(lista, conn, cursor):
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

def preencher_fichas_docencia(lista, conn, cursor):
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

def preencher_tabelas_gerais(ano):
    
    preencher_tipos_estabelecimento(ano)

    conn = sqlite3.connect('rebides.db')
    cursor = conn.cursor()
    print "ANO: 200{0}".format(ano)
    d_tipos_estabelecimento = obter_codigos_tipo_estabelecimento(ano)

    lista = []
    for tipo, codR in d_tipos_estabelecimento.iteritems():
        print tipo, ' ', codR

        d_estabelecimentos = obter_codigos_estabelecimentos(ano, codR)
        
        # coloca na base de dados 
        preencher_estabelecimentos(conn, cursor, d_estabelecimentos)

        for estabelecimento, codP in d_estabelecimentos.iteritems():
            # obtem a informação de um docente
            ld = obter_informacao_docentes(ano, tipo, 
                                           codR, estabelecimento, codP)
            lista.append(ld)
            pass
        pass

    # preenche a informação geral comum
    lista_unica = organizar_conjuntos_unicos(lista, 'graus')
    preencher_geral(lista_unica, conn, cursor, 'graus')

    lista_unica = organizar_conjuntos_unicos(lista, 'cursos')
    preencher_geral(lista_unica, conn, cursor, 'cursos')

    lista_unica = organizar_conjuntos_unicos(lista, 'regimes')
    preencher_geral(lista_unica, conn, cursor, 'regimes')

    lista_unica = organizar_conjuntos_unicos(lista, 'categorias')
    preencher_geral(lista_unica, conn, cursor, 'categorias')

    # preenchimento da informação de cada docente
    preencher_docentes(lista, conn, cursor)

    # preencher ficha de cursos
    preencher_fichas_curso(lista, conn, cursor)
    cursor.close()

    # preencher fichas docencia
    preencher_fichas_docencia(lista, conn, cursor)
    cursor.close()

    pass


t1 = time.clock()
criar_tabelas()

# escrita em ficheiros csv
#for ano in range(0,10):
#    escrita_csv(ano)

for ano in range(0,10):
    # preencher tabelas gerais
    preencher_tabelas_gerais(ano)

t2 = time.clock()
print "tempo de execução: ", t2-t1



