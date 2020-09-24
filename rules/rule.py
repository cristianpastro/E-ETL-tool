#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:38:01 2020

@author: cristian
"""


class Rule(object):
    """
    Esta classe implementa a entidade Regra

    Attributes
    ----------
    priority : int
        Prioridade de execução da regra.
    function : function
        Função que implementa o mapa da regra.
    """

    def __init__(self, priority: int, function):
        """
        Construtor da classe Rule.

        Parameters
        ----------
        priority : str
            Prioridade de execução da regra.
        function : type
            Função que implementa o mapa da regra.

        """

        self.priority = priority
        self.function = function

    def getPriority(self) -> int:
        """
        Foi necessário implementar um getter para a utilização na função ordenadora. Por padrão, ela
        não funciona chamando o atributo priority normalmente.

        Returns
        ----------
        priority : int
         Prioridade da regra

        """

        return self.priority
