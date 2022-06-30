# -*- coding: utf-8 -*-
import base64

from Cryptodome.Cipher import AES


def decode_aes256(data, encryption_key):
    iv = encryption_key[0:16]
    aes = AES.new(encryption_key, AES.MODE_CBC, iv)
    d = aes.decrypt(data)
    unpad = lambda s: s[0:-ord(d[-1:])]
    return unpad(d)

# 此处传入密文
data = '**************************************************'
data = base64.b64decode(data)
# 此处传入CallbackUrlKey
e = decode_aes256(data, bytes('**************************************************', encoding="utf8"))
print(type(e))
print(str(e, encoding="utf8"))
