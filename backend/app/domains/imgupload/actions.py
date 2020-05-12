from PIL import Image
import tempfile
from . import s3, client, bucket_name
import uuid


class UploadActions:
    def upload_image(self, folder_name, files):
        file_list = []
        for file in files:
            image = Image.open(file.file)
            file_id = str(uuid.uuid4())
            key = file_id + '.jpeg'
            image.thumbnail((1920, 1080))
            in_mem_file = tempfile.SpooledTemporaryFile()
            image.save(in_mem_file, 'JPEG')
            in_mem_file.seek(0)
            s3.Bucket(bucket_name).put_object(Key=folder_name + '/' + key, Body=in_mem_file, ContentType='image/JPEG',
                                              ACL='public-read')
            file_list.append(file_id)
        return file_list

    def delete_image(self, folder_name, files: list):
        for file in files:
            client.delete_object(Bucket=bucket_name, Key=folder_name + '/' + file + '.jpeg')
