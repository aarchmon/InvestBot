# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils.request_util import get_slot_value

from ask_sdk_model import Response

from botocore.vendored import requests

# Financial dictionary for DictionaryIntent.
financial_terms = {
    "stock" : "A stock (also known as equity) is a security that represents the ownership of a fraction of a corporation. ",
    "common stock" : "Holders of common stock elect the board of directors and vote on corporate policies. ",
    "preferred stock" : "Preferred stockholders have a higher claim to dividends or asset distribution than common stockholders.",
    "dividends" : "A dividend is the distribution of some of a company's earnings to a class of its shareholders, as determined by the company's board of directors.",
    "bond" : "A bond is a fixed income instrument that represents a loan made by an investor to a borrower (typically corporate or governmental).",
    "volume" : "Volume is the amount of an asset or security that changes hands over some period of time, often over the course of a day.",
    "ETF" : "An exchange traded fund (ETF) is a type of security that tracks an index, sector, commodity, or other asset, but which can be purchased or sold on a stock exchange the same as a regular stock.", 
    "index fund" : "n index fund is a type of mutual fund or exchange-traded fund (ETF) with a portfolio constructed to match or track the components of a financial market index, such as the Standard & Poor's 500 Index (S&P 500).", 
    "brokerage" : "A brokerage company’s main duty is to act as a middleman that connects buyers and sellers to facilitate a transaction. ",
    "cryptocurrency" : "A cryptocurrency is a digital or virtual currency that is secured by cryptography, which makes it nearly impossible to counterfeit or double-spend."
}

# Overview of InvestBot.
investbot_overview = "InvestBot is a digital, one-stop-shop for all of your investment needs. We offer solutions and technologies for stocks, bonds, and cryptocurrencies."

# Getting started with cryptocurrencies.
getting_started_crypto = """
To get started with cryptocurrency, you will first need an account on a trading platform. eToro, Gemini, and Coinbase are a few popular 
trading platform options. 
"""

def get_BTCprice():
    """
    Retrieves the current price of bitcoin in dollars from the alternative.me Crypto API.
    """
    bitcoin_api_url = "https://api.alternative.me/v2/ticker/bitcoin/?convert=USD"
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    price_dollars = response_json["data"]["1"]["quotes"]["USD"]["price"]
    return price_dollars

def get_dogecoin_price():
    """
    Retrieves the current price of dogecoin in dollars from the alternative.me Crypto API.
    """
    dogecoin_api_url = "https://api.alternative.me/v2/ticker/dogecoin/?convert=USD"
    response = requests.get(dogecoin_api_url)
    response_json = response.json()
    price_dollars = response_json["data"]["74"]["quotes"]["USD"]["price"]
    return price_dollars

def get_litecoin_price():
    """
    Retrieves the current price of litecoin in dollars from the alternative.me Crypto API.
    """
    litecoin_api_url = "https://api.alternative.me/v2/ticker/litecoin/?convert=USD"
    response = requests.get(litecoin_api_url)
    response_json = response.json()
    price_dollars = response_json["data"]["2"]["quotes"]["USD"]["price"]
    return price_dollars

def get_ethereum_price():
    """
    Retrieves the current price of ethereum in dollars from the alternative.me Crypto API.
    """
    ethereum_coin_api_url = "https://api.alternative.me/v2/ticker/ethereum/?convert=USD"
    response = requests.get(ethereum_coin_api_url)
    response_json = response.json()
    price_dollars = response_json["data"]["1027"]["quotes"]["USD"]["price"]
    return price_dollars

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Risk Tolerance dialog. 
low_risk_tolerance = "80% bonds, 20% stocks. "
mid_risk_tolerance = "40% bonds, 40% stocks, 20% cryptocurrency. "
high_risk_tolerance = "20% bonds, 40% stocks, 40% cryptocurrency. "

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_request_type("LaunchRequest")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to InvestBot. How may I help you? "
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class OverviewIntentHandler(AbstractRequestHandler):
    """Handler for OverviewIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OverviewIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response 
        return (
            handler_input.response_builder
            .speak(investbot_overview)
            .ask(investbot_overview)
            .response
        )

class GetStartedCryptoIntentHandler(AbstractRequestHandler):
    """Handler for GetStartedCryptoIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetStartedCryptoIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        return (
            handler_input.response_builder
            .speak(getting_started_crypto)
            .ask(getting_started_crypto)
            .response
        )

