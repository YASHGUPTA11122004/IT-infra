from odoo import fields, models


class Computer(models.Model):

    _name = "it_infra.computer"
    _inherit = "it_infra.equipment"
    _description = "Computer"

    user_id = fields.Many2one(comodel_name="res.users", string="User")

    username = fields.Char(required=False)

    office = fields.Char()

    os_id = fields.Many2one(
        comodel_name="it_infra.software",
        string="Operating System",
        domain=[("category_id.parent_id", "ilike", "Operating System")],
        required=False,
    )

    hardware_data = fields.Html()

    _sql_constraints = [
        ("name_unique", "unique(name)", "Computer name must be unique!"),
        (
            "ip_address_unique",
            "unique(ip_address)",
            "Computer IP address must be unique!",
        ),
        (
            "hostname_unique",
            "unique(hostname)",
            "Computer hostname must be unique!",
        ),
    ]
