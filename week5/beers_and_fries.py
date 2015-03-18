def max_score(beers, fries):
    beers = sorted(beers)
    fries = sorted(fries)
    max_score = 0
    index = 0

    while index < len(beers):
        max_score += beers[index] * fries[index]
        index += 1
            
    return max_score
