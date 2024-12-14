import frappe
from frappe.website.website_generator import WebsiteGenerator

class Ticket(WebsiteGenerator):
    def validate(self):
        ticket_doc = frappe.get_doc("Theater show", self.theater_show)
        cinema = ticket_doc.movie_theater

        # Check if the status is 'Confirmed' and email field exists
        contexts = {
        "doc": {
            "ticket_id": self.ticket_id,
            "customer_name": self.customer,
            "seat_number": self.seat_number,
            "movie":self.movie,
            "cinema":cinema,
            
        }
    }
        if self.status == "Confirmed" and self.email:
            frappe.sendmail(
                recipients=[self.email],
                subject="Ticket Confirmation",
                message="Hey, your ticket has been confirmed!",
                template='send',
                # args={"ticket_id": self.ticket_id, "customer_name": self.customer},
                args=contexts,
                as_markdown=False,
            )
       
				

