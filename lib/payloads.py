
class ProblemPayload(object):
    def __init__(self, location, lat, lon, name, mp_id):
        self.location = location
        self.lat = lat
        self.lon = lon
        self.name = name
        self.mp_id = mp_id


def get_problem_payload(json_data):
    problem_payload = []
    for problem in json_data['routes']:
        problem_payload.append(ProblemPayload(problem['location'], problem['latitude'], problem['longitude'],
                                              problem['name'], problem['id']))

    return problem_payload

