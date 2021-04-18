# Import required modules. 
import json

def lambda_handler(event, context):
    """
    Main Amazon Lambda event handler.
    
    :param event: Name of event.
    :param context: Context of event.
    :type event: String.
    :type context: String.
    """
    intent_name = event["currentIntent"]["name"]
    session_attributes = event["sessionAttributes"]
    
    if intent_name == "Profiler":
        return close(session_attributes, "Fulfilled", build_response_message("All good!"))
    
    raise Exception("Intent with name " + intent_name + " not supported")

def close(session_attributes, fulfillment_state, message):
    """
    Close an Amazon Lex Intent. 
    
    :param session_attributes: Session Attributes.
    :param fulfillment_state: State of fulfillment.
    :param message: Message to deliver.
    :type session_attributes: String.
    :type fulfillment_state: String.
    :type message: String.
    """
    response = {
        "sessionAttributes" : session_attributes,
        "dialogAction" : {
            "type" : "Close",
            "fulfillmentState" : fulfillment_state,
            "message" : message
        }
    }
    
    return response

def build_response_message(message):
    """
    Returns the response message for any givent Amazon Intent.
    
    :param message: Content of message to be returned by Lex bot.
    :type message: String.
    """
    return {"contentType" : "PlainText", "content" : message}