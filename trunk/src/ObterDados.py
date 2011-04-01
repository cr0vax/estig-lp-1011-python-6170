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

class ObterDados:
    
    def obter_codigos_tipo_estabelecimento(self, ano):
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

    def obter_codigos_estabelecimentos(self, ano, codigo_tipo_estabelecimento):
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

    def obter_informacao_docentes(self, ano, tipo, codR, estabelecimento, codP):
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
