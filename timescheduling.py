from twilio.rest import Client




# print(str(minut).zfill(2))
raqamlar = ["+998993451598","+998993451598","+998993451598","+998993451598","+998993451598","+998993451598","+998993451598"]
ismlar = ['Shohruh',"Abdujabbor","Shomalik","Abror","Abdumalik","Sardor","Abbos"]

for ism in ismlar:
    print(f'{ism}')


soat = 10
minut = 0
for number in raqamlar:

    # if minut==0:
    #     str(minut).strip().zfill(2)
    if minut==60:
        minut=0
        soat=soat+1

    account_sid = 'ACfe40a932a05078e5b02a581d9987a351'
    auth_token = '31fac19a8c8c75a378db34016d22d4a9'
    TWILIO_NUMBER = "+12347040890"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            from_='+12347040890',
            to=number,
            body=f"Assalomu aleykum, sizga intervyu belgilangan. Intervyu vaqti Chorshanba kuni soat {soat}:{minut}da. "
                 f"Kech qolmasdan,o'z vaqtida kelishingizni so'raymiz!",
        )
    print(f'{soat}:{minut}')
    minut = minut + 10
    # print(message.sid)