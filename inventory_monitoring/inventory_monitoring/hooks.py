from inventory_monitoring import __version__ as app_version

app_name = "inventory_monitoring"
app_title = "Inventory Monitoring"
app_publisher = "Ark143"
app_description = "Advanced Inventory Monitoring for ERPNext v15"
app_email = "your.email@example.com"
app_license = "MIT"

# Required for ERPNext
required_apps = ["erpnext"]

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

# Installation
# ------------

# before_install = "inventory_monitoring.install.before_install"
# after_install = "inventory_monitoring.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "inventory_monitoring.uninstall.before_uninstall"
# after_uninstall = "inventory_monitoring.uninstall.after_uninstall"

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