# -*- coding: utf-8 -*-

# Estes imports servem para não dar erros de Bad Screen Distance 320
import matplotlib
matplotlib.use('QT4Agg')
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

# imports do gráfico
import matplotlib.pyplot as plt

#---------------------------------------
# Classe responsável por gerar gráficos
# Autor: Bruno Moreira
# Número: 6170
#---------------------------------------

class Graphs:
    
    def __init__(self, data, title):

        x = []                          # valores do eixo dos x's
        y = []                          # valores do eixo dos y's
        xlabel = []
        ind = []                        # índice

        bar_width = (0.1)               # largura das barras
        FONT_SIZE = 10                  # tamanho da fonte
        
        for row in data:
            print row
            x.append(row[0])
            y.append(row[len(row)-1])
            xlabel.append(row[len(row)-2])

        ind = range(len(xlabel))

        plt.bar(ind, y, width=bar_width, bottom=0, color='g')
        plt.plot(y)
        plt.xticks( ind, xlabel, horizontalalignment='right', rotation=45 )
        plt.title(title)
        plt.grid(True)
        plt.show()

        pass
    pass
    