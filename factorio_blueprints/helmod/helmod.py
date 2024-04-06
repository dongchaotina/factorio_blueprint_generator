import base64
import zlib
import luadata


def decode_recipe(input_data):
    # 解码base64编码的数据
    decoded_content = base64.b64decode(input_data)

    # 创建一个BytesIO对象，以便像文件一样操作解码后的数据
    # Try to decompress the content assuming it's zlib compressed
    try:
        decompressed_content = zlib.decompress(decoded_content)
    except zlib.error as e:
        decompressed_content = f"Decompression failed: {e}"

    result = decompressed_content.decode("utf-8")
    # remove everything before the first "{" and everything after the last "}"
    lua_table = result[result.find("{") : result.rfind("}") + 1]
    return luadata.unserialize(lua_table)
