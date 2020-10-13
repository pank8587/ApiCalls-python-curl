
import requests

#response = requests.get("https://corporate-ui3.enterprise.com/pnkj-slng/auth?oauth_token=35c0a88051aa2a21fa7345db578e098ba5d7045503621f210e9e1218da7e0dcb3205be361cabc1bb1687cdd2b67406e0eb44c5100e33fbac16718210b6cfc41905f841ce9")

headers = {
'accept': 'text/html',
'Cookie': 'token=5e1a8b55b0249136a60423aa02b9120a845fa4122ac98ce4e771aec5d772d7d7a18ac22f18cd47727d00bddc2ebcc5cddf8a402d7a302ddffdeb7c6e15cb2a7005f857112',
}

response = requests.get("http://pnkjcorp-ui3.pnkj.com/data/1.0/auth/getUserByToken", headers=headers)

print(response.status_code)
