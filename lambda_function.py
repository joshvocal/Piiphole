from urllib.request import Request, urlopen 

#
# Builders
#

def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech
 
    
def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card
    
    
def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response
    
#
# Responses
#

def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return build_response(speechlet)

#
# Custom Intents
#

def peephole_intent(event, context):
    try:
        # urlopen('https://piiphole.localtunnel.me/take-picture')
        # urlopen('https://piiphole.localtunnel.me/upload')
        camera_response = urlopen('https://piiphole.localtunnel.me/search-face')
        body_response = '%s is at the door.' % camera_response.read().decode()
    except:
        body_response = 'Hmm, something went wrong.'
        

    return statement("Piiphole", body_response)

#
# Required Intents
#

def cancel_intent():
    return statement("Cancel", "You want to cancel")
    
    
def stop_intent():
    return statement("Stop", "You want to stop")
    
    
def help_intent():
    return statement("Stop", "You want help")

#
# On Launch
#

def on_launch(event, context):
    return statement("This is the title", "This is the body")

#
# Routing
#

def intent_router(event, context):
    intent = event['request']['intent']['name']

    # Required Intents
    if intent == "AMAZON.CancelIntent":
        return cancel_intent()

    if intent == "AMAZON.HelpIntent":
        return help_intent()

    if intent == "AMAZON.StopIntent":
        return stop_intent()
        
    # Custom Intents
    if intent == "TestIntent":
        return statement("Unknown", "Sorry, I'm not sure about that.")
    
    if intent == "PeepholeIntent":
        return peephole_intent(event, context)


#
# Main
#

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)
        