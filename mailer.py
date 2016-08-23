import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# <tr>
#           <td> data </td>
#           <td> info </td>
#         </tr>


def sendmail(res):
    me = "ben.coste@gmail.com"
    you = "ben.coste@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Daemon appartement"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
    <html>
          <table align="center" width="800" cellspacing="10" cellpadding="0" style="border:1px solid #333;">
            <tr>
              <td> price/m2 </td>
              <td> price </td>
              <td> surface </td>
              <td> title </td>
              <td> img </td>
            </tr>
           """ + res + """
          </table>
    </html>"""

    # Record the MIME types of both parts - text/plain and text/html.
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    username = 'ben.coste'
    password = 'Itadakimasu2!#'
    s.login(username,password)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()

