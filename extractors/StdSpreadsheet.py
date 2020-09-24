#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:03:24 2020

@author: cristian
"""

import xlrd
import functools


class LoadSheet(object):
    """
    Esta classe contém métodos para carregar dados de um arquivo .xls ou .xlsx e salvar em uma lista
    contendo todas as linhas desse arquivo. A primeira linha do arquivo deve ser o cabeçalho.

    Attributes
    ----------
    datas : list of lists
        Contém uma lista de linhas do arquivo lido. Cada elemento da lista contém as colunas de
    dados do arquivo lido.

    """

    def __init__(self, pwd):
        """        
        Construtor da classe.
        
        Parameters
        ----------
        pwd : str
            Planilha .xls ou .xlsx que deseja-se carregar os dados. A extensão do arquivo
            deve estar presente nesse nome.
        
        Notes
        -----
        A primeira linha da planilha é sempre o seu cabeçalho.
        
        """

        #Abre apenas a primeira planilha do arquivo.
        book = xlrd.open_workbook(pwd)
        n_sheets = book.nsheets
        self.datas = []
        for curr_sheet in range(n_sheets):

            sheet = book.sheet_by_index(curr_sheet)

            #Lê o cabeçalho do arquivo
            self.header = []
            for curr_col in range(0, sheet.ncols):
                self.header.append(sheet.cell_value(rowx=0, colx=curr_col))

            #Começa a ler os dados em si
            #A primeira linha deve ser excluída por ser o cabeçalho
            for curr_row in range(1, sheet.nrows):
                if n_sheets > 1:
                    row_data = [str(sheet.name)]
                else:
                    row_data = []
                for curr_col in range(0, sheet.ncols):
                    value = sheet.cell_value(rowx=curr_row, colx=curr_col)
                    row_data.append(value)
                self.datas.append(row_data)

        #Ordena a lista de dados criada
        self.sort_datas()

    def sort_datas(self):
        """        
        Ordena a lista de dados.
        
        
        Notes
        -----
        O critério de ordenação é o primeiro elemento das listas internas. O critério de desempate
        é o segundo elemento das listas internas. Caso o empate persista, o critério de desempate
        passa a ser o terceiro, quarto,... elemento das listas internas.
        
        """

        def compare(list1, list2):
            for e1, e2 in zip(list1, list2):
                if str(e1) != str(e2):
                    return 1 if str(e1) > str(e2) else -1
            return 0
        self.datas = sorted(self.datas, key=functools.cmp_to_key(compare))
