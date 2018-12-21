def iterate(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            iterate(value)
            continue
    print('key {!r} -> value {!r}'.format(key.encode('utf-8'), value.encode('utf-8')))

def iterate_json(data, parent=''):
  for (k, v) in data.items():
    if isinstance(v, dict):
      if parent:
        iterate_json(v, parent + '.' + k)
      else:
        iterate_json(v, k)
    else:
        print(parent + "." + str(k) + ": " + str(v))
