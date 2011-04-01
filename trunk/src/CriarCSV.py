# -*- coding: utf-8 -*-

# escrita em csv
import csv

class CriarCSV:
    
    def escrita_csv(self, ano):
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