from flask import Blueprint, abort, make_response, Flask, request
import subprocess

app = Flask(__name__)
pdf = Blueprint("pdf", __name__)


@pdf.route("/pdf", methods=["POST"])
def convert_file() -> None:
    """受信したdocxファイルをpdfファイルに変換
    - /workspace（Dockerfileで作成済み）にアップロードファイル(docx)を保存
    - 保存したdocxファイルをlibreofficeを使ってpdfに変換
    - 変換元のdocxを削除
    - pdfファイルをリターン
    """
    try:
        if "uploadFile" not in request.files:
            raise Exception("uploadFileがありません")

        file = request.files["uploadFile"]
        filename = file.filename
        if not filename:
            raise Exception("アップロードファイルのファイル名がありません")

        # ファイルを/workspaceに保存
        
        file.save(f"/workspace/{filename}")

        # PDF変換処理
        cmd = (
            "libreoffice --nolockcheck --nologo --headless --norestore"
            " --language=ja --nofirststartwizard --convert-to pdf --outdir"
            f" /workspace /workspace/{filename}"
        )
        app.logger.info(f"Start Conversion: {filename}")
        proc = subprocess.run(cmd.split(" "), shell=False)
        app.logger.info(f"End Conversion: {filename}")
        if proc.returncode != 0:
            raise Exception("pdfの変換に失敗しました。")

        # 変換後のファイルをレスポンスとして送信
        response = make_response()
        converted_filename = filename.replace(".docx", ".pdf")
        with open(f"/workspace/{converted_filename}", "rb") as f:
            response.data = f.read()
        response.headers[
            "Content-Disposition"
        ] = f"attachment; filename={converted_filename}"
        response.mimetype = "application/pdf"

        return response

    except Exception as e:
        app.logger.error(f"Error: {filename}")
        abort(500, f"{e}")