class BitcoinPriceIntentHandler(AbstractRequestHandler):
    """Handler for BitcoinPriceIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BitcoinPriceIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        
        # Get price of BitCoin.
        bitcoin_price = str(get_BTCprice())
        
        # Output phrase.
        speak_output = "Bitcoin currently costs " + bitcoin_price + " US Dollars. "
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class DogecoinPriceIntentHandler(AbstractRequestHandler):
    """Handler for DogecoinPriceIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DogecoinPriceIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        
        # Get price of Dogecoin.
        dogecoin_price = str(get_dogecoin_price())
        
        # Output phrase.
        speak_output = "Dogecoin currently costs " + dogecoin_price + " US Dollars. "
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class LitecoinPriceIntentHandler(AbstractRequestHandler):
    """Handler for LitecoinPriceIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LitecoinPriceIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        
        # Get price of Dogecoin.
        litecoin_price = str(get_litecoin_price())
        
        # Output phrase.
        speak_output = "Litecoin currently costs " + litecoin_price + " US Dollars. "
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class EthereumPriceIntentHandler(AbstractRequestHandler):
    """Handler for EthereumPriceIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EthereumPriceIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        
        # Get price of Dogecoin.
        ethereum_price = str(get_ethereum_price())
        
        # Output phrase.
        speak_output = "Ethereum currently costs " + ethereum_price + " US Dollars. "
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class ProfilerIntentHandler(AbstractRequestHandler):
    """Handler for ProfilerIntentHandler."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ProfilerIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        
        # Retrieve name.
        name_slot = str(get_slot_value(handler_input, "name"))
        
        # Retrieve Profiler slots.
        name_slot = get_slot_value(handler_input, "name")
        age_slot = get_slot_value(handler_input, "age")
        risk_level_slot = get_slot_value(handler_input, "risk_level")
        account_balance_slot = get_slot_value(handler_input, "account_balance")
        
        # Save Profiler slots as Session Attributes.
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr["name"] = name_slot
        session_attr["age"] = age_slot
        session_attr["risk_level"] = risk_level_slot
        session_attr["account_balance"] = float(account_balance_slot)
        
        # Output speech.
        speak_output = "Thank you for your information " + name_slot + ". Based on your inputs, your recommended portfolio allocation is as follows: "
        
        # Retrieve risk_level slot and evaluate. 
        if risk_level_slot.lower() == "low":
            speak_output += low_risk_tolerance
        elif risk_level_slot.lower() == "mid":
            speak_output += mid_risk_tolerance
        else:
            speak_output += high_risk_tolerance
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class AccountBalanceHandler(AbstractRequestHandler):
    """AccountBalance Handler."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AccountBalance")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        
        # Retrieve Session Attributes.
        session_attr = handler_input.attributes_manager.session_attributes
        
        
        # Relay current account balance.
        speak_output = "You have " + str(session_attr["account_balance"]) + " US Dollars available for investment. "
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class DictionaryIntentHandler(AbstractRequestHandler):
    """Handler for DictionaryIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DictionaryIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        
        # Retrieve term slot.
        term_value = get_slot_value(handler_input, "term")
        speak_output = financial_terms[term_value]
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class BrokerageRecommendationIntentHandler(AbstractRequestHandler):
    """Handler for BrokerageRecommendationIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BrokerageRecommendationIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "Ameritrade, Robinhood, E-Trade, Interactive Brokers, and Webull are some prominent brokerages today. All are mobile-friendly and are easy to sign up for! "
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Thank you for using InvestBot. See you soon! "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(OverviewIntentHandler())
sb.add_request_handler(GetStartedCryptoIntentHandler())
sb.add_request_handler(BitcoinPriceIntentHandler())
sb.add_request_handler(DogecoinPriceIntentHandler())
sb.add_request_handler(LitecoinPriceIntentHandler())
sb.add_request_handler(EthereumPriceIntentHandler())
sb.add_request_handler(ProfilerIntentHandler())
sb.add_request_handler(AccountBalanceHandler())
sb.add_request_handler(DictionaryIntentHandler())
sb.add_request_handler(BrokerageRecommendationIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()