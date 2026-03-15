app_name = "role_workspaces_app"
app_title = "Role Workspaces"
app_publisher = "Admin"
app_description = "Automatic role based workspace provisioning"
app_email = "ph.tamir@gmail.com"
app_license = "MIT"

after_install = "role_workspaces_app.install.create_workspaces"
before_uninstall = "role_workspaces_app.install.delete_workspaces"