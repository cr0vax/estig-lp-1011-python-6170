# -*- coding: utf-8 -*-

from Dados import Dados
import shutil
import os

#---------------------------------------
# Classe responsável por gerar páginas HTML
# Autor: Bruno Moreira
# Número: 6170
#---------------------------------------

class Html:
    
    HEADER_COLOR = '#99CCFF'
    ROW_COLORS = ('#E0ECF8', '#FFFFFF')
    
    # Html class constructor
    def __init__(self):
        self.dados = Dados()

        # retorna os anos
        self.years = []
        for year in self.dados.get_years():
            self.years.append(year[0])
        pass
    pass
    
    #---------------------------------------
    # cria as páginas para um determinado ano
    #---------------------------------------
    def create_index(self):
        print "Started creating pages"

        # cria o ficheiro com o índice
        file = open('index.html',"wb")
        
        # inicia a página
        file.write('<html>')        # start html
        file.write('<body>')        # start body
        file.write('<table>')       # start table

        # Adiciona o índíce por ano
        self.add_years_to_index(self.years, file)
        
        # Adiciona as estatisticas
        self.add_statistics_to_index(file)
        
        # Adiciona as listas
        self.add_lists_to_index(file)
        
        # termina a página
        file.write('</html>')        # close html
        file.write('</body>')        # close body
        file.write('</table>')       # close table

        print "Finished creating pages"
        pass
    pass
    
    
    #---------------------------------------
    # Adiciona as estatísticas ao índice
    #
    #   file    - ficheiro onde serão inseridos os dados
    #---------------------------------------
    def add_statistics_to_index(self, file):

        # definição de variaveis
        URL_HTML = 'html/custom'
        URL_CSV =  'csv'
        
        # adiciona o título
        file.write('<tr bgcolor={0}>\
            <td>Últimas 20 estatisticas geradas na aplicação</td>\
            <td>CSV</td></tr>'.\
            format(self.HEADER_COLOR))
                
        # selecciona as estatisticas da base de dados
        bd = Dados()
        pages = bd.get_pages(1)
        
        #escreve as estatisticas da base de dados
        for page in pages:
            page_url = URL_HTML + '/' + str(page[0]) + '.html'
            csv_url  = URL_CSV + '/' + str(page[0]) + '.csv'
            page_title = page[1]
            
            file.write('<tr>\
                <td><a href={0}>{1}</a></td>\
                <td><a href={2}>abrir</a></td></tr>'.\
                            format(page_url, page_title, csv_url))
        pass
    pass
    
    #---------------------------------------
    # Adiciona as listas ao índice
    #
    #   file    - ficheiro onde serão inseridos os dados
    #---------------------------------------
    def add_lists_to_index(self, file):

        # definição de variaveis
        URL_HTML = 'html/custom'
        URL_CSV =  'csv'
        
        # adiciona o título
        file.write('<tr bgcolor={0}><td>\
            Últimas 20 listas geradas na aplicação</td>\
            <td>CSV</td></tr></tr>'.\
            format(self.HEADER_COLOR))
                
        # selecciona as listas da base de dados
        bd = Dados()
        pages = bd.get_pages(0)
        
        #escreve as estatisticas da base de dados
        for page in pages:
            page_url = URL_HTML + '/' + str(page[0]) + '.html'
            csv_url  = URL_CSV + '/' + str(page[0]) + '.csv'
            page_title = page[1]
            
            file.write('<tr>\
                <td><a href={0}>{1}</a></td>\
                <td><a href={2}>abrir</a></td></tr>'.\
                            format(page_url, page_title, csv_url))
        pass
    pass
    
    #---------------------------------------
    # Adiciona os anos ao índice
    #
    #   years   - array com os anos
    #   file    - ficheiro onde serão inseridos os dados
    #---------------------------------------
    def add_years_to_index(self, years, file):
        
        # adiciona o título
        file.write('<tr bgcolor={0}><td>\
            Dados disponíveis na BD Rebides</td></tr>'.\
            format(self.HEADER_COLOR))
        
        # Adiciona os anos
        for year in years:
            file.write('<tr>')
            file.write('<td><a href="html/200{0}">Ano 200{1}</a></td>'.format(year, year))
            file.write('</tr>')

            # cria as restantes páginas do ano
            self.create_pages_for_year(year)
            pass
        pass
        
        # fecha o ficheiro
        file.close 
        pass
    pass

    #---------------------------------------
    # cria as páginas de um determinado ano
    #
    #   year - ano para o qual vão ser criadas as páginas
    #---------------------------------------
    def create_pages_for_year(self, year):
        path = 'html/200{0}'.format(year)        
        # elimina a pasta do ano
        try:
            shutil.rmtree(path)
        except:
            print "Directório inexistente"
        pass
            
        # cria a pasta do ano
        os.makedirs(path)
        
        # cria a página dos tipos de establecimento
        descriptive_path = 'Rebides/200{0}'.format(year)
        self.create_establishment_type_pages(descriptive_path, path, year)

        pass
    pass
    
    #---------------------------------------
    # cria páginas dos tipos de estabelecimento
    #
    #   descriptive_path          - caminho em texto para a página
    #   path                      - caminho para a página
    #   year                      - ano da página a ser criado
    #---------------------------------------
    def create_establishment_type_pages(self, descriptive_path, path, year):
        
        # recolhe os dados
        establishement_types = self.dados.get_establishment_types(year)
        
        # abre o ficheiro a ser criado
        file = open(path + '/index.html',"wb")
        
        # inicia a página
        column_names = ['NOME DO TIPO DE ESTABELECIMENTO']
        self.start_page(file, descriptive_path, path, column_names)
        
        # insere uma linha para cada tipo de establecimento
        for establishment_type in establishement_types:
            description = establishment_type[0].encode('utf-8')            
            establishment_type_code = str(establishment_type[1])
            
            # cria o directorio do tipo de establecimento
            establishment_type_path = path + '/' + establishment_type_code
            os.makedirs(establishment_type_path)
                    
            file.write('<tr>')
            file.write('<td><a href="./{0}">{1}</a></td>'.\
                                 format(establishment_type_code,
                                        description))
                                                
            file.write('</tr>')
            
            # cria as página com os establecimentos deste tipo
            self.create_establishment_pages(\
                descriptive_path + '/' + description,\
                establishment_type_path, year,\
                establishment_type_code)
            pass
        pass
        
        # termina a página
        self.end_page(file, descriptive_path, path)
        
        # fecha o ficheiro
        file.close
        
        pass
    pass
    
    #---------------------------------------
    # cria páginas dos estabelecimentos
    #
    #   descriptive_path          - caminho em texto para a página
    #   path                      - caminho para a página
    #   year                      - ano da página a ser criado
    #   establishment_type_code   - código do tipo de estabelecimento
    #---------------------------------------
    def create_establishment_pages(self, descriptive_path, path, year, establishment_type_code):
        
        establishements = \
            self.dados.get_establishments(year, establishment_type_code)
        file = open(path + '/index.html',"wb")
        
        # inicia a página
        column_names = ['NOME DO ESTABELECIMENTO']
        self.start_page(file, descriptive_path, path, column_names)
        
        for e in establishements:
            description = e[0].encode('utf-8')            
            establishment_code = str(e[1])
            
            # cria o directorio do establecimento
            establishment_path = path + '/' + establishment_code
            os.makedirs(establishment_path)
                    
            file.write('<tr>')
            file.write('<td><a href="./{0}">{1}</a></td>'.\
                                 format(establishment_code,
                                        description))
                                                
            file.write('</tr>')
            
            # cria a página dos docentes deste estabelecimento
            self.create_teacher_pages(\
                descriptive_path + '/' + description,\
                establishment_path,\
                year,\
                establishment_code)
            pass
        pass
        
        # termina a página
        self.end_page(file, descriptive_path, path)
        
        # fecha o ficheiro
        file.close
        
        pass
    pass
    
    #---------------------------------------
    # cria páginas dos docentes de cada estabelecimento
    #
    #   descriptive_path    - caminho em texto para a página
    #   path                - caminho para a página
    #   year                - ano da página a ser criado
    #   establishment       - o estabelecimento a que pertencem os docentes
    #---------------------------------------
    def create_teacher_pages(self, descriptive_path, path, year, establishment):

        teachers = self.dados.get_teachers(year, establishment)
        file = open(path + '/index.html',"wb")
        
        last_teacher = ''   # para saber o nome do ultimo professor
        
        # inicia a página
        column_names =\
            ('NOME COMPLETO', 'GRAU', 'CURSO OU ESPECIALIDADE', \
            'CATEGORIA', 'REGIME')
        self.start_page(file, descriptive_path, path, column_names)

        # define a cor da row
        color = 0
        
        for t in teachers:

            if t[0].encode('utf-8') == last_teacher:
                what_to_write = '&nbsp;'
            else:
                what_to_write = t[0].encode('utf-8')
                
                if color == 0:
                    color = 1
                else:
                    color = 0
                pass
            pass
                
            # inicia a linha
            file.write('<tr bgcolor={0}>'.format(self.ROW_COLORS[color]))
            
            # adiciona colunas à linha
            for x in range(len(t)):
                if x > 0:
                    what_to_write = t[x].encode('utf-8')
                    
                file.write('<td>{0}</td>'.format(what_to_write))
            pass
            
            # fecha a linha
            file.write('</tr>')
            
            # guarda o nome do docente
            last_teacher = t[0].encode('utf-8')
        pass
        
        # termina a página
        self.end_page(file, descriptive_path, path)
        
        # fecha o ficheiro
        file.close
        
        pass
    pass
    
    #---------------------------------------
    # Cria uma página de estatisticas
    #
    #   title       - título da estatistica
    #   data        - dados para construir a página
    #   column_names- nomes das colunas das estatisticas
    #   file_name   - nome do ficheiro a ser criado
    #---------------------------------------
    def create_statistics_page(self, title, data, column_names, file_name):
        
        # cria a pasta das estatisticas
        path = 'html/custom'
        if not os.path.isdir(path):
            os.makedirs(path)
        pass
        
        #cria o ficheiro
        file = open(path + '/' + file_name + '.html',"wb")
                
        # escreve o caminho da página
        descriptive_path = 'Rebides/' + title

        # inicia a página
        column_names.append('Total')
        self.start_page(file, descriptive_path, path, column_names)
        
        # adiciona conteúdo
        for row in data:
            file.write('<tr>')
            for column in row:
                try:
                    encoded_column = column.encode('utf-8')
                    file.write('<td>{0}</td>'.format(encoded_column))
                except:
                    file.write('<td>{0}</td>'.format(column))
                    continue
                pass
            pass
            file.write('</tr>')
        pass
        
        # conclui a página
        self.end_page(file, descriptive_path, path)
    pass
    
    #---------------------------------------
    # Cria uma página com uma lista
    #
    #   title       - título da estatistica
    #   data        - dados para construir a página
    #   column_names- nomes das colunas das estatisticas
    #   file_name   - nome do ficheiro a ser criado
    #---------------------------------------
    def create_lists_page(self, title, data, column_names, file_name):
        
        # cria a pasta fdas estatisticas
        path = 'html/custom'
        if not os.path.isdir(path):
            os.makedirs(path)
        pass
        
        #cria o ficheiro
        file = open(path + '/' + file_name + '.html',"wb")
                
        # escreve o caminho da página
        descriptive_path = 'Rebides/' + title

        # inicia a página
        self.start_page(file, descriptive_path, path, column_names)
        
        # adiciona conteúdo
        for row in data:
            file.write('<tr>')
            for column in row:
                try:
                    encoded_column = column.encode('utf-8')
                    file.write('<td>{0}</td>'.format(encoded_column))
                except:
                    file.write('<td>{0}</td>'.format(column))
                    continue
                pass
                
                # guarda o último valor
                last_column = encoded_column
            pass
            file.write('</tr>')
        pass
        
        # conclui a página
        self.end_page(file, descriptive_path, path)
    pass
    
    
    #---------------------------------------
    # Inicia uma página baseada em tabelas e adiciona-lhe o cabeçlho
    #
    #   file                - o fichiero onde escrever
    #   descriptive_path    - o caminho em texto para o ficheiro
    #   path                - o caminho do ficheiro
    #   column_names        - os nomes das colunas a serem adicionados
    #---------------------------------------
    def start_page(self, file, descriptive_path, path, column_names):
        
        # escreve o caminho da página
        self.page_path(file, descriptive_path, path)
        
        # cria a tabela
        file.write('<html>')                                    # start html
        file.write('<body>')                                    # start body
        file.write('<table cellpadding="0" cellspacing="0">')   # start table
        
        # start Header Row
        file.write('<tr bgcolor={0}>'.\
            format(self.HEADER_COLOR))
        
        # escreve o nomes das colunas
        for name in column_names:
            file.write('<td>{0}</td>'.format(name.encode('utf-8')))
        pass
        
        # end header row
        file.write('</tr>')
        
    pass
    
    #---------------------------------------
    # Termina uma página baseada em tabelas e adiciona-lhe o caminho
    #
    #   file                - o fichiero onde escrever
    #   descriptive_path    - o caminho em texto para o ficheiro
    #   path                - o caminho do ficheiro
    #---------------------------------------
    def end_page(self, file, descriptive_path, path):
        
        # termina a página
        file.write('</table>')   # close table
        file.write('</body>')    # close body
        file.write('</html>')    # close html
        
        # escreve o caminho da página
        file.write('<br><br><br>')
        self.page_path(file, descriptive_path, path)
    pass
    
    #---------------------------------------
    # Escreve a path da página
    #
    #   file                      - ficheiro onde escrever
    #   descriptive_path          - caminho em texto para a página
    #   path                      - caminho para a página
    #---------------------------------------
    def page_path(self, file, descriptive_path, path):
        
        # divide o caminho
        splitted_path = path.split('/')
        descriptions = descriptive_path.split('/')
        
        # relaciona o caminho com a root
        folder_path = ''
        for x in range(len(splitted_path) + 1):
            folder_path = folder_path + '../'
        print folder_path
            
        # escreve o primeiro caminho à parte porque a root
        # não é a pasta html, mas o servidor em sí
        file.write('| <a href={0}>{1}</a> |'.format(folder_path, descriptions[0]))
        folder_path = folder_path + splitted_path[0] + '/'
        
        # escreve o restante caminho
        i = 1
        for folder in splitted_path[1:len(splitted_path)]:
            folder_path = folder_path + folder + '/'
            file.write(' <a href={0}>{1}</a> |'.format(folder_path, descriptions[i]))
            
            # incrementa o indíce
            i = i + 1
        pass
    pass
    