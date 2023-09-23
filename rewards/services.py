
import uuid
import re
import math
from datetime import datetime
from rewards.pointsdb import REWARDS


"""
Generate random uuid (id)
"""
def id_generator():
    return uuid.uuid1()


"""
Return points by id
"""
def get_points(id):
    if id in REWARDS:
        return REWARDS[id]
    return False


"""
Calulate reward points with json ticket 
"""
def calculate_rewards(ticket):
    total_point = 0
    # Retail points
    total_point += retail_name(ticket['retailer'])

    # Total bill
    total_point += total_bill(ticket['total'])

    # Items
    total_point += items_count(ticket['items'])

    # Description item
    total_point += description_item(ticket['items'])

    # Purchase date
    total_point += day_purchase(ticket['purchaseDate'])

    # Purchase Time
    total_point += time_purchase(ticket['purchaseTime'])

    id_reward = id_generator()
    # Add points to local storage dict
    REWARDS[str(id_reward)] = total_point

    # Return dict
    data = {
        "id": id_reward
    }

    return data


"""
10 points if the time of purchase is after 2:00pm and before 4:00pm.
"""
def time_purchase(purchase_time):
    date_format = '%H:%M'

    time = datetime.strptime(purchase_time, date_format)
    start = datetime.strptime('14:00', date_format)
    end = datetime.strptime('16:00', date_format)

    if time >= start and time < end:
        return 10

    return 0

"""
6 points if the day in the purchase date is odd.
"""
def day_purchase(purchase_date):
    date_format = '%Y-%m-%d'

    date = datetime.strptime(purchase_date, date_format)
    day = date.strftime("%d")

    if int(day) % 2 > 0:
        return 6

    return 0


"""
If the trimmed length of the item description is a multiple of 3, 
multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
"""
def description_item(items):
    item_poits = 0
    for item in items:
        if len(item['shortDescription'].strip()) % 3 == 0:
            item_poits += math.ceil(float(item['price']) * 0.2)

    return item_poits


"""
5 points for every two items on the receipt.
"""
def items_count(items):
    no_items = len(items)
    return math.floor(no_items / 2) * 5


"""
50 points if the total is a round dollar amount with no cents. 25 points if the total is a multiple of 0.25.
"""
def total_bill(total):
    points = 0
    # Get de decimal value from string
    frac = int(total.split('.')[1])

    if frac == 0:
        points += 50
    if (frac % 25) == 0:
        points += 25

    return points


"""
One point for every alphanumeric character in the retailer name.
"""
def retail_name(name):
    # Clean retail name, only alphanumeric characters
    retail = re.sub('[^A-Za-z0-9]+', '', name)

    # Return length of string, which will be the number of points
    return len(retail)
