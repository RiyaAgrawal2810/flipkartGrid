from flask import Flask, render_template_string
import subprocess
app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string(open('try.html').read())


@app.route('/run_streamlit', methods=['GET'])
def run_streamlit():
    # This endpoint starts streamlit
    subprocess.Popen(['streamlit', 'run', 'app.py'])
    return "Streamlit is running!"


if __name__ == '__main__':
    app.run(port=8503)

