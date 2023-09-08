from flask import Flask, Response, render_template_string
import requests 

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <div>
        <h4>Hola</h4>
        <p>Bienvenido al backend de la app de Federal FM</p>
    </div>
    """
    return render_template_string(html_content)

@app.route('/stream_proxy')
def stream_proxy():
    audio_url = 'http://usa15.ciudaddigital.com.uy:8040/FederalFM'
    response = requests.get(audio_url, stream=True)
    return Response(response.iter_content(chunk_size=1024), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)