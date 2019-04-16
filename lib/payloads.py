
class ProblemPayload(object):
    def __init__(self, location, lat, lon, name, mp_id, url, grade):
        self.location = location
        self.lat = lat
        self.lon = lon
        self.name = name
        self.mp_id = mp_id
        self.url = url
        self.grade = grade


def get_problem_payload(json_data):
    problem_payload = []
    for problem in json_data['routes']:
        problem_payload.append(ProblemPayload(problem['location'], problem['latitude'], problem['longitude'],
                                              problem['name'], problem['id'], problem['url'], problem['rating']))

    return problem_payload

