from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':
        contract_signed = request.form.get('date1')
        contract_registered = request.form.get('date2')
        shipping_instruction = request.form.get('date3')
        
        doc_no1 = request.form.get('docNo1')
        doc_no2 = request.form.get('docNo2')
        doc_no3 = request.form.get('docNo3')
        
        file1 = request.files.get('file1')
        file2 = request.files.get('file2')
        file3 = request.files.get('file3')

        # Process the form data and files here
        if (contract_signed and contract_registered and shipping_instruction and
            doc_no1 and doc_no2 and doc_no3 and
            file1 and file2 and file3):
            return "Form submitted successfully!"

    return render_template('ScheduleA.html')

if __name__ == '__main__':
    app.run(debug=True)
