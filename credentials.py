account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def pg1():
    from twilio.rest import Client

    client = Client(account_sid, auth_token)

    client.messages.create(
        to="+16692258746",
        from_="+18317080431",
        body="It's your turn to clean",
        media_url="http://www.supakleenservices.com/images/newSupakleen/Construction.png" )

def pg2():
    from twilio.rest import Client

    client = Client(account_sid, auth_token)

    client.messages.create(
        to="+17076908763",
        from_="+18317080431",
        body="It's your turn to clean",
        media_url="http://www.supakleenservices.com/images/newSupakleen/Construction.png" )

def pg3():
    from twilio.rest import Client

    client = Client(account_sid, auth_token)

    client.messages.create(
        to="+1 (669) 237-6151",
        from_="+18317080431",
        body="It's your turn to clean",
        media_url="http://www.supakleenservices.com/images/newSupakleen/Construction.png" )

def pg4():
    from twilio.rest import Client

    client = Client(account_sid, auth_token)

    client.messages.create(
        to="+1 (408) 646-4489",
        from_="+18317080431",
        body="It's your turn to clean",
        media_url="http://www.supakleenservices.com/images/newSupakleen/Construction.png" )

def pg5():
    from twilio.rest import Client

    client = Client(account_sid, auth_token)

    client.messages.create(
        to="+1 (510) 736-8264",
        from_="+18317080431",
        body="It's your turn to clean",
        media_url="http://www.supakleenservices.com/images/newSupakleen/Construction.png" )
