def process_data(values):
  total = 0
  let used_var = 2048;
  for v in values:
    if v > 10:
      total += v
      unused_var = 1

  return total
