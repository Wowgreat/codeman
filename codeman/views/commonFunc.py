import time
import jwt
from jwt import InvalidSignatureError, DecodeError



def jwtencode(dict_data):
    dict_data['time'] = time.time()
    encoded = jwt.encode(dict_data, 'codeman', algorithm='HS256')
    return encoded


def jwtdecode(token):
    now_time = time.time()
    try:
        dict_data = jwt.decode(token, 'codeman', algorithms=['HS256'])
    except (DecodeError, InvalidSignatureError):
        return False
    # 有效期为两个星期
    if (now_time - dict_data.get('time')) >= 60*60*24*14:
        return False
    else:
        return dict_data