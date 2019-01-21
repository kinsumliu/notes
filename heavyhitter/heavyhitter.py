class User:

  def __init__(self, index, rv):
    self.idx = index
    self.rv = rv
    self.generate()

  def generate(self, size=1):
    self.val = self.rv.rvs(size=size)

  def response(self, query):
    pass



class Aggregator:

  def __init__(self, index):
    self.idx = index

  def subscribe(self, users):
    self.subscribers = users

  def query(self, value):
    responses = []
    for user in self.subscribers:
      responses.append(user.response(value))
    return responses

  def aggregate(self, responses):
    pass
