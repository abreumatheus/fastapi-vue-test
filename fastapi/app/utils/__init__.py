import random
import string
import pytz
from pytz import timezone
from datetime import datetime


def ran_gen(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))


def get_datetime():
	utc = pytz.utc
	sp = timezone('America/Sao_Paulo')
	utc_dt = utc.localize(datetime.utcnow())
	sp_dt = utc_dt.astimezone(sp)
	return sp_dt.strftime("%d/%m/%Y %H:%M:%S")


def list_to_string(lista):
	sep = ';'
	return sep.join(lista)


def string_to_list(link: str):
	link = link.split(";")
	return link


if __name__ == '__main__':
	public_id = 'SUL' + ran_gen(6, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
	print(public_id)
