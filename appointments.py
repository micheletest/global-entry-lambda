import os
import requests
from datetime import datetime
from twilio.rest import Client

GLOBAL_ENTRY_MAIN_URL = 'https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=3&locationId={location_id}&minimum=1'
LOCATION_IDS = [5140, 5444, 6480]  # JFK, EWR, Bowling Green respectively
PREFERRED_TIMESLOTS = [{'StartTime': datetime.strptime('Jun 12 2023', '%b %d %Y'),
                        'EndTime': datetime.strptime('Jun 24 2023', '%b %d %Y')},
                       {'StartTime': datetime.strptime('Jul 18 2023', '%b %d %Y'),
                        'EndTime': datetime.strptime('Jul 26 2023', '%b %d %Y')}]
TWILIO_TEXT_TO = os.getenv('TWILIO_TEXT_TO')
TWILIO_TEXT_FROM = os.getenv('TWILIO_TEXT_FROM')
# twilio_client = Client()


def parse_timeslot_datetime(timeslot: dict) -> dict:
    """Parse the timestamp of a single timeslot."""
    return datetime.strptime(timeslot["startTimestamp"], "%Y-%m-%dT%H:%M")


def get_timeslots_for_location(location_id):
    r = requests.get(GLOBAL_ENTRY_MAIN_URL.format(location_id=location_id))
    timeslots = [parse_timeslot_datetime(timeslot) for timeslot in r.json()]
    return sorted(list(set(timeslots)))


def check_for_great_timeslots(timeslots):
    for timeslot in timeslots:
        if (timeslot > PREFERRED_TIMESLOTS[0]['StartTime'] and timeslot < PREFERRED_TIMESLOTS[0]['EndTime']) or (timeslot > PREFERRED_TIMESLOTS[1]['StartTime'] and timeslot < PREFERRED_TIMESLOTS[1]['EndTime']):
            print('got a good timeslot')
        else:
            print('not')


def handler(event, context):
    print('main')
    for location_id in LOCATION_IDS:
        timeslots = get_timeslots_for_location(location_id)
        print(timeslots)
        good_timeslot = check_for_great_timeslots(timeslots)

    # if ochd_home == 0 or ochd_covid_page == 0:
    #     message = twilio_client.messages.create(to=TWILIO_TEXT_TO, from_=TWILIO_TEXT_FROM,
    #                                             body=f'POTENTIAL AVAILABILITY! home:{ochd_home}, covid:{ochd_covid_page} {OCHD_MAIN_URL}')
    # else:
    #     print('Nothing to see here')
