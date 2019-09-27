import requests
import json
# import pdb

REMOTE_URL = 'http://localhost:3001/notify'


class RealtimApi:
    @staticmethod
    def notify(channel_name, vehicle):
        data = {
            'channel_name': channel_name,
            'object': {
                'id': vehicle.id,
                'status': vehicle.status,
                'vehicle_id': vehicle.vehicle_id,
                'reg_num': vehicle.reg_num,
                'customer_id': vehicle.customer_id,
                'customer_name': vehicle.customer_name()
            }
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(url=REMOTE_URL, data=json.dumps(data), headers=headers)
        # pdb.set_trace()