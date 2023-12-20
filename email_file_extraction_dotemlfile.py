import os
import email
from email import policy
from email.parser import BytesParser
from email.header import decode_header
from email.utils import parsedate_to_datetime

# Path to your .eml file
eml_file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'letters-summanus.eml')

# Check if the file exists
if os.path.exists(eml_file_path):
    with open(eml_file_path, 'rb') as f:
        # Parse the .eml file
        msg = BytesParser(policy=policy.default).parse(f)

        # Extract and print subject and sender information
        subject, encoding = decode_header(msg['subject'])[0]
        subject_decoded = subject.decode(encoding) if isinstance(subject, bytes) else subject
        print(f"Subject: {subject_decoded}")
        print(f"From: {msg['from']}")

        # Extract date and time information
        date_time = parsedate_to_datetime(msg['date'])
        print(f"Date and Time: {date_time}")

        # Accessing the body of the email
        body = ""
        for part in msg.iter_parts():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                break
        print("\nBody:")
        print(body.decode('utf-8'))

        # Handling Attachments
        for part in msg.iter_parts():
            if part.get_content_disposition() and 'attachment' in part.get('Content-Disposition', '').lower():
                attachment_data = part.get_payload(decode=True)
                attachment_filename, encoding = decode_header(part.get_filename())[0]
                attachment_filename = attachment_filename.decode(encoding) if encoding else attachment_filename
                save_path = os.path.join(os.path.expanduser('~'), 'Downloads', attachment_filename)
                
                with open(save_path, 'wb') as attachment_file:
                    attachment_file.write(attachment_data)

                print(f"\nAttachment saved: {save_path}")

else:
    print("File not found.")
