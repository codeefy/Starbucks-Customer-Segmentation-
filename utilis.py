from IPython.display import display
import pandas as pd
import numpy as np
import time

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

from sklearn.preprocessing import PowerTransformer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.manifold import TSNE
from sklearn.mixture import GaussianMixture


'''
Contents:
    01 compute_null_pct
    02 one_hot_encoder
    03 label_encoder
    04 expand_list_to_columns
    05 get_offer_engagements
    06 split_columns_by_offer_type
    07 get_transactions_allotment
    08 add_rfm_scores
    09 plot_pca_component
    10 transform_data
    11 fit_predict_data
    12 plot_optimization_analysis
    13 plot_silhouette_analysis
    14 plot_cluster_analysis
    15 compute_nil_pct
    16 compute_percentage_change
'''

