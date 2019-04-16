from hello import models
from lib import mp_api


def cache_problems_at_coordinates(lat, lon, area_id):
    processor = models.ProblemProcessor

    problem_models = []

    boulder_payload = mp_api.get_boulders_at_coordinates(lat, lon)
    for problem in boulder_payload:
        problem_models.append(processor.create_problem(
            mp_id=problem.mp_id, boulder=True, location=problem.location,
            lat=problem.lat, lon=problem.lon, name=problem.name, area_id=area_id),
            mp_url=problem.url, grade=problem.grade)

    route_payload = mp_api.get_routes_at_coordinates(lat, lon)
    for problem in route_payload:
        problem_models.append(processor.create_problem(
            mp_id=problem.mp_id, boulder=False, location=problem.location,
            lat=problem.lat, lon=problem.lon, name=problem.name, area_id=area_id,
            mp_url=problem.url, grade=problem.grade))

    for problem in problem_models:
        processor.save_problem(problem)
