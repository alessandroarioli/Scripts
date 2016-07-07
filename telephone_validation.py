from gevent.monkey import patch_all; patch_all()
from gevent.pool import Pool
import requests
import time
from functools import partial
from internet import MiddlewareMixer, LuminatiMiddleware
import OCR_Engine


# @contextmanager
# def prova():
#     print 'suca'
#     yield
#     print 'forte'
#
# with prova() as suca:
#     print 'sucone'

def number_validation(phone_number):
    # headers = LuminatiMiddleware(MiddlewareMixer().browser).headers
    # number = number.replace('+39', '')
    payload = {"VisitorSid": 'MQe1qs89SX8pWV8+YIJzjG6UsnEgMryqppxooTf7lIWxCp57AGV4yX7WDYOg1i9sErU613WLwyExwzNvjL5ogwYf9qCnsgo3fHmiPdSf3JFVjaYnCcFiRM0mo7clgmOQ',
               "CSRF": '1456995701-fa2f2192f16e0354ff3583ca0f231c9710d860271afe54b997f4173480b42904+1456995701-c6c80bc43b93a268e31875d9a516008946caedc238e87064ed42639e64395a6b'}
    x = requests.post('https://www.twilio.com/functional-demos?Type=lookup&PhoneNumber= ' + '+39{}'.format(phone_number),
                      data=payload)
    print x.text
    return x.text


if __name__ == '__main__':
    start = time.time()
    pool = Pool(20)
    phone_set = set()
    with open('/Users/dev-01/PycharmProjects/My_fucking_code_folder/email_test.ldj') as phones:
        for phone in phones.readlines():
            phone_set.add(phone)
    greenlets = pool.imap(number_validation, phone_set)
    with open('/Users/dev-01/PycharmProjects/My_fucking_code_folder/numbers_out.ldj', 'a') as file:
        for greelet in greenlets:
            file.write('number:    {}'.format(greelet))
    seconds = time.time() - start
    print 'Total time:  ', seconds

# Number_validation('./email_test.ldj', './emails_out_mobile.ldj')