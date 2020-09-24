#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 18:06:03 2020

@author: cristian
"""
from copy import deepcopy
from typing import List

from rules.basicsRules.auxFunctions import *


def fixStrInt(phenomenon_list: List[Phenomenon]) -> List[Phenomenon]:
    """
     Percorre os fenômenos da lista phenomenon_list invocando a conversão de string para inteiro,
     quando necessário

     Parameters
     ----------
     phenomenon_list : list of phenomenon
         lista de fenômenos que deseja-se fazer a conversão. A conversão ocorre quando houver uma
         tag com tipo string, mas com setup correspondente inteiro

    Returns
     ----------
     Retorna uma lista de fenômenos corrigidos

     """

    phenomenon_list_copy = deepcopy(phenomenon_list)
    for Phenom in phenomenon_list_copy:
        basicConvert(Phenom, int, str, int_conv)
    return phenomenon_list_copy


def FixFloatInt(phenomenon_list: List[Phenomenon]) -> List[Phenomenon]:
    """
     Percorre os fenômenos da lista phenomenon_list invocando a conversão de float para inteiro,
     quando necessário

     Parameters
     ----------
     phenomenon_list : list of phenomenon
         lista de fenômenos que deseja-se fazer a conversão. A conversão ocorre quando houver uma
         tag com tipo float, mas com setup correspondente inteiro

    Returns
     ----------
     Retorna uma lista de fenômenos corrigidos
     """

    phenomenon_list_copy = deepcopy(phenomenon_list)
    for Phenom in phenomenon_list_copy:
        basicConvert(Phenom, int, float, int_conv)
    return phenomenon_list_copy


def FixFloatDate(phenomenon_list: List[Phenomenon]) -> List[Phenomenon]:
    """
     Percorre os fenômenos da lista phenomenon_list invocando a conversão de float para datetime python,
     quando necessário

     Parameters
     ----------
     phenomenon_list : list of phenomenon
         lista de fenômenos que deseja-se fazer a conversão. A conversão ocorre quando houver uma
         tag com tipo float, mas com setup correspondente datetime python

    Returns
     ----------
     Retorna uma lista de fenômenos corrigidos
     """

    phenomenon_list_copy = deepcopy(phenomenon_list)
    for Phenom in phenomenon_list_copy:
        basicConvert(Phenom, type(datetime.today()), float, xldate_to_datetime)
    return phenomenon_list_copy


def FixStrDate(phenomenon_list: List[Phenomenon]) -> List[Phenomenon]:
    """
     Percorre os fenômenos da lista phenomenon_list invocando a conversão de string para datetime python,
     quando necessário

     Parameters
     ----------
     phenomenon_list : list of phenomenon
         lista de fenômenos que deseja-se fazer a conversão. A conversão ocorre quando houver uma
         tag com tipo string, mas com setup correspondente datetime python

    Returns
     ----------
     Retorna uma lista de fenômenos corrigidos
     """

    phenomenon_list_copy = deepcopy(phenomenon_list)
    for Phenom in phenomenon_list_copy:
        basicConvert(Phenom, type(datetime.today()), str, dateConf)
    return phenomenon_list_copy
