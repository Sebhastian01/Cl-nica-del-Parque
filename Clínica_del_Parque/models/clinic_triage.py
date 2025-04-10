from odoo import models, fields

class ClinicTriage(models.Model):
    _name = 'clinic.triage'
    _description = 'Triage'

    name = fields.Char(string='Referencia')
    patient_id = fields.Many2one('clinic.patient', string='Paciente')
    state = fields.Selection([
        ('espera', 'En espera'),
        ('evaluado', 'Evaluado'),
        ('transferido', 'Transferido'),
    ], string='Estado', default='espera')
    notes = fields.Text(string='Notas')
