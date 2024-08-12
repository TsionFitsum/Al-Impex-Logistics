import os
from flask import Flask, request, render_template
from models import PreShipmentTask, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db.init_app(app)

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
                    return file.filename
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
                'bag_mark_file': save_file(request.files.get('file4'))
            }

            task = PreShipmentTask(**data)
            db.session.add(task)
            db.session.commit()

            return "Form submitted and data saved successfully!"

        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}"

    return render_template('ScheduleA.html')

if __name__ == '__main__':
    app.run(debug=True)
