# Copyright 2012, Israel Cruz Argil, Argil Consulting
# Copyright 2016, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Freight Management',
    'version': '14.0.1.0.0',
    'category': 'Transport',
    'author': 'Jarsa Sistemas, Argil Consulting',
    'website': 'https://www.jarsa.com.mx/page/transport-management-system',
    'depends': [
        'account_operating_unit',
        'fleet',
        'hr',
    ],
    'external_dependencies': {
        'python': [
            'sodapy',
            'num2words',
            'responses',
        ],
    },
    'summary': 'Management System for Carriers, Trucking and other companies',
    'license': 'AGPL-3',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/tms_view.xml',
        'data/ir_sequence_data.xml',
        'data/account_journal_data.xml',
        'views/operating_unit_view.xml',
        'views/fleet_vehicle_odometer_view.xml',
        'views/hr_employee_view.xml',
        'views/fleet_vehicle_view.xml',
        'views/fleet_vehicle_log_fuel_view.xml',
        'views/fleet_vehicle_log_fuel_prepaid_view.xml',
        'views/product_template_view.xml',
        'views/tms_advance_view.xml',
        'views/tms_event_view.xml',
        'views/tms_expense_view.xml',
        'views/tms_expense_line_view.xml',
        'views/tms_expense_loan_view.xml',
        'views/tms_factor_view.xml',
        'views/tms_place_view.xml',
        'views/tms_route_view.xml',
        'views/tms_transportable_view.xml',
        'views/tms_travel_view.xml',
        'views/tms_unit_kit_view.xml',
        'views/tms_waybill_view.xml',
        'views/tms_extradata_view.xml',
        'views/account_move_view.xml',
        'views/tms_route_tollstation_view.xml',
        'views/fleet_vehicle_engine_view.xml',
        'views/tms_route_note_view.xml',
        'data/product_product_data.xml',
        'data/operating_unit.xml',
        'wizards/tms_wizard_payment_view.xml',
        'wizards/tms_wizard_invoice_view.xml',
        'report/travel_instructions_letter.xml',
        'report/expense_report.xml',
        'data/ir_config_parameter.xml',
    ],
    'demo': [
        'demo/ir_sequence.xml',
        'demo/product_product.xml',
        'demo/product_template.xml',
        'demo/fleet_vehicle_odometer.xml',
        'demo/operating_unit.xml',
        'demo/fleet_vehicle_engine.xml',
        'demo/fleet_vehicle_model_brand.xml',
        'demo/fleet_vehicle.xml',
        'demo/hr_employee.xml',
        'demo/tms_place.xml',
        'demo/tms_route.xml',
        'demo/tms_travel.xml',
        'demo/fleet_vehicle_log_fuel.xml',
        'demo/tms_advance.xml',
        'demo/tms_route_fuelefficiency.xml',
        'demo/tms_transportable.xml',
        'demo/tms_unit_kit.xml',
    ],
    'application': True,
    'installable': True,
}
