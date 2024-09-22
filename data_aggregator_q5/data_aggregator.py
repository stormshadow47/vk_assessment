def aggregate_data(data: list[dict], key: str, aggregator: callable) -> dict:
 
  result = {}
  for item in data:
    key_value = item[key]
    if key_value not in result:
      result[key_value] = []
    result[key_value].append(item)

  for key_value, group in result.items():
    result[key_value] = aggregator(group)

  return result

data = [
    {'category': 'fruit', 'item': 'apple', 'quantity': 10},
    {'category': 'fruit', 'item': 'banana', 'quantity': 5},
    {'category': 'vegetable', 'item': 'carrot', 'quantity': 7},
    {'category': 'fruit', 'item': 'orange', 'quantity': 8},
    {'category': 'vegetable', 'item': 'potato', 'quantity': 12},
]

def sum_quantity(group):
    return sum(item['quantity'] for item in group)

result = aggregate_data(data, 'category', sum_quantity)
print(result)
