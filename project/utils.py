import zlib
import json
# import aiohttp
from datetime import datetime
import unicodedata


def key_formatter(label: str) -> str:
    s = ''.join(c for c in unicodedata.normalize('NFD', label) if unicodedata.category(c) not
                in ['Mn', 'So', 'Po', 'Ps', 'Pe'])
    return s.replace(' ', '_')


# async def send_chat_msg(webhook_url: str, msg: str):
#     async with aiohttp.ClientSession() as session:
#         async with session.post(
#                 webhook_url,
#                 json={'text': msg}
#         ) as resp:
#             data = await resp.text()
#             # print(data)


def months_diff(d: str, format_: str = '%Y%m%d') -> int:
    # d = '20210301'                     format = '%Y%m%d'
    # d = '202103'                       format = '%Y%m'
    # d = '1983-12-26T12:00:00-03:00'    format = '%Y-%m-%dT%H:%M:%S-%f'
    date = datetime.strptime(d, format_)
    now = datetime.now()
    diff = (now.year - date.year) * 12 + (now.month - date.month)
    return diff


def dict_compress(input_dict: dict, encoding: str = 'utf-8', compression_level: int = 9) -> str:
    # zlib.compress(bytes(json.dumps(data), 'utf-8')).decode('latin1')
    if not isinstance(compression_level, int) or compression_level < 0 or compression_level > 9:
        raise ValueError('Invalid compression_level: it must be an "int" between 0 and 9')
    original_bytes = bytes(json.dumps(input_dict), encoding)
    compressed_bytes = zlib.compress(original_bytes, compression_level)
    output = compressed_bytes.decode('latin1')
    return output


def dict_decompress(compress_string: str, encoding: str = 'utf-8') -> dict:
    # json.loads(zlib.decompress(data.encode('latin1')))
    compress_bytes = compress_string.encode('latin1')
    decompressed_bytes = zlib.decompress(compress_bytes)
    original_dict = json.loads(decompressed_bytes)
    return original_dict

