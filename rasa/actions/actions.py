# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import arrow
import dateparser
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



class ActionGetNearestStation(Action):

    def name(self) -> Text:
        return "Action_Get_Nearest_Station"  

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I am fetching the nearest station information.")
        dispatcher.utter_message(text=".")
        dispatcher.utter_message(text=".")
        dispatcher.utter_message(text="done.")
        return []
    

class ActionToChargingStation(Action):

    def name(self) -> Text:
        return "Action_To_Charging_Station" 
    

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        station = list(tracker.get_latest_entity_values("place"))

        if station:
            
            station_name = station[0]  
            dispatcher.utter_message(text=f"I understand. Taking you to the {station_name} charging station.")
        else:
            
            dispatcher.utter_message(text="i did not extract a location")
        
        return []
    

       
    
    



class ActionHowLongToCharge(Action):

    def name(self) -> Text:
        return "Action_How_Long_To_Charge" 
    

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="It takes 20hr on slow, 12hr on 7kw fast, 7hr on 22kw fast, 1 hr on 43-50kw rapid, 30min on 150kw charge")
        
        
        return []
    
class ActionDistanceICanGo(Action):

    def name(self) -> Text:
        return "Action_Distence_I_Can_Go" 
    

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="depending on your car and driving style. you can expect between. 320 to 480km on a full charge")
        
        
        return []

    

class ActionFilterStations(Action):

    def name(self) -> Text:
        return "Action_Filter_Stations"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        filter_preferences = tracker.get_slot("filter_preferences")

        if filter_preferences:
            dispatcher.utter_message(text=f"Filtering stations based on your preference: {filter_preferences}")
        else:
            dispatcher.utter_message(text="No filter preferences found. Showing all stations.")
        
        return []





class ActionTrafficInfo(Action):

    def name(self) -> Text:
        return "Action_Traffic_Info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sorry, I couldn't fetch traffic information at the moment. Please try again later.")
        return []






class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sorry, I didn't get that. Can you rephrase?")
        return []