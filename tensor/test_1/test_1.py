import tensorflow as tf
tf.enable_eager_execution()
import numpy as np
import os
import time
path_to_file=r'E:\tensor\shakespeare.txt'
text = open(path_to_file).read()
# length of text is the number of characters in it
vacab = sorted(set(text))
char2idx={u:i for i,u in enumerate(vacab)}
idx2char=np.array(vacab)
text_as_int=np.array([char2idx[u] for u in text])