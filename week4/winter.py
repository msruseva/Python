def winter_is_coming(seasons):
    is_coming = False

    counter = 0

    for season in seasons:
        if season == "winter":
            counter = 0
        else:
            counter += 1

        if counter == 5:
            is_coming = True
            break

    return is_coming
