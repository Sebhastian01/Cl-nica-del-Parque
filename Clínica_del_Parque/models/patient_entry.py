from odoo import models, fields

class PatientEntry(models.Model):
    _name = 'clinic.patient.entry'
    _description = 'Ingreso de Paciente'
    _order = 'create_date desc'

    name = fields.Char(string='Nombre del Paciente', required=True)
    birth_date = fields.Date(string='Fecha de Nacimiento')
    contact = fields.Char(string='Teléfono/Email')
    companion = fields.Char(string='Acompañante')
    reason = fields.Text(string='Motivo de Ingreso')
    signature = fields.Binary(string='Firma Digital')
    clinical_file_created = fields.Boolean(string='Ficha Clínica Creada', default=False)
