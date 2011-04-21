# -*- coding: utf-8 -*-

# escrita em csv
import csv

class CriarCSV:
    
    #----------------------------
    # Escreve informação no formato CSV
    #
    #   title       - título do CSV
    #   csv_name    - nome do csv
    #   data        - data a ser inserida no CSV
    #----------------------------
    def escrita_csv(self, title, csv_name, data):
        print "escrita csv"
        CSV_PATH = 'csv/'
        
        ficheiro = open(CSV_PATH + csv_name + '.csv',"wb")
        csvwriter = csv.writer( ficheiro, delimiter=',')

        # escrever título
        csvwriter.writerow(('----------------------------------------------',))
        csvwriter.writerow((title.encode('utf-8'),))
        csvwriter.writerow(('----------------------------------------------',))
                
        # escreve o conteúdo
        for row in data:
            encoded_row = []
            i = 0
            for column in row:

                try:
                    encoded_column = column.encode('utf-8')
                    encoded_row.append(encoded_column)
                except:
                    encoded_column = str(column)
                    encoded_row.append(encoded_column)
                    continue
                pass

                
            pass

            csvwriter.writerow(encoded_row)
        pass

        # fecha o ficheiro
        ficheiro.close()
    pass
    