from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        file1 = request.files.get('file1')
        file2 = request.files.get('file2')

        # Process the form data and files here
        if name and email and file1 and file2:
            return "Form submitted successfully!"

    return render_template('ScheduleA.html')

if __name__ == '__main__':
    app.run(debug=True)
