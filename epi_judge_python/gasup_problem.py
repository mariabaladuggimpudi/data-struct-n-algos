def gasup_problem(gallons, distance):
    mileage = 20
    min_city_n_dist = (0, 0)
    city_no_count = 1
    mileage_remaining = 0
    for g, d in zip(gallons, distance):
        next_city_mileage_remaining = g*mileage - d + mileage_remaining
        if next_city_mileage_remaining < min_city_n_dist[1]:
            min_city_n_dist = (city_no_count+1, next_city_mileage_remaining)
        mileage_remaining = next_city_mileage_remaining
        city_no_count += 1
    return min_city_n_dist