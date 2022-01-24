#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:13:48 2022

@author: manuel
"""
class feature:
    def __init__(self,identificador,nombre,beneficio,dificultad,servicios,listaServicios):
        self.identificador=identificador
        self.nombre=nombre
        self.beneficio=beneficio
        self.dificultad=dificultad
        self.servicios=servicios
        self.listaServicios=[]
        self.serviciosImplementados=[]
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, feature):
            return self.identificador == other.identificador
        return False
    
class binary:
    def __init__(self,identificador):
        self.identificador=identificador
        self.listaservicios=[]
        self.listaserviciosCambiados=[]
        self.featuresImplementados=[]
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, binary):
            return self.identificador == other.identificador
        return False
class servicio:
    def __init__(self,identificador,nombre):
        self.indentificador=identificador
        self.nombre=nombre
        self.features=[]
        self.featuresImplementados=[]
        self.cambiado=False
        def __eq__(self, other):
            """Overrides the default implementation"""
            if isinstance(other, servicio):
                return self.identificador == other.identificador
            return False
        