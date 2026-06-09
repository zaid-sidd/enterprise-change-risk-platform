from app.datasets.historical_changes import historical_changes
from app.utils.text_similarity import calculate_similarity


def retrieve_historical_changes(
    service_name,
    current_issue=None
):

    ranked_matches = []

    for change in historical_changes:

        service_match = (
            change["service"].lower() == service_name.lower()
        )

        similarity_score = 0

        if current_issue:

            similarity_score = calculate_similarity(
                current_issue,
                change["failure_pattern"]
            )

        if service_match or similarity_score >= 2:

            ranked_matches.append({
                "change": change,
                "similarity_score": similarity_score
            })

    ranked_matches = sorted(
        ranked_matches,
        key=lambda item: item["similarity_score"],
        reverse=True
    )

    return ranked_matches