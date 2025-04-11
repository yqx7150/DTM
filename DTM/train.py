# flake8: noqa
import os.path as osp

import sys
sys.path.append('/home/b109/lxb/DiffIR-master/DiffIR-demotionblur/DTM-master/DTM')
sys.path.append('/home/b109/lxb/DiffIR-master/DiffIR-demotionblur/DTM-master')
from DTM.train_pipeline import train_pipeline
import DTM.archs
import DTM.data
import DTM.models
import DTM.losses
import warnings

warnings.filterwarnings("ignore")

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    train_pipeline(root_path)
