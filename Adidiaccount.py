import requests, time, random, string, os
from bs4 import BeautifulSoup
from GmailDotEmailGenerator import GmailDotEmailGenerator


# TODO : Turn off this gosh darn rap music

def account_successfully_createdUS(response):
    try:
        return False if BeautifulSoup(response.text, "html.parser").find('input',
                                                                         {'id': 'resumeURL'}).get('value') == \
                        'https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MyAccount-CreateOrLogin' \
            else True
    except:
        return True


def US():
    print 'WE ARE GENERATING FOR ADIDAS US'

    basemail = raw_input('Enter prefix of your email\t')

    randompass = raw_input('Do you want a random pass? Y for Yes. Any other Key for No\t')
    if randompass == 'y' and 'y':
        print 'Generating Random passwords.'
    else:
        password = raw_input('Enter Desired Password\t')
    accountstogen = raw_input('Enter Desired Accounts to be Made\t')
    accountstogen = int(accountstogen)

    for email in \
            (GmailDotEmailGenerator(basemail + '@gmail.com').generate())[:accountstogen]:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1'
        }
        if randompass == 'y' and 'y':
            length = 13
            chars = string.ascii_letters + string.digits + '$&@?!#%'
            random.seed = (os.urandom(1024))
            password = ''.join(random.choice(chars) for i in range(length))

        s = requests.Session()
        s.headers.update(headers)

        r = s.get('https://cp.adidas.com/web/eCom/en_US/loadcreateaccount')
        csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'CSRFToken'}).get('value')

        s.headers.update({
            'Origin': 'https://cp.adidas.com',
            'Referer': 'https://cp.adidas.com/web/eCom/en_US/loadcreateaccount',
        })
        r = s.post('https://cp.adidas.com/web/eCom/en_US/accountcreate',
                   data={
                       'firstName': 'YOUR_FIRST_NAME',  ### Set your Name
                       'lastName': 'Jigga',  # Set your name
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
                       'locale': 'en_US',
                       'domain': '',
                       'consentData1': 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
                       'consentData2': '',
                       'consentData3': '',
                       'CSRFToken': csrftoken
                   })

        if account_successfully_createdUS(r) == False:
            # print 'ACCOUNT EXISTS'
            print "Account EXISTS : Username = {0}, Password = {1}".format(email, password)

        if account_successfully_createdUS(r) == True:

            print "Created Account : Username = {0}, Password = {1}".format(email, password)
            with open('accounts' + '.txt', 'a') as f:
                f.write(email + ':' + password + '\n')
                f.close()

            time.sleep(5)


def account_successfully_createdUK(response):
    try:

        return False if BeautifulSoup(response.text, "html.parser").find('input',
                                                                         {'id': 'resumeURL'}).get('value') == "" \
            else False
    except:
        return True


