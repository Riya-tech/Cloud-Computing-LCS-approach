from utils import Logger


class LRUCache:
    def __init__(self, execution_time=1, warm_time=3):
        self.warm_containers = []
        self.container_timestamps = []
        self.warm_time = warm_time
        self.execution_time = execution_time
        self.container_lifetime = warm_time + execution_time
        self.logger = Logger()

    def count_requests(requests):
        return sum(requests)

    def least_recently_used_container(self, requests, cycle, existing_warm_container_timestamps=[]):
        num_cold_starts = 0

        for t in range(cycle):
            for i in range(len(self.warm_containers)):
                if t >= self.container_timestamps[i] and t < self.container_timestamps[i]+self.execution_time:
                    self.warm_containers[i] = 1
                elif t >= self.container_timestamps[i] + self.execution_time and t < self.container_timestamps[i] + self.container_lifetime:
                    self.warm_containers[i] = 0

            existing_warm_containers = existing_warm_container_timestamps.count(
                t)
            if existing_warm_containers != 0:
                self.logger.log_info(
                    t, "Initializing {} warm containers".format(existing_warm_containers))
            for x in range(existing_warm_containers):
                self.warm_containers.append(1)
                self.container_timestamps.append(t)

            self.logger.log_info(
                t, "No. of warm containers available: {}".format(self.warm_containers.count(0)))
            request_idx = 0
            for request_idx in range(requests[t]):
                self.logger.log_info(
                    t, "No. of incoming requests: {}".format(requests[t]))
                lru_container_index = -1
                for i, container in enumerate(self.warm_containers):
                    if container == 0:
                        if lru_container_index == -1:
                            lru_container_index = i
                        elif self.container_timestamps[i] < self.container_timestamps[lru_container_index]:
                            lru_container_index = i

                if lru_container_index != -1:
                    self.logger.log_info(
                        t, "Warm container with container index {} used".format(lru_container_index))
                    self.warm_containers[lru_container_index] = 1
                    self.container_timestamps[lru_container_index] = t
                else:
                    self.warm_containers.append(1)
                    self.container_timestamps.append(t)
                    num_cold_starts += 1
                    self.logger.log_info(
                        t, "Cold Start has occured")

            for i in range(len(self.warm_containers)):
                if t >= self.container_timestamps[i] + self.container_lifetime:
                    self.warm_containers[i] = -1

        return num_cold_starts
