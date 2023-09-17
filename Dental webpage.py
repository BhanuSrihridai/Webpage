from flask import Flask, render_template

app = Flask(__name__)
# app = Flask(__name__, template_folder='C:\\D365 CE Practice\\HTML\\Dental\\templates')


@app.route('/')
def home():
    return render_template(r"C:\D365 CE Practice\HTML\Dental\templates")

if __name__ == '__main__':
    app.run(debug=True)
