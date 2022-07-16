import os
import sys
current_file_name = __file__
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(current_file_name))) + '/src'
sys.path.append(current_dir)
print(current_dir)

from dgld.utils.dataset import GraphNodeAnomalyDectionDataset
from dgld.models.CONAD import CONAD
from dgld.models.CONAD import get_parse
from dgld.utils.evaluation import split_auc

import dgl
import torch
import numpy as np


if __name__ == '__main__':
    """
    sklearn-like API for most users.
    """
    """
    using GraphNodeAnomalyDectionDataset 
    """
    # args = get_parse()
    # gnd_dataset = GraphNodeAnomalyDectionDataset("Cora")
    # g = gnd_dataset[0]
    # label = gnd_dataset.anomaly_label
    # model = CONAD(feat_size=1433)
    # model.fit(g, num_epoch=1, device='cpu')
    # result = model.predict(g, device='cpu')
    # print(split_auc(label, result))

    """
    custom dataset
    """
    # args = get_parse()
    # g = dgl.graph((torch.tensor([0, 1, 2, 4, 6, 7]), torch.tensor([3, 4, 5, 2, 5, 2])))
    # g.ndata['feat'] = torch.rand((8, 4))
    # label = np.array([1, 2, 0, 0, 0, 0, 0, 0])
    # model = CONAD(feat_size=4)
    # model.fit(g, num_epoch=1, device='cpu')
    # result = model.predict(g, auc_test_rounds=2)
    # print(split_auc(label, result))
    
    """[command line mode]
    test command line mode
    """
    args = get_parse()
    print(args)
    
    gnd_dataset = GraphNodeAnomalyDectionDataset(args['dataset'])
    g = gnd_dataset[0]
    label = gnd_dataset.anomaly_label
    model = CONAD(**args["model"])
    model.fit(g, **args["fit"])
    result = model.predict(g, **args["predict"])
    print(split_auc(label, result))