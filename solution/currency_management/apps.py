import threading
import time
import requests

from django.apps import AppConfig


class CurrencyManagementConfig(AppConfig):
    name = 'currency_management'

    # note: the currencies initial values implemented in the migration
    CURRENCIES = [
        ('USD', "United States Dollar", 0.290933),
        ('CAD', "Canadian Dollar", 0.389428),
        ('JPY', "Japaneses Yen", 30.7421),
        ('GBP', "Great Briton Pound", 0.226413),
        ('EUR', "Euro", 0.248382)
    ]
    CURRENCIES_NAME = list(map(lambda currency: (currency[0], currency[1]), CURRENCIES))
    CURRENCY_MODEL = None  # assigned after initializing the app (in ready function)
    CURRENCY_SERVER_URL = "http://api.openrates.io/latest"
    CURRENCY_SERVER_URL_PARAMS = "?base=ILS&symbols={}".format(",".join(map(lambda x: x[0], CURRENCIES)))
    CURRENCY_SERVER_INTERVAL_TIME = 30  # min

    def ready(self):
        CurrencyManagementConfig.CURRENCY_MODEL = self.get_model('Currency')
        t = threading.Thread(target=self.update_currency_values,
                             args=(CurrencyManagementConfig.CURRENCY_MODEL,
                                   CurrencyManagementConfig.CURRENCY_SERVER_INTERVAL_TIME * 60,
                                   CurrencyManagementConfig.CURRENCY_SERVER_URL +
                                   CurrencyManagementConfig.CURRENCY_SERVER_URL_PARAMS), daemon=True)
        t.start()

    def update_currency_values(self, model, sleep_time, url):
        response = requests.get(url)
        if response.ok:
            for cur_name, val in response.json()['rates'].items():
                res = model.objects.filter(currency_name__contains=cur_name)
                if len(res):
                    cur_obj = res[0]
                    cur_obj.value = val
                    cur_obj.save()
            time.sleep(sleep_time)
            self.update_currency_values(model, sleep_time, url)
