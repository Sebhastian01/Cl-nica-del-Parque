from odoo import models, fields, api

class ConsultaMedica(models.Model):
    _name = 'clinic.consulta'
    _description = 'Consulta Médica'

    name = fields.Char(string='Referencia', required=True)
    patient_id = fields.Many2one('clinic.patient.entry', string='Paciente', required=True)
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizada', 'Finalizada'),
    ], default='pendiente', string='Estado', required=True)
    notes = fields.Text(string='Notas')

    @api.model
    def create(self, vals):
        """
        Se pueden agregar acciones personalizadas al momento de crear una consulta.
        Por ejemplo, cambiar el estado del paciente, etc.
        """
        # Crear el registro de consulta médica
        record = super(ConsultaMedica, self).create(vals)

        # Si es necesario, puedes realizar alguna acción adicional, como cambiar el estado
        # del paciente o realizar otras validaciones.
        return record
