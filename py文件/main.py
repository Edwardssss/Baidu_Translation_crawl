import requests
from sign import sign
import re
import warnings

warnings.filterwarnings("ignore", category=Warning)  # 关闭弃用报错

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/66.0.3359.139 Safari/537.36",
           "Cookie": 'BIDUPSID=248487DDE4F4874C768DD664800AFB01; '
                     'PSTM=1624632627; '
                     '__yjs_duid'
                     '=1_9e9a49b48ccf294be969148528d703281624677345512; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; '
                     'REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; '
                     'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=39C416629357EBAB497629178C0541C1:FG=1; '
                     'BDUSS'
                     '=m9DMm1RUFZTTFBCNmdZUUFhY3lpeUR4Y3NNRW5SdThvb3FpTnZDNWdXNWRyeEJpSVFBQUFBJCQAAAAAAAAAAAEAAACSX1uneHp5MjAwMzIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF0i6WFdIulhZ; BDUSS_BFESS=m9DMm1RUFZTTFBCNmdZUUFhY3lpeUR4Y3NNRW5SdThvb3FpTnZDNWdXNWRyeEJpSVFBQUFBJCQAAAAAAAAAAAEAAACSX1uneHp5MjAwMzIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF0i6WFdIulhZ; H_PS_PSSID=35410_35105_31254_35774_34584_35490_35693_35796_35324_26350_35744; BAIDUID_BFESS=39C416629357EBAB497629178C0541C1:FG=1; BCLID=11903837222192425398; BDSFRCVID=meFOJeC627p69AjHgenlU9pUEeQF9_oTH6aoc1Pmnv6SwQ5bF3wEEG0PEM8g0Kub1VDqogKKQgOTHRCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbFqoKI5JK03J-Fk-R6BMtCbMfQyetJyaR0tXJvvWJ5TMCoJ0-c25-InbPvwblL8-NT42-ovyJ6_ShPC-tnc3M4nKxC82Mb8Qa743qbX3l02Vhvae-t2ynLIQMFLQ-RMW23I0h7mWUoTsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjC5DTOXjH8OtTnfb5kXWnbEatD_Hn7zeUDWeM4pbt-qJqTzLNQLWqnjBpRBSDTx3fo1j4tUXxTnBT5KaKTvaCTw5l7KHq32yqKKQlKkQN3TWxuO5bRi5Roy-q3FDn3oypQJXp0n04bly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfJut_I05JID-bnPk5PQ_b-40Mq0X5-RLfKj-Kq7F5l8-hC3xj6rNMxksbfTQL6cjQmT-blLXXb7xOKQphP-a0-uH5Gjg-h_tKeFeLh5N3KJmsqC9bT3v5tjL34OD2-biWa6M2MbdLqOP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe4bK-TrLjHKftxK; BCLID_BFESS=11903837222192425398; BDSFRCVID_BFESS=meFOJeC627p69AjHgenlU9pUEeQF9_oTH6aoc1Pmnv6SwQ5bF3wEEG0PEM8g0Kub1VDqogKKQgOTHRCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbFqoKI5JK03J-Fk-R6BMtCbMfQyetJyaR0tXJvvWJ5TMCoJ0-c25-InbPvwblL8-NT42-ovyJ6_ShPC-tnc3M4nKxC82Mb8Qa743qbX3l02Vhvae-t2ynLIQMFLQ-RMW23I0h7mWUoTsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjC5DTOXjH8OtTnfb5kXWnbEatD_Hn7zeUDWeM4pbt-qJqTzLNQLWqnjBpRBSDTx3fo1j4tUXxTnBT5KaKTvaCTw5l7KHq32yqKKQlKkQN3TWxuO5bRi5Roy-q3FDn3oypQJXp0n04bly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfJut_I05JID-bnPk5PQ_b-40Mq0X5-RLfKj-Kq7F5l8-hC3xj6rNMxksbfTQL6cjQmT-blLXXb7xOKQphP-a0-uH5Gjg-h_tKeFeLh5N3KJmsqC9bT3v5tjL34OD2-biWa6M2MbdLqOP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe4bK-TrLjHKftxK; delPer=0; PSINO=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1641456854,1642661186,1642662678,1642687449; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1642688201; BA_HECTOR=248g858580ak84a0u91guirq80q; ab_sr=1.0.1_MjM4OGFjMTZiZjUyMmYxMmU5NDhjY2FkZDkzNzRkMzZkZGUxN2RmMmY1NzEwYzg5ZDlmYTk2YTIzZmM0ODBlMzJlYzAwNDMxNjllNjk3OGMxZDJmMzI1NjNiNjlhNjExNTEzYmNkZTFlZWNjYzI4ZGVmZTA4NDk3ODBjYThlYzM='}

if __name__ == '__main__':
    print("请输入要选择的翻译模式")
    choose = int(input("[1]英译中\n[2]中译英\n"))
    while choose != 1 and choose != 2:
        print("错误！请重新输入")
        choose = int(input("[1]英译中\n[2]中译英\n"))
        data = {}
    if choose == 1:
        custom_input = input('请输入要翻译的英文\n')
        data = {
            "from": "en",
            "to": "zh",
            "query": "%s" % custom_input,
            "transtype": "translang",
            "simple_means_flag": "3",
            "token": '97c823341ff704dea2625870404fcec4',
            "sign": sign(custom_input)
        }
        response = requests.post(url='https://fanyi.baidu.com/v2transapi', headers=headers, timeout=1, data=data)
        response.encoding = 'utf-8'
        print(re.search("[\\u4e00-\\u9fa5]+", response.content.decode('unicode_escape'), flags=re.S)[0])
    elif choose == 2:
        custom_input = input('请输入要翻译成英文的中文\n')
        data = {
            "from": "zh",
            "to": "en",
            "query": "%s" % custom_input,
            "transtype": "translang",
            "simple_means_flag": "3",
            "token": '97c823341ff704dea2625870404fcec4',
            "sign": sign(custom_input)
        }
        response = requests.post(url='https://fanyi.baidu.com/v2transapi', headers=headers, timeout=1, data=data)
        response.encoding = 'utf-8'
        print(re.findall(pattern='[a-zA-Z]+', string=response.content.decode('unicode_escape'), flags=re.S)[4])
