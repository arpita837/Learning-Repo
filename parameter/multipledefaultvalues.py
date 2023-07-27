def send_email(subject, body, recipient_email, cc_email=None, bcc_email=None):
    print(f"Sending email with subject: {subject}")
    print(f"To: {recipient_email}")
    if cc_email:
        print(f"Cc: {cc_email}")
    if bcc_email:
        print(f"Bcc: {bcc_email}")

# Calling the function with different combinations of parameters
send_email("Greetings", "Hello there!", "alice@example.com")
send_email("Meeting", "Agenda attached", "bob@example.com", "charlie@example.com")
