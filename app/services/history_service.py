from app.datasets.historical_changes import historical_changes


def retrieve_historical_changes(service_name):

    matching_changes = []

    for change in historical_changes:

        if change["service"].lower() == service_name.lower():

            matching_changes.append(change)

    return matching_changes