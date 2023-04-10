import json
import logging
from table_logger import TableLogger


def format_input_from_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data["inputs"]


class Logger:

    def log_table(self, data):
        table = TableLogger(
            columns="Warm containers, Function Requests, LRU Cold Starts, MRU Cold Starts")
        for ele in data:
            table(ele[0], ele[1], ele[2], ele[3])

    def log_info(self, time, msg):
        logging.basicConfig(filename="results.log",
                            format='%(asctime)s %(message)s', filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.info("t={}: {}".format(time, msg))
