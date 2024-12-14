// Copyright (c) 2024, Bittu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ticket", {
	refresh(frm) {
        frm.add_custom_button("Aproved", function() {
            frappe.msgprint("Aproved")
            frappe.call({
                "method":"frappe.client.set_value",
                "args":{
                    doctype:"Ticket",
                    name:frm.doc.name,
                    "fieldname":{
                        "status":"Confirmed"
                    }
                },
            })
        });

	},
});
