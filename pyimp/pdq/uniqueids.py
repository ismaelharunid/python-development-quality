

def unique_id_generator(uid=0):
  def unique_id(uid=0):
    while True:
      uid += 1
      yield uid
  return unique_id(uid)

