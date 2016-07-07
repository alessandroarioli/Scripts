#!/usr/bin/python
import telephone_validation
import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO
import string
import re
from internet import MiddlewareMixer
import sys, time
# if 'threading' in sys.modules:
#     del sys.modules['threading']
import gevent
import gevent.pool
import gevent.socket
import gevent.monkey
gevent.monkey.patch_thread()


def process_image(url):
    # image = _get_image(url)
    requester = MiddlewareMixer()
    response = requester(url)
    image = Image.open(StringIO(response.content))
    correct = small_image_manipulation(image=image)
    return correct


def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))


def small_image_manipulation(image):
    # Fucking rude corrector.. but it works!
    image = image.convert("RGBA")
    nx, ny = image.size
    processed_image = image.resize((int(nx*5), int(ny*5)), Image.ANTIALIAS)
    processed_image = processed_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    processed_image.save("./ResizeImage.png", dpi=(400, 400))
    new = Image.open("./ResizeImage.png")
    text = pytesseract.image_to_string(image=new)
    # This is for News Gothic MT font
    if "\\" in text:
        text = string.replace(text, "\\", "i")
    if " " in text:
        text = string.replace(text, " ", "")
    if "|" in text:
        text = string.replace(text, "|", "l")
    if ".con" in text:
        text = string.replace(text, ".con", ".com")
    return text

# process_image("http://www.misterimprese.it/img//Z3N5RzlWdVY3T0d3TFlDQzM5ZW42cE5hVDdPQmdkMUkyMGNNS3J0Uy9Qcz0=")

# @click.argument('file', type=click.Path(file_okay=True, resolve_path=True))
# @click.argument('file_out', type=click.Path(file_okay=True, resolve_path=True))


def process(line):
    match_email = re.search(r'\"emails\"\: \[\"(.+?)=', line)
    before_segment = re.search(r'(.+?)\"emails\"\: \[\"', line)
    after_segment = re.search(r'"size": {(.+?)}}', line)
    if match_email:
        email = string.replace(match_email.group(), '"emails": ["', 'http://www.misterimprese.it/img/')
        correct = process_image(email)
        correct_line = ""
        correct_line += (before_segment.group())
        correct_line += (correct)
        correct_line += ('"], ')
        correct_line += (after_segment.group())
        print correct_line
        return correct_line
    else:
        return line


def number_validation(phone_number):
    # headers = LuminatiMiddleware(MiddlewareMixer().browser).headers
    # number = number.replace('+39', '')
    payload = {"VisitorSid": 'wI7LgxsBW5zzgn8Mkux3oUMZLBUE0mxnVyWI0yzf5Dw67kjkNaNAAUT699io3ZmQWEq44rnrVZQa2br41d8QXrAAKAYjyOio5jBeQX8S+R70NhHHmJYZhMwl2jD2Od8V',
               "CSRF": '1458048597-f79839ca7a9373d1ba8ed09950a7b97f673326a86c31dc1c5659b9f5f6630744+1458048597-437a5d36223321359f845577a183d89da08048789925193a3fbd55b3f028b81a'}
    x = requests.post('https://www.twilio.com/functional-demos?Type=lookup&PhoneNumber= ' + '+39' + phone_number,
                      data=payload)
    print x.text
    return x.text


def phone_number_validation_calling(record):
    phone_segment = re.search(r'"phones": \[{"raw": "(.+?)"}],', record)
    if phone_segment:
        phone_segment = re.search(r' "(.+?)"', phone_segment.group())
    full_phone_segment = re.search(r'"phones": \[(.+?)],', record)
    if phone_segment:
        phones = (phone_segment.group().replace('"', ''))
        phones_ok = phones.split(',')
        for phone in phones_ok:
            if phone == '':
                break
            response = number_validation(phone)
            if '"success": false' in response:
                return record.replace(full_phone_segment.group(), '"phones": [],')
            return record


# process(file='/Users/dev-01/Downloads/Bullonerie.ldj',
# file_out='/Users/dev-01/Desktop/Da_caricare_in_Piatttaforma_con_emails/Bullonerie.ldj')

if __name__ == '__main__':
    start_time = time.time()
    pool = gevent.pool.Pool(20)
    lines = set()
    records = set()
    with open(sys.argv[1]) as file_in:
        for one_line in file_in.readlines():
            lines.add(one_line)
        threads = pool.imap(process, lines)
        for th in threads:
            print th
            records.add(th)
    print 'Waiting till gevent can join the greenlets...'
    print "Starting phone number validation..."

    start_time_validation = time.time()
    greenlets = pool.imap(phone_number_validation_calling, records)

    with open(sys.argv[2], 'a') as writer:
        for greenlet in greenlets:
            if greenlet:
                writer.write(str(greenlet))
    #     for single_line in records:
    #         single_line = phone_number_validation_calling(single_line)
    #         if single_line:
    #             writer.write(str(single_line))

    print "DONE!"
    print 'OCR + phone validation tooks %s seconds' % (time.time() - start_time)
    print 'Phone validation only tooks %s seconds' % (time.time() - start_time_validation)
    exit()


# Testing
# start_time = time.time()
# pool = gevent.pool.Pool(20)
# lines = set()
# records = set()
# with open("/Users/dev-01/Downloads/Biciclette.ldj") as file_in:
#     for one_line in file_in.readlines():
#         lines.add(one_line)
#     threads = pool.imap(process, lines)
#     for th in threads:
#         print th
#         records.add(th)
# print 'Waiting till gevent can join the greenlets...'
# print "Writing to file..."
#
# greenlets = pool.imap(phone_number_validation_calling, records)
#
# with open("/Users/dev-01/Desktop/Da_caricare_in_Piatttaforma_con_emails/Biciclette.ldj", 'a') as writer:
#     for greenlet in greenlets:
#         if greenlet:
#             writer.write(str(greenlet))
# #     for single_line in records:
# #         single_line = phone_number_validation_calling(single_line)
# #         if single_line:
# #             writer.write(str(single_line))
#
# print "DONE!"
# print 'OCR + phone validation tooks %s seconds' % (time.time() - start_time)
# exit()
# phone_number_validation_calling('{"description": [], "links": [], "revenue": {"raw": ""}, "phones":
# [{"raw": "010 3622730"}, {"raw": "010 310393"}], "industry": {"code": ["tran_railtru"]}, "tax_id": {"raw": ""},
# "address": {"raw": "V. Dassori, 47 16131 Genova (GE)"}, "year_of_establishment": "", "country": "IT", "name":
# {"raw": "Saim Am Automotive - Firam Srl"}, "emails": [], "size": {"raw": ""}}')







