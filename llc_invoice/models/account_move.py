from odoo import fields, api, models

class AccountMove(models.Model):

    _inherit = "account.move"

    def action_receipt_print(self):
        report_name = "llc_invoice.shopee_official_receipt"
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": f"/report/pdf/{report_name}/{self.id}?enable_editor=1",
        }