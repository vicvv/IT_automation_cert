#!/usr/bin/env python3

import sys
import emails
import os
import reports
from datetime import date

today = date.today()


def load_data():
    result =''
    path = "./supplier-data/descriptions/"
    for file in os.listdir("./supplier-data/descriptions"):
        with open(path + file ) as f:
            data = f.read().split('\n')
        result +="name: " + data[0] + "<br/>" + "weight: " + data[1] + "<br/><br/>"
    print(result)           
    return result

def main(argv):
    
    result = load_data()
    print(result)
    # TODO: turn this into a PDF report
    title ='Processed Update on ' + today.strftime("%B %d, %Y")
    paragraph=''
    attachment ='/tmp/processed.pdf'
    reports.generate_report(attachment, title, result)

    # send the PDF report as an email attachment   
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    message = emails.generate(sender, receiver, subject, body, attachment)
    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)
