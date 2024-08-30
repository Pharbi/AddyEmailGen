import requests
import time
import random
import string
import os
from bs4 import BeautifulSoup
from GmailDotEmailGenerator import GmailDotEmailGenerator

def generate_random_password(length=13):
    chars = string.ascii_letters + string.digits + '$&@?!#%'
    return ''.join(random.choice(chars) for _ in range(length))

def account_successfully_created(response, resume_url):
    try:
        return BeautifulSoup(response.text, "html.parser").find('input', {'id': 'resumeURL'}).get('value') != resume_url
    except:
        return True

def create_account(s, email, password, country_code, csrftoken):
    url = f'https://cp.adidas.com/web/eCom/en_{country_code}/accountcreate'
    data = {
        'firstName': 'YOUR_FIRST_NAME',
        'lastName': 'YOUR_LAST_NAME',
        'minAgeCheck': 'true',
        '_minAgeCheck': 'on',
        'email': email,
        'password': password,
        'confirmPassword': password,
        '_amf': 'on',
        'terms': 'true',
        '_terms': 'on',
        'metaAttrs[pageLoadedEarlier]': 'true',
        'app': 'eCom',
        'locale': f'en_{country_code}',
        'domain': '',
        'consentData1': 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Privacy Policy</a> for details.',
        'consentData2': '',
        'consentData3': '',
        'CSRFToken': csrftoken
    }

    if country_code in ['AU', 'UK']:
        data.update({
            'day': '5',
            'month': '10',
            'year': '1980',
        })

    if country_code == 'CA':
        data['consentData2'] = 'By entering my information, I give permission for adidas Canada Limited to contact me in future for marketing, advertising and opinion research for purposes of the adidas Group. I understand I can later withdraw consent.<a target="_blank" href="http://www.adidas.ca/en/help-topics-privacy_policy.html"><b>Learn More</b></a'

    return s.post(url, data=data)

def generate_accounts(country_code):
    print(f'Generating accounts for Adidas {country_code}')

    basemail = raw_input('Enter prefix of your email: ')
    use_random_pass = raw_input('Do you want a random password? (Y/N): ').lower() == 'y'
    password = generate_random_password() if use_random_pass else raw_input('Enter desired password: ')
    accounts_to_gen = int(raw_input('Enter desired number of accounts to be made: '))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1'
    }

    resume_url = f'https://www.adidas.com/on/demandware.store/Sites-adidas-{country_code}-Site/en_{country_code}/MyAccount-CreateOrLogin'

    for email in (GmailDotEmailGenerator(basemail + '@gmail.com').generate())[:accounts_to_gen]:
        s = requests.Session()
        s.headers.update(headers)

        r = s.get(f'https://cp.adidas.com/web/eCom/en_{country_code}/loadcreateaccount')
        csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'CSRFToken'}).get('value')

        s.headers.update({
            'Origin': f'https://cp.adidas.com',
            'Referer': f'https://cp.adidas.com/web/eCom/en_{country_code}/loadcreateaccount',
        })

        r = create_account(s, email, password, country_code, csrftoken)

        if account_successfully_created(r, resume_url):
            print(f"Created Account: Username = {email}, Password = {password}")
            with open('accounts.txt', 'a') as f:
                f.write(f"{email}:{password}\n")
        else:
            print(f"Account EXISTS: Username = {email}, Password = {password}")

        time.sleep(5)

def main():
    country_codes = {
        'US': 'US',
        'UK': 'GB',
        'CA': 'CA',
        'AU': 'AU'
    }

    loc = raw_input('Enter location (US/UK/CA/AU): ').upper()
    if loc in country_codes:
        generate_accounts(country_codes[loc])
    else:
        print("Invalid location. Please choose from US, UK, CA, or AU.")

if __name__ == "__main__":
    main()
