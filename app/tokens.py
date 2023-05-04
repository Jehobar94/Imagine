 import jwt
 key = 'YXNkc2Rhc2RmYXNkZmFzZmRhc2RmYXNk'
 message = { 'iss': key }
 secret = 'dnVvODY4Yzc2bzhzNzZqOG83czY4b2Nq'
 token_bytes = jwt.encode(message, secret, algorithm='HS256')
 token = token_bytes.decode()
 token
'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJZWE5rYzJSaGMyUm1ZWE5rWm1GelptUmhjMlJtWVhOayJ9.P4leoe9q_H3lmIlnpZuVFSt7ORgLhLfQ3JN_3FMexSo'