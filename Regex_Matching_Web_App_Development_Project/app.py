from flask import Flask, render_template, request
from regex import perform_regex_matching
import os

app = Flask(__name__)

# Set the template folder explicitly
template_folder = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_folder)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']

        matches = perform_regex_matching(test_string, regex_pattern)

        return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

    return render_template('index.html', test_string='', regex_pattern='', matches=None)

if __name__ == '__main__':
    app.run(debug=True)
