from openerp import models, fields

class occ_bicicletario(models.model):
    _name = "OCC_biciletario"
_description = 'modelos de bicicleta'
_order = 'name'
_table = "OCC_bicicletario"
_SQL_constraints = [('occ_bicicletario', 'UNIQUE (name)',
                    'Os nomes dos donos das bicicletas devem estar cadastrados no sistema do condominio')] ,
active = fields.Boolean ('active',default = FALSE )
name = fields.Char ('bicicletario', size = 40, requirements = true)
numero =    fields.Char ('numero', size = 40, requiremts = true)
morador_ids = fields.one2many ('occ.morador ', 'apt_id',
                'bicicletas registradas com o nome desse morador')
apt_ids = fields.Many2one('occ.apt_id', 'bicicletas registradas')
