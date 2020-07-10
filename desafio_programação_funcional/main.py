from collections import defaultdict
from datetime import datetime
from itertools import groupby
from operator import itemgetter

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):
    data = list()
    call = dict()
    fee_fixed = 0.36
    fee_call = 0.09

    for record in records:
        call['source'] = record['source']
        start_date = datetime.fromtimestamp(record['start'])
        end_date = datetime.fromtimestamp((record['end']))

        if start_date.strftime('%Y/%m/%d') == end_date.strftime('%Y/%m/%d'):

            if 6 <= start_date.hour < 22:
                if 6 <= end_date.hour < 22:
                    duration = end_date - start_date
                    call['total'] = fee_fixed + ((duration.seconds // 60 % 60) * fee_call)

            if 6 <= start_date.hour < 22:
                duration = end_date - start_date
                call['total'] = fee_fixed + ((duration.seconds // 60 % 60) * fee_call)

            else:
                call['total'] = fee_fixed

        data.append(call.copy())
        call.clear()

    new_data = list()
    new_call = dict()
    for k, v in groupby(sorted(data, key=itemgetter('source')), itemgetter('source')):
        temp_list = list(map(itemgetter('total'), v))
        total = 0
        for i in temp_list:
            total +=float(i)

        new_call['source'] = k
        new_call['total'] = float(f'{total:.2f}')

        new_data.append(new_call.copy())
        new_call.clear()

    result = sorted(new_data, key=itemgetter('total'), reverse=True)
    return result





print(classify_by_phone_number(records))