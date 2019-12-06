from flask import Blueprint, abort, make_response, jsonify, Flask
import subprocess

app = Flask(__name__)
pdf = Blueprint('pdf', __name__)


@pdf.route('/pdf/<target_file_name>', methods=['GET'])
def create_account(target_file_name):
    try:
        cmd = (
            "libreoffice --nolockcheck --nologo --headless --norestore"
            " --language=ja --nofirststartwizard --convert-to pdf --outdir"
            f" /workspace /workspace/{target_file_name}"
        )

        app.logger.info(f"Start Conversion: {target_file_name}")

        proc = subprocess.run(cmd.split(" "), shell=False)

        app.logger.info(f"End Conversion: {target_file_name}")

        if proc.returncode != 0:
            raise Exception("pdfの変換に失敗しました。")

    except Exception as e:
        app.logger.error(f"Error: {target_file_name}")
        abort(500, f'{e}')

    else:
        app.logger.info(f"Success: {target_file_name}")
        data = {"code": 200, "message": "pdfの変換に成功しました。"}
        return make_response(jsonify(data))
