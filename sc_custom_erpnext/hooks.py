# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sc_custom_erpnext"
app_title = "SC Custom ERPNext"
app_publisher = "unknownTH"
app_description = "ERPNext customisations for Sora Choi"
app_icon = "octicon octicon-gear"
app_color = "grey"
app_email = "unknown"
app_license = "GNU General Public License"
hide_in_installer = True
fixtures = [
	{"dt":"Custom Field", "filters": [["Fieldname", "in", ("is_consignment_transaction")]]},
	"Custom Script",
	{"dt":"Print Format", "filters": [["Module", "in", ("SC Custom ERPNext")]]}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/sc_custom_erpnext/css/desk.css"
# app_include_js = "/assets/sc_custom_erpnext/js/sc_custom_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/sc_custom_erpnext/css/sc_custom_erpnext.css"
# web_include_js = "/assets/sc_custom_erpnext/js/sc_custom_erpnext.js"

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

# Website user home page (by function)
# get_website_user_home_page = "sc_custom_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sc_custom_erpnext.install.before_install"
# after_install = "sc_custom_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sc_custom_erpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
 	"Sales Invoice": {
		"validate": "sc_custom_erpnext.sc_custom_erpnext.controllers.sales_invoice.validate",
		"on_submit": "sc_custom_erpnext.sc_custom_erpnext.controllers.sales_invoice.on_submit",
		"on_cancel": "sc_custom_erpnext.sc_custom_erpnext.controllers.sales_invoice.on_cancel"
	},	
	"Delivery Note": {
		"validate": "sc_custom_erpnext.sc_custom_erpnext.controllers.delivery_note.validate",
		"on_submit": "sc_custom_erpnext.sc_custom_erpnext.controllers.delivery_note.on_submit",
		"on_cancel": "sc_custom_erpnext.sc_custom_erpnext.controllers.delivery_note.on_cancel"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sc_custom_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"sc_custom_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"sc_custom_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sc_custom_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sc_custom_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sc_custom_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sc_custom_erpnext.event.get_events"
# }

