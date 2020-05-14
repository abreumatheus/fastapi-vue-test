from app.utils.base_dao import DaoBase


class CrudBase(DaoBase):
	def add_new(self, model, params: dict = None):
		if params is not None:
			new = model(**params)
		else:
			new = model()
		self.add(new)
		return new

	def update(self, the_object):
		self.merge(the_object)
		return the_object

	def get_one_by(self, model, params: dict):
		found = self.session.query(model).filter_by(**params).first()
		return found

	def get_all_by(self, model, params: dict):
		all_found = self.session.query(model).filter_by(**params).all()
		return all_found

	def delete_by(self, model, params: dict):
		found = self.session.query(model).filter_by(**params).first()
		self.delete(found)

	def get_all(self, model):
		all_found = self.session.query(model).all()
		return all_found
