import sys
import json, requests

def run():
  payload = {
    "access_token": access_token,
    "data": raw_item_json
  }

  json_encoded_payload = json.dumps(payload)

  response = requests.request("POST", endpoint, data=json_encoded_payload, verify=verify)

  res_json = json.loads(response.text)
  print(res_json)


# Paste the raw item json blob here and remove any unwanted keys
raw_item_json = json.loads("""
{
  "body": {
    "message": {
      "body": "hello world"
    }
  }
}
""")


if __name__ == '__main__':
  host = 'rollbar.com'
  access_token = sys.argv[-1]
  endpoint = 'https://api.{}/api/1/item/'.format(host)
  verify = True

  if 'dev' in sys.argv:
    host = 'localhost'
    access_token = sys.argv[-1]
    endpoint = 'https://{}/api/1/item/'.format(host)
    verify = False

  run()
