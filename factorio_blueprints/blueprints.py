import base64
import zlib
import json

def blueprint_to_json(blueprint_string):
    # 跳过第一个字节
    blueprint_string = blueprint_string[1:]

    # Base64解码
    decoded_data = base64.b64decode(blueprint_string)

    # 使用zlib的inflate解压缩
    decompressed_data = zlib.decompress(decoded_data)

    # 将解压缩后的数据转换为字符串形式的JSON
    json_data = decompressed_data.decode('utf-8')

    return json_data


def json_to_blueprint(json_data):
    # 将JSON数据转换为字节形式
    json_bytes = json_data.encode('utf-8')

    # 使用zlib的deflate压缩
    compressed_data = zlib.compress(json_bytes)

    # Base64编码
    blueprint_string = base64.b64encode(compressed_data)

    # 添加第一个字节
    blueprint_string = b'0' + blueprint_string

    return blueprint_string

def test_decode():
    with open('test_bp1.txt', 'r') as f:
        blueprint_string = f.read()

    # 转换并打印JSON数据
    json_data = blueprint_to_json(blueprint_string)
    # save to json file with indent
    with open('test_bp1.json', 'w') as f:
        f.write(json.dumps(json.loads(json_data), indent=2))

def test_encode():
    with open('test_bp1.json', 'r') as f:
        json_data = f.read()

    # 转换并打印蓝图字符串
    blueprint_string = json_to_blueprint(json_data)
    with open('test_bp1_encoded.txt', 'w') as f:
        f.write(blueprint_string.decode('utf-8'))

if __name__ == '__main__':
    test_encode()
