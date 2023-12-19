import os
from time import sleep

os.system("pytest C://Users//ReddySaS//PycharmProjects//Upass-2.0//tests//test_manager//test_create_new_account.py --alluredir=C://Users//ReddySaS//PycharmProjects//Upass-2.0//Reports")
# os.system("pytest C://Users//ReddySaS//PycharmProjects//Upass-2.0//tests//test_manager//test_create_new_program.py --alluredir=C://Users//ReddySaS//PycharmProjects//Upass-2.0//Reports")
# os.system("pytest C://Users//ReddySaS//PycharmProjects//Upass-2.0//tests//test_manager//test_program_active.py --alluredir=C://Users//ReddySaS//PycharmProjects//Upass-2.0//Reports")
# os.system("pytest C://Users//ReddySaS//PycharmProjects//Upass-2.0//tests//test_manager//test_publish_the_program.py --alluredir=C://Users//ReddySaS//PycharmProjects//Upass-2.0//Reports")
# os.system("pytest C://Users//ReddySaS//PycharmProjects//Upass-2.0//tests//test_manager//test_verify_record_by_id.py --alluredir=C://Users//ReddySaS//PycharmProjects//Upass-2.0//Reports")
# os.system("pytest C://Users//ReddySaS//PycharmProjects//Upass-2.0//tests//test_manager//test_unpublish_the_program.py --alluredir=C://Users//ReddySaS//PycharmProjects//Upass-2.0//Reports")
# os.system("pytest C://Users//ReddySaS//PycharmProjects//Upass-2.0//tests//test_manager//test_inactivate_program.py --alluredir=C://Users//ReddySaS//PycharmProjects//Upass-2.0//Reports")


sleep(15)

os.system("allure serve C://Users//ReddySaS//PycharmProjects//Upass-2.0//Reports")
