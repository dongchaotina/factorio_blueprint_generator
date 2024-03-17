import base64
import gzip
from io import BytesIO

import luadata


def decode_recipe(input_data):
    # 解码base64编码的数据
    decoded_data = base64.b64decode(input_data)

    # 创建一个BytesIO对象，以便像文件一样操作解码后的数据
    with BytesIO(decoded_data) as compressed_file:
        # 使用gzip模块解压数据
        with gzip.GzipFile(fileobj=compressed_file, mode="rb") as decompressed_file:
            # 读取解压后的数据
            decompressed_data = decompressed_file.read()

    result = decompressed_data.decode("utf-8")
    # remove everything before the first "{" and everything after the last "}"
    lua_table = result[result.find("{") : result.rfind("}") + 1]
    return luadata.unserialize(lua_table)
