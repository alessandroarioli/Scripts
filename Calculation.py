import time
import OCR_Engine

def calc_pure_python(file_in, file_out):
    start_time = time.time()
    output = OCR_Engine.process(file=file_in, file_out=file_out)
    end_time = time.time()
    secs = end_time - start_time
    print 'It tooks ' , secs , 'seconds'

calc_pure_python(file_in='/Users/dev-01/Downloads/Autoveicoli_elettrici.ldj', file_out='/Users/dev-01/Desktop/Da_caricare_in_Piatttaforma_con_emails/Autoveicoli_elettrici.ldj')
