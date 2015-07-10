
import sys

from yelp_batch import Batch

from replication_handler.components.heartbeat_searcher import HeartbeatSearcher


class MySQLHeartbeatSearchBatch(Batch):
    """Batch which runs the heartbeat searcher component from the command line.
    Useful for manual testing.

    To use from the command line:
        python -m replication_handler.batch.mysql_heartbeat_search {heartbeat_sequence_num}
    Prints information about the heartbeat or None if the heartbeat could
    not be found.
    """

    notify_emails = [
        "bam+replication+handler@yelp.com"
    ]

    def __init__(self, hb_seq_num):
        super(MySQLHeartbeatSearchBatch, self).__init__()
        self.hb_seq_num = hb_seq_num

    def run(self):
        """Runs the batch by calling out to the heartbeat searcher component"""
        print HeartbeatSearcher().get_position(self.hb_seq_num)


if __name__ == '__main__':
    MySQLHeartbeatSearchBatch(int(sys.argv[1])).start()