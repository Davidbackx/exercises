import json
data = {}
def gemiddelde(numbers):
  index = 0
  gem = 0
  for number in numbers:
    index += 1
    gem += number
    avg = gem/index
  return avg


with open('input.json') as f:
    with open('output.txt', 'w') as output:
      datas = json.load(f)
  
      for data in datas:
        grades = data['grades']
        ids = data['id']
        avg = gemiddelde(grades)
        sortedids = ''.join((sorted(ids, key=lambda x: x[0])))
        print(f'{sortedids} {round(avg)}',file=output)

