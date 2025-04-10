from odoo import models, fields, api

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

    triage_ids = fields.One2many('clinic.triage', 'entry_id', string='Triage')
    state = fields.Selection([
        ('ingreso', 'Ingreso'),
        ('triage', 'Triage'),
    ], default='ingreso', string='Estado', required=True)

    @api.model
    def create(self, vals):
        # Crear el registro de ingreso
        record = super(PatientEntry, self).create(vals)
        
        # Cambiar el estado a triage automáticamente al crear el registro
        record.state = 'triage'
        
        # Crear el registro de triage automáticamente
        self.env['clinic.triage'].create({
            'name': f'Triage de {record.name}',
            'patient_id': record.id,
            'entry_id': record.id,
        })
        
        return record
