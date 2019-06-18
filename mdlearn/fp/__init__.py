from .fp import Fingerprint
from .wyz import WyzIndexer
from .simple import SimpleIndexer
from .rdk import ECFP4Indexer, MorganCountIndexer, Morgan1CountIndexer, PredefinedMorganCountIndexer, PredefinedMorgan1CountIndexer

encoders_dict = dict([(e.name, e) for e in (WyzIndexer, SimpleIndexer,
                                            ECFP4Indexer, MorganCountIndexer, Morgan1CountIndexer,
                                            PredefinedMorganCountIndexer, PredefinedMorgan1CountIndexer
                                            )])