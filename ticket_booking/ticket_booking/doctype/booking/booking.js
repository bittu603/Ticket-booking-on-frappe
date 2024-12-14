// Copyright (c) 2024, Bittu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Booking", {
    theater_show: function (frm) {
        frappe.call({
            method: "ticket_booking.api.get_unavailable_seats",
            args: {
                theater_show: frm.doc.theater_show
            },
            callback: function (response) {
                if (response.message) {
                    let unavailableSeats = response.message;
                    console.log("Unavailable seats: ", unavailableSeats);
                    // Process the unavailable seats as necessary
                }
            }



        })
        // The field 'theater_show' has been changed, so you can perform actions here
        // frappe.msgprint("Theater Show field has been changed.");
    },
    movie: (frm) => {
        console.log(frm.doc);
        let release_date = frm.doc.release_date

        frm.set_query("date", function () {
            return {
                filters: {
                    // Example: Filter dates greater than or equal to today
                    date: [">=", frappe.datetime.now_date()]
                }
            };
        });




    },
    movie: function (frm) {
        let release_date = frm.doc.release_date
        // if (typeof release_date === 'string') {
        release_date = new Date(release_date);
        $(frm.fields_dict['book_date'].$input).datepicker({
            minDate: release_date
        });
        // }

        // Setting up the date picker for the 'book_date' field

    },
    book_date: function (frm) {

        frappe.call({
            method: "ticket_booking.api.filter_seat_number",
            args: {
                "movie": frm.doc.movie,
                "book_date": frm.doc.book_date,
            },
            callback: function (response) {
                // Handle response if necessary
                if (response.message) {
                    frm.fields_dict['seat_number'].get_query = function () {
                        if (!frm.doc.book_date) {
                            return {
                                filters: {
                                    'seat_number': __('Please select seat_number')
                                }
                            };
                        } else {
                            return {
                                filters: [ 
                                    ['Seat Number', 'seat_number', 'NOT IN', response.message],
                                ]
                            };
                        }
                    };
                }
            }
        });
    },

    refresh(frm) {

        let release_date = frm.doc.release_date
        let book_date = frm.doc.book_date
        if (book_date < release_date) {
            frappe.throw("Please Select a Valid Date")
        }


    }

});