def UK():
    print 'WE ARE GENERATING FOR ADIDAS UK'
    basemail = raw_input('Enter prefix of your email\t')

    randompass = raw_input('Do you want a random pass? Y for Yes. Any other Key for No\t')
    if randompass == 'y' and 'y':
        print 'Generating Random passwords.'
    else:
        password = raw_input('Enter Desired Password\t')
    accountstogen = raw_input('Enter Desired Accounts to be Made\t')
    accountstogen = int(accountstogen)

    for email in \
            (GmailDotEmailGenerator(basemail + '@gmail.com').generate())[:accountstogen]:

        headers = {
            'GBer-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'en-GB,en;q=0.8',
            'Upgrade-Insecure-Requests': '1'
        }
        if randompass == 'y' and 'y':
            length = 13
            chars = string.ascii_letters + string.digits + '$&@?!#%'
            random.seed = (os.urandom(1024))
            password = ''.join(random.choice(chars) for i in range(length))

        s = requests.Session()
        s.headers.update(headers)

        r = s.get('https://cp.adidas.co.uk/web/eCom/en_GB/loadcreateaccount')
        csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'CSRFToken'}).get('value')

        s.headers.update({
            'Origin': 'https://cp.adidas.co.uk',
            'Referer': 'https://cp.adidas.co.uk/web/eCom/en_GB/loadcreateaccount',
        })
        r = s.post('https://cp.adidas.co.uk/web/eCom/en_GB/accountcreate',
                   data={
                       'firstName': 'YOUR_FIRST_NAME',  ### Set your Name
                       'lastName': 'Jigga',  # Set your name
                       'minAgeCheck': 'true',
                       'day': '3',
                       'month': '4',
                       'year': '1994',
                       '_minAgeCheck': 'on',
                       'email': email,
                       'password': password,
                       'confirmPassword': password,
                       '_amf': 'on',
                       'terms': 'true',
                       '_terms': 'on',
                       'metaAttrs[pageLoadedEarlier]': 'true',
                       'app': 'eCom',
                       'locale': 'en_GB',
                       'domain': '',
                       'consentData1': 'Sign me up for adidas emails, featuring exclGBive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.co.uk/GB/help-topics-privacy_policy.html">Policy Policy</a> for details.',
                       'consentData2': '',
                       'consentData3': '',
                       'CSRFToken': csrftoken
                   })

        if account_successfully_createdUK(r) == False:
            # print 'ACCOUNT EXISTS'
            print "Account EXISTS : Username = {0}, Password = {1}".format(email, password)
        if account_successfully_createdUK(r) == True:
            print "Created Account : Username = {0}, Password = {1}".format(email, password)
            with open('accounts' + '.txt', 'a') as f:
                f.write(email + ':' + password + '\n')
                f.close()

        time.sleep(5)


def AU():
    print 'WE ARE GENERATING FOR ADIDAS AU'
    basemail = raw_input('Enter prefix of your email\t')

    randompass = raw_input('Do you want a random pass? Y for Yes. Any other Key for No\t')
    if randompass == 'y' and 'y':
        print 'Generating Random passwords.'
    else:
        password = raw_input('Enter Desired Password\t')
    accountstogen = raw_input('Enter Desired Accounts to be Made\t')
    accountstogen = int(accountstogen)

    def account_successfully_created(response):
        try:
            return False if BeautifulSoup(response.text, "html.parser").find('input',
                                                                             {'id': 'resumeURL'}).get('value') == \
                            'https://www.adidas.com.au/on/demandware.store/Sites-adidas-AU-Site/en_AU/MyAccount-CreateOrLogin' \
                else True
        except:
            return True

    for email in \
            (GmailDotEmailGenerator(basemail + '@gmail.com').generate())[:accountstogen]:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1'
        }
        if randompass == 'y' and 'y':
            length = 13
            chars = string.ascii_letters + string.digits + '$&@?!#%'
            random.seed = (os.urandom(1024))
            password = ''.join(random.choice(chars) for i in range(length))

        s = requests.Session()
        s.headers.update(headers)

        r = s.get('https://cp.adidas.com/web/eCom/en_AU/loadcreateaccount')
        csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'CSRFToken'}).get('value')

        s.headers.update({
            'Origin': 'https://cp.adidas.com',
            'Referer': 'https://cp.adidas.com/web/eCom/en_AU/loadcreateaccount',
        })
        r = s.post('https://cp.adidas.com/web/eCom/en_AU/accountcreate',
                   data={
                       'firstName': 'YOUR_FIRST_NAME',  ### Set your Name
                       'lastName': 'Sarmiento',  # Set your name
                       'day': '5',
                       'month': '10',
                       'year': '1980',
                       'email': email,
                       'password': password,
                       'confirmPassword': password,
                       '_amf': 'on',
                       'terms': 'true',
                       '_terms': 'on',
                       'metaAttrs[pageLoadedEarlier]': 'true',
                       'app': 'eCom',
                       'locale': 'en_AU',
                       'domain': '',
                       'consentData1': 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
                       'consentData2': '',
                       'consentData3': '',
                       'CSRFToken': csrftoken
                   })

        if account_successfully_created(r) == False:
            # print 'ACCOUNT EXISTS'
            print "Username = {0}, Password = {1}, Account EXISTS".format(email, password)
        if account_successfully_created(r) == True:
            print "Created Account : Username = {0}, Password = {1}".format(email, password)
            with open('accounts' + '.txt', 'a') as f:
                f.write(email + ':' + password + '\n')
                f.close()

        time.sleep(5)


