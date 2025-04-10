from odoo import models, fields

class ClinicTriage(models.Model):
    _name = 'clinic.triage'
    _description = 'Triage'

    name = fields.Char(string='Referencia', required=True)
    patient_id = fields.Many2one('clinic.patient.entry', string='Paciente', required=True)
    entry_id = fields.Many2one('clinic.patient.entry', string='Ingreso', required=True)
    state = fields.Selection([
        ('espera', 'En espera'),
        ('evaluado', 'Evaluado'),
        ('transferido', 'Transferido'),
    ], default='espera', string='Estado', required=True)
    notes = fields.Text(string='Notas')



