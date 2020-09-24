#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 05 14:02:40 2020

@author: cristian
"""
from datetime import datetime, timedelta

from mainComponents.dataStores import Phenomenon


def basicConvert(p: Phenomenon, expected_type, found_type, conv_func):
    """
    Percorre um fenômeno e caso uma tag tenha um tipo diferente de seu setup, realiza a conversão,
    considerando os tipos esperado e encontrado passado como parâmetro.

    Parameters
    ----------
    p : Phenomenon
        Fenômeno ao qual deseja-se fazer a busca pelas tags com tipo diferente de seu setup.
    expected_type : type
        Tipo de dado esperado.
    found_type : type
        Tipo de dado realmente encontrado.
    conv_func : function
        Função que converte de found_type para expected_type.

    Returns
    ----------
    Retorna o número de falhas. Uma falha ocorre quando uma tag contém o tipo found_type, seu setup
    correspondente o tipo expected_type, mas algum erro ocorreu ao realizar a correção. Geralmente
    esse tipo de falha ocorre quando o formato do dado não foi previsto.

    """
    fails: int = 0
    for instance in p.dataInstanceList:
        for i, tag in enumerate(instance.listTag):
            if tag.TagType is found_type and p.IdTagList[i].IdTagType is expected_type and tag.TagValue:
                try:
                    tag.TagValue = conv_func(tag.TagValue)
                    tag.TagType = type(tag.TagValue)
                except ValueError:
                    fails += 1
    return fails


def int_conv(x):
    """
    Conversão simples para inteiro

    Parameters
    ----------
    x : undefined
        Variável para ser convertida para inteiro.

    Returns
    ----------
    Retorna a variável convertida

    """
    return int(x)


def dateConf(x):
    """
    Formata um datetime do python para uma string no formato dd/mm/aa

    Parameters
    ----------
    x : datetime
        datetime que deseja-se formatar para string.

    Returns
    ----------
    Retorna a variável convertida

    """
    return datetime.strptime(x, '%d/%m/%Y')


def xldate_to_datetime(xlr_date):
    """
    Converte um inteiro ou float contendo um datatime do excel e converte para python datetime

    Parameters
    ----------
    xlr_date : float, int
        datetime do excel que deseja-se formatar para datetime python.

    Returns
    ----------
    Retorna a variável convertida
    """

    temp_date = datetime(1900, 1, 1)
    delta_days = timedelta(days=int(xlr_date) - 2)
    the_time = (temp_date + delta_days)
    return the_time.strftime("%d/%m/%Y")
