from .models import Category
from app.utils.base_crud import CrudBase
from app.utils import cleanup_dict_and_title_strings


class CategoryActions(CrudBase):
    def get_all_categories(self):
        all = self.get_all(Category)
        return all

    def get_category_by_id(self, category_id: int):
        one = self.get_one_by(Category, {'id': category_id})
        return one

    def get_all_categories_by(self, query: dict):
        query = cleanup_dict_and_title_strings(query)
        all = self.get_all_by(Category, query)
        return all

    def add_new_category(self, category_in: dict):
        new = self.add_new(Category, category_in)
        return new

    def update_category(self, category_in: dict):
        category_in = cleanup_dict_and_title_strings(category_in)
        category_in_db = self.get_category_by_id(category_in['id'])
        category_in_db_dict = category_in_db.__dict__
        for item in category_in:
            if item in category_in_db_dict:
                setattr(category_in_db, item, category_in[item])
        updated = self.update(category_in_db)
        return updated

    def delete_category_by_id(self, category_in: int):
        self.delete_by(Category, category_in)
