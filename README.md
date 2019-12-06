# libreoffice-ja
LibreOfficeを用いたドキュメントコンバーター（日本語対応）

## Quick Start
変換したいドキュメント（今回はdocx）をworkspaceフォルダ内に入れて以下実施。
test.docx部分を適宜変更してください。
```
docker-compose run --rm libreoffice libreoffice --nolockcheck --nologo --headless --norestore --language=ja --nofirststartwizard --convert-to pdf test.docx
```
