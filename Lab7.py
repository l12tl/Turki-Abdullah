def TnC_closest_pair_1D(P):

  # Create a list of tuples (point, original_index)

  indexed_points = [(P[i], i) for i in range(len(P))]

   

  # Sort the points by their values

  indexed_points.sort(key=lambda x: x[0])

   

  # Initialize minimum distance to a large value

  min_dist = float('inf')

  index_p1 = -1

  index_p2 = -1

   

  # Traverse the sorted points to find the closest pair

  for i in range(1, len(indexed_points)):

    # Calculate the distance between consecutive points

    dist = abs(indexed_points[i][0] - indexed_points[i - 1][0])

     

    # If this distance is smaller than the current minimum, update the minimum

    if dist < min_dist:

      min_dist = dist

      index_p1 = indexed_points[i - 1][1] # Original index of the first point

      index_p2 = indexed_points[i][1]   # Original index of the second point

   

  return [min_dist, index_p1, index_p2]



# Example usage:

P = [10, 2, 5, 8, 15]

result = TnC_closest_pair_1D(P)

print(f"Minimum distance: {result[0]}")

print(f"Closest points indices: {result[1]}, {result[2]}")
