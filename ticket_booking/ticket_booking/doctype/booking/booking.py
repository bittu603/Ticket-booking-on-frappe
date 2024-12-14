import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime,getdate  # Import the function to get the current datetime

class Booking(Document):
   
    def validate(self):
        release_date = getdate(self.release_date)
        book_date = getdate(self.book_date)   
    
        
        
        
        if self.paid == 1:
            frappe.msgprint("Booking has been paid.")
            if book_date < release_date:
                frappe.throw("Please Select a Valid Date")
        else:
            frappe.throw("please check the paid button")
        
            exists = frappe.db.exists('Booking', {
                'theater_show': self.theater_show,
            })
            if exists:
                frappe.throw(f"A booking already exists with this theater show '{self.theater_show}'.")
        
        ticket = frappe.new_doc('Ticket')
        ticket.ticket_id = self.name 
        ticket.status = "Pending"
        ticket.theater_show = self.theater_show 
        ticket.customer = self.customer_name  
        ticket.booking_time = now_datetime()  
        # ticket.seat_number = self.seat_number 
        ticket.num_ticket = self.num_ticket  
        ticket.movie = self.movie  
        ticket.email = self.email
        ticket.is_published = 1

        ticket.insert()  # This line saves the ticket automatically
        frappe.msgprint("Ticket created successfully.")







