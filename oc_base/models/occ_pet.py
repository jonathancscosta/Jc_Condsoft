#-*-coding: utf-8 _*_
from dataclasses import fields
from oc_base import models
from openerp import model, fields


class OccPet (models.Model):
    _name ='occ.pet'
    _description ='Tipos de pets'
    _order = 'name'
    _table = 'occ_pet'
    _sql_constraints = [('occ.pet', 'UNIQUE(name)',
                        'Os nomes dos pets devem ser únicos')]
    active = fields.Boolean('ativo', default = True)
    name =fields.Char('pet',size =4, required= True)
    morador_ids =fields.One2many('occ.morador','apto_id',
                        'moradores neste Apartamento')
    bloco_id = fields.Many2one ('occ.bloco', 'Bloco' 
 ondelete ="cascade", required=True) 