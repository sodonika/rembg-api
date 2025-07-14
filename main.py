from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
from PIL import Image
import os
app = Flask(__name__)

@app.route('/')
def home():
    return 'Rembg API is up!'

@app.route('/remove', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {'error': 'No image provided'}, 400

    image_file = request.files['image']
    input_image = Image.open(image_file.stream).convert("RGBA")
    output_image = remove(input_image)

    byte_io = BytesIO()
    output_image.save(byte_io, 'PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')

    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)