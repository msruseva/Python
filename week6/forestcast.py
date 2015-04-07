def forestcast(days):
    weather = {
        "sunshine": 0,
        "rain": 0,
        "snow": 0
        }
    
    for i in range(0, len(days)):
        if days[i] == "sunshine":
            weather["sunshine"] += 1
        elif days[i] == "rain":
            weather["rain"] += 1
        elif days[i] == "snow":
            weather["snow"] += 1
    
    if weather["rain"] > weather["sunshine"] and weather["rain"] > weather["snow"]:
        return "rain"
    elif weather["sunshine"] > weather["rain"] and weather["sunshine"] > weather["snow"]:
        return "sunshine"
    elif weather["snow"] > weather["rain"] and weather["snow"] > weather["sunshine"]:
        return "snow"
    elif weather["rain"] == weather["snow"] and weather["rain"] > weather["sunshine"]:
        return "sunshine"
    elif weather["sunshine"] == weather["snow"] and weather["sunshine"] > weather["rain"]:
        return "rain"
    elif weather["sunshine"] == weather["rain"] and weather["sunshine"] > weather["snow"]:
        return "snow"
    elif weather["sunshine"] == weather["rain"] == weather["snow"]:
        return days[len(days) - 1]
