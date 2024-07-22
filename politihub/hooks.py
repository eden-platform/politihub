from . import __version__ as app_version

app_name = "politihub"
app_title = "PolitiHub"
app_publisher = "Don't Panic Consulting, Co."
app_description = "Political Party Management and Collaboration tools."
app_email = "devs@dpcco.me"
app_license = "AGPLv3"
app_icon_url = "/assets/politihub/manifest/favicon-180.png"
app_icon_title = "PolitiHub"
app_icon_route = "/g"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/politihub/css/politihub.css"
# app_include_js = "/assets/politihub/js/politihub.js"

# include js, css files in header of web template
# web_include_css = "/assets/politihub/css/politihub.css"
# web_include_js = "/assets/politihub/js/politihub.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "politihub/public/scss/website"

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

# Fixtures

fixtures = [
	{"dt": "Role", "filters": [["role_name", "like", "Gameplan %"]]},
]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

website_route_rules = [
	{"from_route": "/g/<path:app_path>", "to_route": "g"},
]

website_redirects = [
	{"source": r"/teams(/.*)?", "target": r"/g\1"},
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "politihub.utils.jinja_methods",
# 	"filters": "politihub.utils.jinja_filters"
# }

# Installation
# ------------

before_install = "politihub.install.before_install"
after_install = "politihub.install.after_install"

after_migrate = ["politihub.search.build_index_in_background"]

# Uninstallation
# ------------

# before_uninstall = "politihub.uninstall.before_uninstall"
# after_uninstall = "politihub.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "politihub.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"*": {
		"on_trash": "politihub.mixins.on_delete.on_trash",
	},
	"User": {
		"after_insert": "politihub.politihub.doctype.gp_user_profile.gp_user_profile.create_user_profile",
		"on_trash": [
			"politihub.politihub.doctype.gp_user_profile.gp_user_profile.delete_user_profile",
			"politihub.politihub.doctype.gp_guest_access.gp_guest_access.on_user_delete",
		],
		"on_update": "politihub.politihub.doctype.gp_user_profile.gp_user_profile.on_user_update"
	}
}

on_login = 'politihub.www.g.on_login'

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		"politihub.search.build_index_if_not_exists"
	],
	"hourly": [
		"politihub.politihub.doctype.gp_invitation.gp_invitation.expire_invitations"
	],
}

# scheduler_events = {
# 	"all": [
# 		"politihub.tasks.all"
# 	],
# 	"daily": [
# 		"politihub.tasks.daily"
# 	],
# 	"hourly": [
# 		"politihub.tasks.hourly"
# 	],
# 	"weekly": [
# 		"politihub.tasks.weekly"
# 	],
# 	"monthly": [
# 		"politihub.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "politihub.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.client.get_list": "politihub.extends.client.get_list"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "politihub.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"politihub.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
