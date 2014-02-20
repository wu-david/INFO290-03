from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

import re

WORD_RE = re.compile(r"[\w']+")


class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches,
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/

    def extract_business(self, _, record):
        if record['type'] == 'review':
            yield [record['user_id'], record['business_id']]

    def business_set(self, uid, bid): #[user_id, business_id]
        business_ids = list(set(bid))
        yield ["SETS", [uid, business_ids]] 

    def jaccard_index(self, _, user_business_ids):
        ubi = list(user_business_ids)
        for user_a, bid_a in ubi:
            for user_b, bid_b in ubi:
                if user_a < user_b:
                    index = self.jaccard(bid_a, bid_b)
                    if index >= 0.5:
                        yield [(user_a, user_b), index]

    def jaccard(self, a, b):
        a = set(a)
        b = set(b)
        intersection = a & b
        union = a | b
        return float(len(intersection)) / float(len(union))


    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [
            self.mr(self.extract_business, self.business_set),
            self.mr(reducer=self.jaccard_index),
#            self.mr(mapper=self.mapper1, reducer=self.reducer1),
#            self.mr(mapper=...),
        ]


if __name__ == '__main__':
    UserSimilarity.run()
