from flask import Flask, send_file

app = Flask(__name__)

@app.route('/gif')
def serve_gif():
    # Substitua 'caminho/para/seu_gif.gif' pelo caminho do seu arquivo GIF
    gif_path = 'Dey.gif'
    return send_file(gif_path, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True)