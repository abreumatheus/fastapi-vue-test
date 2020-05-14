import uuid
from .models import Products
from app.utils.base_crud import CrudBase
from app.domains.imgupload.actions import UploadActions
from app.utils import cleanup_dict_and_title_strings

_UPLOAD = UploadActions()


class ProductsActions(CrudBase):
    def get_all_products(self):
        all = self.get_all(Products)
        return all

    def get_product_by_id(self, product_id: str):
        one = self.get_one_by(Products, {'id': product_id})
        return one

    def get_all_products_by(self, query: dict):
        query = cleanup_dict_and_title_strings(query)
        all = self.get_all_by(Products, query)
        return all

    def add_new_product(self, product_in: dict):
        product_in['id'] = str(uuid.uuid4())
        product_in['photos'] = _UPLOAD.upload_image(folder_name='products', files=product_in['photos'])
        new = self.add_new(Products, product_in)
        return new

    def update_product(self, product_in: dict):
        product_in = cleanup_dict_and_title_strings(product_in)
        product_in_db = self.get_one_by(Products, {'id': product_in['id']})
        product_in_db_dict = product_in_db.__dict__
        for item in product_in:
            if item in product_in_db_dict:
                setattr(product_in_db, item, product_in[item])
        updated = self.update(product_in_db)
        return updated

    def delete_product_by_id(self, product_in):
        self.delete_by(Products, product_in)
