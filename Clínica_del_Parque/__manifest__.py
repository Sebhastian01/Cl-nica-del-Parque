{
    'name': 'Clínica del Parque',
    'version': '1.0',
    'category': 'Healthcare',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_entry_views.xml',
        'views/clinic_triage_views.xml',
    ],
    'installable': True,
    'application': True,
}