import frappe
@frappe.whitelist()
def get_unavailable_seats(theater_show):
        # doc = frappe.get_doc('Theater show', '')
        booked_seats = frappe.db.get_list(
            'Booking',
            filters={'theater_show': theater_show},
            fields=['seat_number']
        )
        return [seat['seat_number'] for seat in booked_seats]
# def get_unavailable_seats():
#     return frappe.msgprint("get_unavailable_seats11")
@frappe.whitelist()
def filter_seat_number(movie,book_date):
    bookings = frappe.get_all('Booking',filters={'movie':movie,'book_date':book_date}, pluck="name")
    book_all=[]
    for item in bookings: 
        data = frappe.get_doc('Booking',item)
        book_all.extend([i.seat_number for i in data.get('seat_number')])
    return  book_all

