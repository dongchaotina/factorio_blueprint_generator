import base64
import gzip
from io import BytesIO
import luadata
import json


def decode_recipe(input_data):
    # 解码base64编码的数据
    decoded_data = base64.b64decode(input_data)

    # 创建一个BytesIO对象，以便像文件一样操作解码后的数据
    with BytesIO(decoded_data) as compressed_file:
        # 使用gzip模块解压数据
        with gzip.GzipFile(fileobj=compressed_file, mode='rb') as decompressed_file:
            # 读取解压后的数据
            decompressed_data = decompressed_file.read()

    result = decompressed_data.decode('utf-8')
    # remove everything before the first "{" and everything after the last "}"
    result = result[result.find('{'):result.rfind('}') + 1]
    return result


if __name__ == '__main__':
    # 假设input_data是你从某处（如文件、网络请求等）获取的base64编码且gzip压缩的数据
    with open('recipe.txt', 'r') as f:
        input_data = f.read()
    lua_table = decode_recipe(input_data)
    result = luadata.unserialize(lua_table)
    with open('recipe.json', 'w') as f:
        f.write(json.dumps(result, indent=2))
