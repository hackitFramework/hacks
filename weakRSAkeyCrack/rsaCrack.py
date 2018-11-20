##
## rsaCrack
##
# Crack weak AES, DES methods using repeating decryption
# Henry Samuelson, Christopher Hansen
#
# 11/19/18
import base64
import sys
print(sys.argv[0] + sys.argv[1])
key = "bXqnLSa8E8KbD3A/isI7++FNAFTXH6nF184TKUaQBePapvPfcnlZ782mDuMwL4E7Be57HcGBOFMIU/3ALuxq2+cUlyMK07jEU1vdJDbUgXbc3wEbJtWHbs1Y3DJb+DCi9PiDZplE2G1nAXkQQWTuv2+dCv6pUFRgWeocQty8y/s="
#print(base64.b64decode(key))
encoded = base64.b64encode(sys.argv[1])
print(encoded)
data = base64.b64decode(encoded)
print(data)
