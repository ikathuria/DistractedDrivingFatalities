DATA_PATH = 'data/'
ACCIDENT_PATH = DATA_PATH + '*/ACCIDENT.csv'
DISTRACT_PATH = DATA_PATH + '*/DISTRACT.csv'
VEHICLE_PATH = DATA_PATH + '*/VEHICLE.csv'
PERSON_PATH = DATA_PATH + '*/PERSON.csv'
MERGED_DATA_PATH = DATA_PATH + 'full_merged_data.csv'

accident_cols = ['ST_CASE', 'YEAR', 'FATALS']
distract_cols = ['ST_CASE', 'VEH_NO', 'MDRDSTRD']
vehicle_cols = ['ST_CASE', 'VEH_NO']
person_cols = ['ST_CASE', 'VEH_NO', 'PER_TYP', 'INJ_SEV']

# Available from 2010-2019 as MDRDSTRD
distraction_codes = {
    0: "Not Distracted",

    1: "Looked but Did Not See",

    3: "By Other Occupants",
    4: "By a Moving Object in Vehicle",
    12: "Distracted by Outside Person, Object or Event",

    13: "Eating or Drinking",
    14: "Smoking Related",

    5: "While Talking or Listening to Mobile Phone",
    6: "While Manipulating Mobile Phone",
    15: "Other Mobile Phone Related",

    7: "While Adjusting Audio or Climate Controls",
    9: "While Using Other Components/Controls Integral to Vehicle",
    10: "While Using or Reaching for Device/Object Brought Into Vehicle",

    17: "Distraction/Inattention",
    18: "Distraction/Careless",
    19: "Careless/Inattentive",
    93: "Inattention - Inattentive, Details Unknown",
    97: "Lost in Thought/Daydreaming",

    92: "Distraction - Distracted, Details Unknown",
    96: "Not Reported",
    98: "Other Distraction",
    99: "Reported as Unknown if Distracted"
}

distraction_categories = {
	'Not Distracted/Unknown': [0, 1, 92, 96, 98, 99],
	'Carelessness/Inattention': [17, 18, 19, 93, 97],
	'Passenger/Moving Objects': [3, 4, 12],
	'Mobile Phone': [5, 6, 15],
	'Car Controls/Devices': [7, 9, 10],
	'Eating/Smoking': [13, 14],
}
