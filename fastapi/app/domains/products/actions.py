from app.utils.base_crud import CrudBase
from .models import Products
import uuid
from app.domains.imgupload.actions import UploadActions


_UPLOAD = UploadActions()


class ProductsActions(CrudBase):
    def get_all_products(self):
        all = self.get_all(Products)
        return all

    def get_product_by_id(self, product_id: str):
        one = self.get_one_by(Products, {'id': product_id})
        return one

    def get_all_products_by(self, query: dict):
        for item in list(query):
            if query[item] is None:
                del query[item]
            elif isinstance(query[item], str):
                query[item] = query[item].title()
        all = self.get_all_by(Products, query)
        return all

    def add_new_product(self, product_in: dict):
        product_in['id'] = str(uuid.uuid4())
        product_in['photos'] = _UPLOAD.upload_image(folder_name='products', files=product_in['photos'])
        new = self.add_new(Products, product_in)
        return new

    def update_product(self, product_in: dict):
        for item in list(product_in):
            if product_in[item] is None:
                del product_in[item]
            elif isinstance(product_in[item], str):
                product_in[item] = product_in[item].title()
        imovel = self.get_one_by(Products, {'id': product_in['id']})
        imovel_dict = imovel.__dict__
        for item in product_in:
            if item in imovel_dict:
                setattr(imovel, item, product_in[item])
        updated = self.update(imovel)
        return updated

    def delete_by_id(self, product_in):
        self.delete_by(Products, product_in)