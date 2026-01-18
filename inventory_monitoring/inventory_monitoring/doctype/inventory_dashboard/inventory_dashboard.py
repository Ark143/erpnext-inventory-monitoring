# Copyright (c) 2026, Ark143 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class InventoryDashboard(Document):
	def before_save(self):
		if not self.created_by:
			self.created_by = frappe.session.user
		self.modified_by = frappe.session.user
	
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
	
	def get_low_stock_items(self, limit=10):
		"""Get items with low stock"""
		return frappe.db.sql("""
			SELECT 
				b.item_code,
				b.actual_qty,
				i.item_name,
				i.stock_uom,
				COALESCE(i.reorder_level, 0) as reorder_level
			FROM `tabBin` b
			LEFT JOIN `tabItem` i ON b.item_code = i.name
			WHERE b.actual_qty <= COALESCE(i.reorder_level, 0)
			AND b.actual_qty >= 0
			ORDER BY b.actual_qty ASC
			LIMIT %s
		""", (limit,), as_dict=True)
	
	def get_stock_movement_trend(self, days=30):
		"""Get stock movement trend for specified days"""
		return frappe.db.sql("""
			SELECT 
				DATE(posting_date) as date,
				SUM(CASE WHEN actual_qty > 0 THEN actual_qty ELSE 0 END) as inward,
				SUM(CASE WHEN actual_qty < 0 THEN ABS(actual_qty) ELSE 0 END) as outward
			FROM `tabStock Ledger Entry`
			WHERE posting_date >= DATE_SUB(CURDATE(), INTERVAL %s DAY)
			GROUP BY DATE(posting_date)
			ORDER BY posting_date DESC
		""", (days,), as_dict=True)