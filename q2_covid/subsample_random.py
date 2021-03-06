import pandas as pd
import qiime2 

from q2_covid.common import IDSelection


def subsample_random(ids: qiime2.Metadata, n: int, seed: int=None) \
        -> IDSelection:
    if n > ids.id_count:
        raise ValueError("Value for n is larger than the number of IDs"
                         " present")

    df = ids.to_dataframe()
    samples = df.sample(n, replace=False, random_state=seed)
    inclusion = pd.Series(False, index=df.index)
    inclusion[samples.index] = True

    return IDSelection(inclusion, ids, "subsample_random")