def CA():
    print 'WE ARE GENERATING FOR ADIDAS CA'
    basemail = raw_input('Enter prefix of your email\t')
    randompass = raw_input('Do you want a random pass? Y for Yes. Any other Key for No\t')
    if randompass == 'y' and 'y':
        print 'Generating Random passwords.'
    else:
        password = raw_input('Enter Desired Password\t')
    accountstogen = raw_input('Enter Desired Accounts to be Made\t')
    accountstogen = int(accountstogen)

    def account_successfully_created(response):
        try:
            return False if BeautifulSoup(response.text, "html.parser").find('input',
                                                                             {'id': 'resumeURL'}).get('value') == \
                            'https://www.adidas.ca/on/demandware.store/Sites-adidas-CA-Site/en_CA/MyAccount-CreateOrLogin' \
                else True
        except:
            return True

    for email in \
            (GmailDotEmailGenerator(basemail + '@gmail.com').generate())[:accountstogen]:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1'
        }
        if randompass == 'y' and 'y':
            length = 13
            chars = string.ascii_letters + string.digits + '$&@?!#%'
            random.seed = (os.urandom(1024))
            password = ''.join(random.choice(chars) for i in range(length))

        s = requests.Session()
        s.headers.update(headers)

        r = s.get('https://cp.adidas.ca/web/eCom/en_CA/loadcreateaccount')
        csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'CSRFToken'}).get('value')

        s.headers.update({
            'Origin': 'https://cp.adidas.ca',
            'Referer': 'https://cp.adidas.ca/web/eCom/en_CA/loadcreateaccount',
        })
        r = s.post('https://cp.adidas.ca/web/eCom/en_CA/accountcreate',
                   data={
                       'firstName': 'YOUR_FIRST_NAME',  ### Set your Name
                       'lastName': 'Sarmiento',  # Set your name
                       'minAgeCheck': 'true',
                       '_minAgeCheck': 'on',
                       'email': email,
                       'password': password,
                       'confirmPassword': password,
                       'amf': 'true',
                       '_amf': 'on',
                       'terms': 'true',
                       '_terms': 'on',
                       'metaAttrs[pageLoadedEarlier]': 'true',
                       'app': 'eCom',
                       'locale': 'en_CA',
                       'domain': '',
                       'consentData1': 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
                       'consentData2': 'By entering my information, I give permission for adidas Canada Limited to contact me in future for marketing, advertising and opinion research for purposes of the adidas Group. I understand I can later withdraw consent.<a target="_blank" href="http://www.adidas.ca/en/help-topics-privacy_policy.html"><b>Learn More</b></a',
                       'consentData3': '',
                       'CSRFToken': csrftoken
                   })

        if account_successfully_created(r) == False:
            # print 'ACCOUNT EXISTS'
            print "Username = {0}, Password = {1}, Account EXISTS".format(email, password)
        if account_successfully_created(r) == True:
            print "Created Account : Username = {0}, Password = {1}".format(email, password)
            with open('accounts' + '.txt', 'a') as f:
                f.write(email + ':' + password + '\n')
                f.close()

        time.sleep(5)


def main():
    loc = raw_input('ENTER LOC US UK CA AU  \t')
    if loc == 'UK':
        UK()
    if loc == 'US':
        US()
    if loc == 'AU':
        AU()
    if loc == 'CA':
        CA()
main()
