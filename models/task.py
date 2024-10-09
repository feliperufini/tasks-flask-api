class Task:
  def __init__(self, id, title, description, closed=False) -> None:
    self.id = id
    self.title = title
    self.description = description
    self.closed = closed

  def toDictionary(self):
    return {
      "id": self.id,
      "title": self.title,
      "description": self.description,
      "closed": self.closed
    }