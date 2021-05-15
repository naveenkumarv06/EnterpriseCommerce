import inspect
import logging


class Log:

    def get_ogger(self):

        loggername = inspect.stack()[1][3]

        logger = logging.getLogger(loggername)

        file = logging.FileHandler(r"C:\Users\naveenk\PycharmProjects\EnterpriseCommerceAutomation\Utilities\logfile.log")

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        file.setFormatter(formatter)

        logger.addHandler(file)

        logger.setLevel(logging.DEBUG)

        return logger