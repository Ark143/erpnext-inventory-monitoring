# Copyright (c) 2026, Ark143 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class InventoryDashboard(Document):
	def get_stock_summary(self):
		"""Get stock summary for dashboard"""
		return frappe.db.sql("""
			SELECT 
				COUNT(*) as total_items,
				SUM(actual_qty) as total_qty,
				SUM(stock_value) as total_value
			FROM `tabBin`
			WHERE actual_qty > 0
		""", as_dict=True)[0]