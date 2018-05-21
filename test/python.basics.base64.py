import base64

text = b'data to be encoded'
encoded = base64.b64encode(text)
encoded

decoded = base64.b64decode(encoded)
decoded
text == decoded
