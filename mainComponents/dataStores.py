#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:43:03 2020

@author: cristian
"""

from extractors.StdSpreadsheet import *


class Setup(object):
    """
    Esta classe implementa a entidade IdTag

    Attributes
    ----------
    id_tag_name : str
        Identificador da Tag.
    id_tag_type : type
        Tipo da IdTag.
    """

    def __init__(self, id_tag_name, id_tag_type):
        """        
        Construtor da classe IdTag.
        
        Parameters
        ----------
        id_tag_name : str
            Nome da IdTag.
        id_tag_type : type
            Tipo esperado para a IdTag.

        """
        self.IdTagName = id_tag_name
        self.IdTagType = id_tag_type

    def __str__(self):
        return '(' + str(self.IdTagName) + ', ' + str(self.IdTagType) + ')'


class Tag(object):
    """
    Esta classe implementa a entidade Tag.

    Attributes
    ----------
    tag_value : undefined
        Valor da Tag.
    TagType : type
        Tipo da Tag, identificado automaticamente.

    """

    def __init__(self, tag_value):
        self.TagValue = tag_value
        self.TagType = type(tag_value)

    def __str__(self):
        return '(' + str(self.TagValue) + ',' + str(self.TagType) + ')'


class Instance(object):
    """
    Esta classe implementa a entidade Instância.

    Attributes
    ----------
    list_tag : list of tag
        Lista de tags da referida Instância.
    datas : undefined
        Dados

    """

    def __init__(self, list_tag):
        """        
        Construtor da Classe Instance.
        
        Parameters
        ----------
        list_tag : list of Tag
            Lista de Tags valuadas da referida instância.

        """
        self.listTag = list_tag  # Lista de Tags da instância
        self.datas = []  # Dados da instância

    def append_data(self, new_data):
        """        
        Adiciona um novo dado à Instância.
        
        Parameters
        ----------
        new_data : undefined
            Dado a ser adicionado.
        
        """
        self.datas.append(new_data)

    def __str__(self):
        str_returned = []
        for item in self.listTag:
            str_returned.append(str(item) + ' ')

        str_returned.append(str(self.datas) + ' ')

        return ''.join(str_returned)


class Phenomenon(object):
    """
    Esta classe implementa a entidade Fenômeno.

    Attributes
    ----------
    tuple_tag_list : list of tuple
        Lista de Tuplas no formato (Nome da IdTag, Tipo da Idtag), no qual o Nome
         da IdTag é do tipo str e o TIpo da IdTag é do tipo type.
    dataInstanceList : list of Instance
        Contém a lista de instâncias presentes no Fenômeno.

    """
    def __init__(self, tuple_tag_list):
        """        
        Construtor da classe Phenomenon.
        
        Parameters
        ----------
        tuple_tag_list : list of tuples
            Lista de tuplas no formato (nome_da_id_tag, tipo_da_id_tag)
        """

        self.IdTagList = []
        for item in tuple_tag_list:
            self.IdTagList.append(Setup(item[0], item[1]))

        self.dataInstanceList = []  # Lista de instâncias de dados

    def append_instance(self, instance):
        """
        Adiciona uma instância ao fenômeno.

        Parameters
        ----------
        instance : Instance
            Instância a ser adicionada.
        """
        self.dataInstanceList.append(instance)

    def from_xls_data(self, pwd):
        """        
        Carrega um arquivo .xls ou .xlsx, criando as instâncias, tags e dadoss correspondentes.
        
        Parameters
        ----------
        pwd : str
            Nome da planilha a ser carregada.
        
        Notes
        -------
        A lista de dados não ficará na ordem das linhas da planilha. Ela será ordenada.
        """

        def convert_to_tag_list(var_list):
            tag_list = []
            for itm in var_list:
                tag_list.append(Tag(itm))
            return tag_list

        list_datas = LoadSheet(pwd)

        past_list_tag = []
        new_instance = []

        for lineValue in list_datas.datas:
            # Verifica as tags da linha atual
            curr_act_list_tag = []
            count_tag = 0

            # Captura o valor das tags na linha atual
            for tagName, tagValue in zip(self.IdTagList, lineValue):
                curr_act_list_tag.append(tagValue)
                count_tag += 1

            # Verifica os dados da linha atual
            new_data = []
            for item in lineValue[count_tag:]:
                new_data.append(item)
            if curr_act_list_tag != past_list_tag:
                if new_instance:
                    self.append_instance(new_instance)
                new_instance = Instance(convert_to_tag_list(curr_act_list_tag))

            new_instance.append_data(new_data)
            past_list_tag = curr_act_list_tag

    def __str__(self):
        str_returned = ['Id_Tag list: ']
        for item in self.IdTagList:
            str_returned.append(str(item) + ' ')
        str_returned.append('\n')
        for item in self.dataInstanceList:
            str_returned.append(str(item) + '\n')

        return ''.join(str_returned)
