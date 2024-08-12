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
    # Add more fields as necessary
