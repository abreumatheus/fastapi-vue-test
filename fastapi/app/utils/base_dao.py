from app.db.session import session


class DaoBase:
	def __init__(self):
		self.session = session

	def add(self, the_object: object):
		self.session.add(the_object)
		self.session.commit()

	def merge(self, the_object: object):
		self.session.merge(the_object)
		self.session.commit()

	def delete(self, the_object: object):
		self.session.delete(the_object)
		self.session.commit()
