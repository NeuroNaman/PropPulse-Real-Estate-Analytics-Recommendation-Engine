import gzip
import pickle

with gzip.open('pipeline1.pkl.gz', 'rb') as f:
    pipeline = pickle.load(f)

print(pipeline)