from pymd5 import md5, padding
from sys import argv
import urllib

query_file = argv[1]
command_file = argv[2]
output_file = argv[3]

with open(query_file) as f:
    query = f.read().strip()
    
with open(command_file) as f:
    command = f.read().strip()
    
md5_state = query[6:38]

h = md5(state = md5_state.decode('hex'), count = 512)

h.update(command)
token = h.hexdigest()

msg_len = 8 + len(query[39:])
pad = padding(msg_len * 8)

new_query = urllib.quote("token=" + str(token) + str(query[38:]) + pad + command, safe ="&=")

with open(output_file, "w") as f:
    f.write(new_query)