# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
# class securitypanel(models.Model):
#     _name = 'securitypanel.securitypanel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class equipo(models.Model):
    _name = 'securitypanel.equipo'
    imagen = fields.Binary()
    id = fields.Integer(String="Nº Equipo", required = True)
    sistema = fields.Char(String="Sistema Operativo")
    fechaInstalacion = fields.Date("Fecha de instalacion", required = True)
    description = fields.Text()
    planificador = fields.One2many("securitypanel.planificador","equipo", string="Modificacion Planificada")
    _sql_constraints = [
         ('PK_NM', 'unique (id)','Ese id ya existe')]

class responsable(models.Model):
    _name = 'securitypanel.responsable'
    imagen = fields.Binary()
    dni = fields.Char(String="DNI", required = True)
    nombre = fields.Char(String="Nombre", required = True)
    apellidos = fields.Char(String="Apellidos")
    telefono = fields.Integer(String="Telefono")

class planificador(models.Model):
    _name = 'securitypanel.planificador'
    id = fields.Integer(String="Nº Modificacion", required = True)
    fechaInstalacion = fields.Date("Fecha prevista", required = True)
    description = fields.Text()
    equipo = fields.Many2one("securitypanel.equipo", string="Equipo")
    responsable = fields.Many2many("securitypanel.responsable", string="Responsables")
    realizado = fields.Boolean()
    estado = fields.Char(compute="_dato_p", store=False)
    _sql_constraints = [
         ('PK_NM', 'unique (id)','Ese id ya existe')]

    @api.one
    @api.depends('fechaInstalacion','realizado')
    def _dato_p(self):
        if self.realizado == True:
            self.estado = "Realizado"
        else:
            tiempo1 = str(self.fechaInstalacion)
            tiempo2 = str(datetime.now())
            if tiempo1 >= tiempo2 :
                self.estado = "En espera"
            else:
                self.estado = "No realizado"
    @api.one
    def botonRealizar(self):
        if self.realizado == True:
            self.realizado = False
        else:
            self.realizado = True
