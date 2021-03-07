#!env/bin/python

from webull import webull

wb = webull()
wb.get_mfa('email@email.com')
# or
# wb.get_mfa('+1-1234567890')
wb.get_security('email@email.com')
# or
# wb.next_security('email@email.com')
wb.login('email@email.com', 'password', 'device-id', 'code recvd from get_mfa()', 'question_id recved from get_security', 'answer to said question')
