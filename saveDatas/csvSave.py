#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:00:03 2020

@author: cristian
"""
import csv


def csvSave(filename, data_set):
    """
     Salva um conjunto de dados em um arquivo csv

     Parameters
     ----------
     filename : str
         Nome do arquivo que será salvo (sem o .csv no final)
     data_set : list of list
         Lista contendo listas, no qual cada lista interna representa uma linha que será salva
         no arquivo csv

     """

    with open(filename + '.csv', 'a') as arquivo_csv:
        write = csv.writer(arquivo_csv, delimiter=';', lineterminator='\n')
        for line in data_set:
            write.writerow(line)
