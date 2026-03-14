import frappe
import json
from role_workspaces_app.workspace_definitions import WORKSPACE_DEFINITIONS


def create_workspaces():

    for ws in WORKSPACE_DEFINITIONS:
        create_single_workspace(ws)


def create_single_workspace(config):

    if frappe.db.exists("Workspace", config["label"]):
        return

    content = build_workspace_content(config)

    workspace = frappe.get_doc({
        "doctype": "Workspace",
        "label": config["label"],
        "title": config["label"],
        "module": config["module"],
        "icon": config["icon"],
        "indicator_color": config["color"],
        "public": 1,
        "sequence_id": config["sequence"],
        "content": json.dumps(content),
        "roles": [
            {"role": config["role"]}
        ]
    })

    workspace.insert(ignore_permissions=True)


def build_workspace_content(config):

    content = []

    content.append({
        "type": "header",
        "data": {
            "text": config["label"]
        }
    })

    for section in config["sections"]:

        content.append({
            "type": "header",
            "data": {
                "text": section["title"]
            }
        })

        for shortcut in section["shortcuts"]:

            content.append({
                "type": "shortcut",
                "data": {
                    "shortcut_name": shortcut,
                    "type": "DocType",
                    "doc_view": "List"
                }
            })

    return content


def delete_workspaces():

    for ws in WORKSPACE_DEFINITIONS:

        if frappe.db.exists("Workspace", ws["label"]):
            frappe.delete_doc(
                "Workspace",
                ws["label"],
                ignore_permissions=True
            )