from . import __version__ as app_version

app_name = "inventory_monitoring"
app_title = "Inventory Monitoring"
app_publisher = "Ark143"
app_description = "Advanced Inventory Monitoring for ERPNext v15"
app_email = "your.email@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/inventory_monitoring/css/inventory_monitoring.css"
# app_include_js = "/assets/inventory_monitoring/js/inventory_monitoring.js"

# include js, css files in header of web template
# web_include_css = "/assets/inventory_monitoring/css/inventory_monitoring.css"
# web_include_js = "/assets/inventory_monitoring/js/inventory_monitoring.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "inventory_monitoring/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "inventory_monitoring.utils.jinja_methods",
#	"filters": "inventory_monitoring.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "inventory_monitoring.install.before_install"
# after_install = "inventory_monitoring.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "inventory_monitoring.uninstall.before_uninstall"
# after_uninstall = "inventory_monitoring.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "inventory_monitoring.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"inventory_monitoring.tasks.all"
#	],
#	"daily": [
#		"inventory_monitoring.tasks.daily"
#	],
#	"hourly": [
#		"inventory_monitoring.tasks.hourly"
#	],
#	"weekly": [
#		"inventory_monitoring.tasks.weekly"
#	],
#	"monthly": [
#		"inventory_monitoring.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "inventory_monitoring.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "inventory_monitoring.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "inventory_monitoring.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["inventory_monitoring.utils.before_request"]
# after_request = ["inventory_monitoring.utils.after_request"]

# Job Events
# ----------
# before_job = ["inventory_monitoring.utils.before_job"]
# after_job = ["inventory_monitoring.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"inventory_monitoring.auth.validate"
# ]