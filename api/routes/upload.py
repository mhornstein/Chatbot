from flask import Blueprint, request, jsonify
from PIL import Image
import io

upload_bp = Blueprint('upload_dp', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    camera_id = request.form.get('camera_id')
    prompt = request.form.get('prompt')

    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))

    # TODO: compare text + image to the required image. the required image is identified by the camera id

    return jsonify({"message": "הגעתם ל-95% דיוק! כל הכבוד! הקוד למצלמה הוא: 5463"}) # reply example
