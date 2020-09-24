#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:33:58 2020

@author: cristian
"""


def Psi(pin, r):
    """
    Função Psi que executa uma regra

    Parameters
    ----------
    pin : list of Phenomenon
        Conjunto de fenômenos de entrada para a regra.
    r : rule
        Regra a ser executada.

    Returns
    ----------
    Retorna o resultado da função atributo da regra

    """
    return r.function(pin)
