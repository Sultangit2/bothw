from aiogram.utils import executor
import logging
from config import dp

from handlers import client, callback,  admin, extra,fsmAdminMentor

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_hadlers_extra(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)
admin.register_handlers_client(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True)