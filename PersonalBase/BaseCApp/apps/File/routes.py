import json
import os

from flask import Blueprint, request, send_from_directory, abort, render_template
from werkzeug.utils import secure_filename

from PersonalBase.BaseCApp.apps.File.beam import FileNodeCode
from PersonalBase.BaseCApp.apps.File.config import Config
from PersonalBase.BaseCApp.apps.Section.func import func_section_add, \
    func_section_get_function_with_json_con, func_section_delete_token, func_section_select_token, \
    func_section_select_token_with_json_con


def init_file_blueprint():
    File_Blueprint = Blueprint("File_Blueprint",
                               __name__,
                               url_prefix="/file",
                               template_folder="{}/PersonalBase/BaseCApp/apps/File/templates".format(os.getcwd()))

    file_store_path = Config.FilePathConfig.StorePath

    @File_Blueprint.route("/index", methods=['GET'])
    def index():
        return render_template("file_panel.html")

    @File_Blueprint.route("/upload", methods=['POST'])
    def upload():
        for file_node in request.files.getlist('file'):
            filename_original = secure_filename(file_node.filename)
            file_type = os.path.splitext(filename_original)[-1]
            note = request.form.get("note") or "blank"

            token = func_section_add(Config.Function,
                                     Config.Type,
                                     json.dumps(FileNodeCode(filename_original,
                                                             file_type,
                                                             note).to_object())).get("Body")

            file_node.save(os.path.join(file_store_path, token))

        return "upload files done"

    @File_Blueprint.route("/list", methods=["GET"])
    def list_file():
        os.listdir(file_store_path)
        body = func_section_get_function_with_json_con(Config.Function)
        body["Body"] = {
            "db": body["Body"],
            "folder": os.listdir(file_store_path)
        }
        return body

    @File_Blueprint.route("/delete", methods=['DELETE'])
    def delete_file():
        token = request.args.get("token") or abort(400)
        if os.path.exists(os.path.join(file_store_path, token)):
            os.remove(os.path.join(file_store_path, token))
        func_section_delete_token(token)
        return "file {} delete done".format(token)

    @File_Blueprint.route("/download", methods=['GET'])
    def download_file():
        token = request.args.get("token") or abort(400)
        tmp = func_section_select_token_with_json_con(token)
        if os.path.exists(os.path.join(file_store_path, token)) and os.path.isfile(
                os.path.join(file_store_path, token)):
            if tmp is not None:
                return send_from_directory(directory=file_store_path,
                                           filename=token,
                                           as_attachment=True,
                                           attachment_filename=tmp["con"]["FilenameOriginal"])
            else:
                return send_from_directory(directory=file_store_path, filename=token, as_attachment=True)
        else:
            abort(404)

    return File_Blueprint

# 这是2020.12.29-30晚上玩回形针的第一个交互视频
# 《一个人工智能的诞生》中用到的计算矩阵可能结果的代码
# 将被永久保存
# if __name__ == '__main__':
#     # x, y = -15, -15
#     for i in range(-15, 16):
#         for j in range(-15, 16):
#             if -14 * i + j * -10 == -76:
#                 print(i, j)
#
#     print("=====")
#     for i in range(-15, 16):
#         for j in range(-15, 16):
#             if -14 * i + j * -10 == -88:
#                 print(i, j)
#
#     print("===")
#     for i in range(-15, 16):
#         for j in range(-15, 16):
#             if -14 * i + j * -10 == 152:
#                 print(i, j)
