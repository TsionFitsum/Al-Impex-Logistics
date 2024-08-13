from config import db

class PreShipmentTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contract_signed_date = db.Column(db.Date)
    contract_signed_doc_no = db.Column(db.String(100))
    contract_signed_file = db.Column(db.String(100))
    contract_registered_date = db.Column(db.Date)
    contract_registered_doc_no = db.Column(db.String(100))
    contract_registered_file = db.Column(db.String(100))
    shipping_instruction_date = db.Column(db.Date)
    shipping_instruction_doc_no = db.Column(db.String(100))
    shipping_instruction_file = db.Column(db.String(100))
    bag_mark_sent = db.Column(db.String(100))
    bag_mark_approve = db.Column(db.String(100))
    bag_mark_date = db.Column(db.Date)
    bag_mark_doc_no = db.Column(db.String(100))
    bag_mark_file = db.Column(db.String(100))
    vessel_booking_sent = db.Column(db.String(100))
    vessel_booking_approve = db.Column(db.String(100))
    vessel_booking_date = db.Column(db.Date)
    vessel_booking_doc_no = db.Column(db.String(100))
    vessel_booking_file = db.Column(db.String(100))
    pss_sent = db.Column(db.String(100))
    pss_approve = db.Column(db.String(100))
    pss_date = db.Column(db.Date)
    pss_doc_no = db.Column(db.String(100))
    pss_file = db.Column(db.String(100))
    way_bill_to_port_date = db.Column(db.Date)
    way_bill_to_port_doc_no = db.Column(db.String(100))
    way_bill_to_port_file = db.Column(db.String(100))
    weighbridge_report_at_loading_date = db.Column(db.Date)
    weighbridge_report_at_loading_doc_no = db.Column(db.String(100))
    weighbridge_report_at_loading_file = db.Column(db.String(100)) 
    warehouse_stock_report_date = db.Column(db.Date)
    warehouse_stock_report_doc_no = db.Column(db.String(100))
    warehouse_stock_report_file = db.Column(db.String(100))
    stuffing_report_date = db.Column(db.Date)
    stuffing_report_doc_no = db.Column(db.String(100))
    stuffing_report_file = db.Column(db.String(100))
    weighbridge_report_at_stuffing_date = db.Column(db.Date)
    weighbridge_report_at_stuffing_doc_no = db.Column(db.String(100))
    weighbridge_report_at_stuffing_file = db.Column(db.String(100))
