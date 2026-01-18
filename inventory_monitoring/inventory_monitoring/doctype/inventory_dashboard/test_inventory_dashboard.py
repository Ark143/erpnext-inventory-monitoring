# Copyright (c) 2026, Ark143 and Contributors
# See license.txt

import frappe
import unittest

class TestInventoryDashboard(unittest.TestCase):
	def test_dashboard_creation(self):
		dashboard = frappe.get_doc({
			"doctype": "Inventory Dashboard",
			"dashboard_name": "Test Dashboard",
			"description": "Test inventory dashboard",
			"is_active": 1
		})
		dashboard.insert()
		self.assertTrue(dashboard.name)
		dashboard.delete()