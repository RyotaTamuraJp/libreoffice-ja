from flask import jsonify

from src import create_app
from conf.app_config import LogConfig

app = create_app(logging_conf_path=LogConfig.logging_conf_path)


@app.errorhandler(500)
def error_handler_500(error):
    '''
    サーバーサイドの不明なエラーハンドリング
    '''
    response = {
        'message': 'サーバー側で予期せぬエラーが発生しました。',
        'description': error.description,
        'code': error.code
    }
    return jsonify(response), error.code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
