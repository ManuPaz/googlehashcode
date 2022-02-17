#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:27:27 2022

@author: manuel
"""
class clase:
    def __init__(self,identificador,nombre):
        self.identificador=identificador
        self.nombre=nombre
      
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, clase):
            return self.identificador == other.identificador
        return False