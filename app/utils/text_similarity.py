def calculate_similarity(current_text, historical_text):

    current_words = set(
        current_text.lower().split()
    )

    historical_words = set(
        historical_text.lower().split()
    )

    matching_words = current_words.intersection(
        historical_words
    )

    similarity_score = len(matching_words)

    return similarity_score