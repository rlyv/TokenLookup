import requests as req
import colorama
from colorama import Fore
import time

r = Fore.RED
g = Fore.GREEN
re = Fore.RESET
b = Fore.BLUE
c = Fore.CYAN
y = Fore.YELLOW
m = Fore.MAGENTA
lm = Fore.LIGHTMAGENTA_EX
lr = Fore.LIGHTRED_EX
ly = Fore.LIGHTYELLOW_EX
lg = Fore.LIGHTGREEN_EX

def TokenLookup():
    print(fr"""{c}
 _____     _                _                 _                
|_   _|   | |              | |               | |               
  | | ___ | | _____ _ __   | |     ___   ___ | | ___   _ _ __  
  | |/ _ \| |/ / _ \ '_ \  | |    / _ \ / _ \| |/ / | | | '_ \ 
  | | (_) |   <  __/ | | | | |___| (_) | (_) |   <| |_| | |_) |
  \_/\___/|_|\_\___|_| |_| \_____/\___/ \___/|_|\_\\__,_| .__/ 
                                                        | |    
                                                        |_|    
""")
    token = input(f'{b}Your Token :{re} ')
    headers = {'Authorization':token}
    uri = "https://discordapp.com/api/v6"  
    url = f'{uri}/users/@me'
    purl = f'{uri}/users/@me/billing/payment-sources'

    res = req.get(url=url, headers=headers)

    if res.status_code == 200:
        profile = res.json()
        print(f"{g}Username: {lg}{profile['username']} {re}| {r}User ID: {lr}{profile['id']} {re}| {b}Email: {c}{profile['email']}{re}\n"
        f"{lg}Phone: {g}{profile['phone']} {re}| {r}Flags: {lr}{profile['flags']} {re}| {m}Locale: {lm}{profile['locale']} {re}| "
        f"{b}MFA: {c}{profile['mfa_enabled']} {re}| {y}NITRO : {y}{profile['premium_type']}{re}")

        payment_methods = 0
        payment_type = ""
        valid = 0

        try:
            response = req.get(purl, headers=headers)
            response.raise_for_status()
            data = response.json()

            for x in data:
                if 'type' in x and 'invalid' in x:
                    if x['type'] == 1:
                        payment_type += "CreditCard "
                    elif x['type'] == 2:
                        payment_type += "PayPal "

                    if not x['invalid']:
                        valid += 1
                        payment_methods += 1

        except req.exceptions.RequestException as e:
            print(f"Error: {e}")
            print(f"Valid Payment Methods: {valid}")
            print(f"Payment Types: {payment_type}")

    else:
        print(f"{r}Error: {res.status_code} - {res.text}{re}")
TokenLookup()