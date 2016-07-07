import mandrill


def send_mandrill_email(email_to, number_of_points, schedule_time =''):
    try:
        mandrill_client = mandrill.Mandrill("9lvsfZJ9lLVIIbMZFb2AlQ")
        template_content = [{'content': 'example content', 'name': 'example name'}]
        message = {
            'auto_html': None,
            'auto_text': None,
            'from_email': 'info@kuldat.com',
            'from_name': 'Kuldat',
            'preserve_recipients': None,
            'return_path_domain': None,
            'signing_domain': None,
            'global_merge_vars': [{'content': number_of_points, 'name': 'LEADS'}],
            'subject': 'Utilizza i tuoi punti gratis sulla piattaforma Kuldat',
            'to': [{'email': email_to,
             'name': 'Alessandro',
             'type': 'to'}],
        }
        result = mandrill_client.messages.send_template(template_name='keep_in_touch',
                                                        template_content=template_content,
                                                        message=message, async=False, ip_pool='Main Pool',
                                                        send_at=schedule_time)
        print result

    except mandrill.Error, e:
        print  'A mandrill error occurred: %s - %s' % (e.__class__, e)
        raise


send_mandrill_email('alessandro.arioli@kuldat.com', '88', schedule_time='2016-02-09 11:20:00')
