import os
from flask import Flask, request, render_template, redirect, url_for
from models import PreShipmentTask, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logisticsdatabase.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db.init_app(app)

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':
        try:
            from datetime import datetime

            def parse_date(date_str):
                if date_str:
                    return datetime.strptime(date_str, '%Y-%m-%d').date()
                return None

            def save_file(file):
                if file:
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                    file.save(filepath)
                    return filepath  # Store the file path in the database
                return None

            data = {
                'contract_signed_date': parse_date(request.form.get('date1')),
                'contract_signed_doc_no': request.form.get('docNo1'),
                'contract_signed_file': save_file(request.files.get('file1')),
    
                'contract_registered_date': parse_date(request.form.get('date2')),
                'contract_registered_doc_no': request.form.get('docNo2'),
                'contract_registered_file': save_file(request.files.get('file2')),
    
                'shipping_instruction_date': parse_date(request.form.get('date3')),
                'shipping_instruction_doc_no': request.form.get('docNo3'),
                'shipping_instruction_file': save_file(request.files.get('file3')),
    
                'bag_mark_sent': request.form.get('sent'),
                'bag_mark_approve': request.form.get('approve'),
                'bag_mark_date': parse_date(request.form.get('date4')),
                'bag_mark_doc_no': request.form.get('docNo4'),
                'bag_mark_file': save_file(request.files.get('file4')),
    
                'vessel_booking_sent': request.form.get('sent1'),
                'vessel_booking_approve': request.form.get('approve1'),
                'vessel_booking_date': parse_date(request.form.get('date5')),
                'vessel_booking_doc_no': request.form.get('docNo5'),
                'vessel_booking_file': save_file(request.files.get('file5')),
    
                'pss_sent': request.form.get('sent2'),
                'pss_approve': request.form.get('approve2'),
                'pss_date': parse_date(request.form.get('date6')),
                'pss_doc_no': request.form.get('docNo6'),
                'pss_file': save_file(request.files.get('file6')),
    
                'way_bill_to_port_date': parse_date(request.form.get('date7')),
                'way_bill_to_port_doc_no': request.form.get('docNo7'),
                'way_bill_to_port_file': save_file(request.files.get('file7')),
    
                'weighbridge_report_at_loading_date': parse_date(request.form.get('date8')),
                'weighbridge_report_at_loading_doc_no': request.form.get('docNo8'),
                'weighbridge_report_at_loading_file': save_file(request.files.get('file8')),
    
                'warehouse_stock_report_date': parse_date(request.form.get('date9')),
                'warehouse_stock_report_doc_no': request.form.get('docNo9'),
                'warehouse_stock_report_file': save_file(request.files.get('file9')),
    
                'stuffing_report_date': parse_date(request.form.get('date10')),
                'stuffing_report_doc_no': request.form.get('docNo10'),
                'stuffing_report_file': save_file(request.files.get('file10')),
    
                'weighbridge_report_at_stuffing_date': parse_date(request.form.get('date11')),
                'weighbridge_report_at_stuffing_doc_no': request.form.get('docNo11'),
                'weighbridge_report_at_stuffing_file': save_file(request.files.get('file11'))
            }

            task = PreShipmentTask(**data)
            db.session.add(task)
            db.session.commit()

            # Redirect to weightCertificate.html after successful submission
            return redirect(url_for('weight_certificate'))

        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}"

    return render_template('ScheduleA.html')

@app.route('/weightCertificate', methods=['GET'])
def weight_certificate():
    return render_template('weightCertificate.html')

if __name__ == '__main__':
    app.run(debug=True)
