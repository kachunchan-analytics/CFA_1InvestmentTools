def arithmetic_mean(data):
  """Calculates the arithmetic mean of a list of numbers.

  Args:
    data: A list of numbers.

  Returns:
    The arithmetic mean of the data.
  """
  return sum(data) / len(data)

def geometric_mean(data):
  """Calculates the geometric mean of a list of numbers.

  Args:
    data: A list of numbers.

  Returns:
    The geometric mean of the data.
  """
  product = 1
  for x in data:
    if x <= 0:
      raise ValueError("Geometric mean cannot be calculated with non-positive values.")
    product *= x
  return product ** (1 / len(data))

def harmonic_mean(data):
  """Calculates the harmonic mean of a list of numbers.

  Args:
    data: A list of numbers.

  Returns:
    The harmonic mean of the data.
  """
  if any(x <= 0 for x in data):
    raise ValueError("Harmonic mean cannot be calculated with non-positive values.")
  return len(data) / sum(1 / x for x in data)

if __name__ == "__main__":
  data = [1, 2, 3, 4, 5]
  print(f"Arithmetic Mean: {arithmetic_mean(data)}")
  print(f"Geometric Mean: {geometric_mean(data)}")
  print(f"Harmonic Mean: {harmonic_mean(data)}")