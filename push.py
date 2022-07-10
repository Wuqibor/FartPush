import argparse
import base64
import hmac
import json
import requests
import time
import urllib.parse
import hashlib
import timeout_decorator



# 钉钉推送 加签 text模式 # 标题 消息 token 签名密钥 是否艾特全体 # By Wuqibor
@timeout_decorator.timeout(60)
def ding(title, msg, token, secret, isAtAll=True):
    # 推送
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "Content-Type": "application/json"
    }
    msgjson = {
        "msgtype": "text",
        "text": {
            "title": title,
            "content": msg + "\n"
        },
        "at": {
            "isAtAll": isAtAll
        }
    }
    dingApi = "https://oapi.dingtalk.com/robot/send?"
    pushUrl = dingApi + "access_token=" + token

    if secret != "":  # 是否需要加签
        # 钉钉推送签名算法
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        pushUrl = pushUrl + "&timestamp=" + timestamp + "&sign=" + sign

    rs = requests.post(url=pushUrl, data=json.dumps(msgjson), headers=headers)
    return str(rs.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='钉钉土味情话推送')
    parser.add_argument('--dingtoken', type=str, help='钉钉token')
    parser.add_argument('--dingsecret', type=str, help='钉钉secret')
    args = parser.parse_args()
    dingtoken = args.dingtoken
    dingsecret = args.dingsecret
    if dingtoken == "":
        print("### error DingTalk push token not found | 未发现钉钉推送Token ###")
        exit(3)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30",
        "Host": "api.lovelive.tools"
    }

    api = "http://api.lovelive.tools/api/SweetNothings"
    text = requests.get(url=api, headers=headers, timeout=60)

    if text.ok:
        print(f"### info text: {text.text} ###")
        json1 = json.loads(ding("日日夜夜土味情话", text.text, dingtoken, dingsecret, False))
        if str(json1['errcode']) == "0":
            print("### info DingTalk push successfully | 钉钉推送成功 ###")
        else:
            print(f"### error DingTalk push falied | 钉钉推送失败 : {json.dumps(json1)} ###")
    else:
        print(f"### error Failed to obtain unfashionable love words | Failed to obtain unfashionable love words ###")
