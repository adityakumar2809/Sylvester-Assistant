import poplib
import email
import json

from decouple import config


def check_mail():
    """Look for any new mail received in the inbox"""
    EMAIL_ID = config('EMAIL_ID')
    EMAIL_PASSWORD = config('EMAIL_PASSWORD')

    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user(EMAIL_ID)
    pop_conn.pass_(EMAIL_PASSWORD)
    messages = [pop_conn.retr(i)
                for i in range(1, len(pop_conn.list()[1]) + 1)
                ]
    messages = [b"\n".join(mssg[1]) for mssg in messages]
    messages = [email.message_from_bytes(mssg) for mssg in messages]
    for message in messages:
        print(message)
        print("\n\nSubject = ", message['subject'], end='\n\n\n')
        print("\n\nFrom = ", message['from'], end='\n\n\n')
        print("\n\nDate = ", message['date'], end='\n\n\n')
    pop_conn.quit()


if __name__ == "__main__":
    check_mail()
