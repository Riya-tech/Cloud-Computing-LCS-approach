from lru import LRUCache
from mru import MRUCache
from utils import format_input_from_json, Logger
import logging


def simulate(input_filename):
    logger = Logger()
    logger.log_info(0, "Starting Simulation")
    input_data = format_input_from_json(input_filename)
    results = []
    for i, data in enumerate(input_data):
        logger.log_info(0, "Data Input {}\t Requests: {} Warm Containers: {}".format(
            i, sum(data["requests"]), len(data["existing_warm_container_timestamps"])))
        mru_cache = MRUCache(execution_time=1, warm_time=3)
        lru_cache = LRUCache(execution_time=1, warm_time=3)
        mru_cold_starts = mru_cache.most_recently_used_container(
            data["requests"], data["cycle"], data["existing_warm_container_timestamps"])
        lru_cold_starts = lru_cache.least_recently_used_container(
            data["requests"], data["cycle"], data["existing_warm_container_timestamps"])
        results.append([sum(data["requests"]), len(
            data["existing_warm_container_timestamps"]), lru_cold_starts, mru_cold_starts])
        logger.log_info(data["cycle"], "LRU Cold starts: {}".format(lru_cold_starts))
        logger.log_info(data["cycle"], "MRU Cold starts: {}".format(mru_cold_starts))
    logger.log_table(results)


def main():
    simulate("input.json")


if __name__ == "__main__":
    main()
