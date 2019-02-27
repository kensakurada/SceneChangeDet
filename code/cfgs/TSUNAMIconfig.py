import os

BASE_PATH = '/home/sakurada/work/src/SceneChangeDet/code'
PRETRAIN_MODEL_PATH = os.path.join(BASE_PATH,'pretrain')
DATA_PATH = '/projects/g-nedo-geospatial/work/sakurada/work/data/pcd/pcd_2018_0906_r4s4/set0'
TRAIN_DATA_PATH = os.path.join(DATA_PATH+'/train')
TRAIN_LABEL_PATH = os.path.join(DATA_PATH+'/train')
TRAIN_TXT_PATH = os.path.join(DATA_PATH,'train.txt')
VAL_DATA_PATH = os.path.join(DATA_PATH+'/test')
VAL_LABEL_PATH = os.path.join(DATA_PATH+'/test')
VAL_TXT_PATH = os.path.join(DATA_PATH,'test.txt')
SAVE_PATH = '/projects/g-nedo-geospatial/work/sakurada/work/data/pcd_precut/SceneChangeDet/checkpoint/set0'
SAVE_CKPT_PATH = os.path.join(SAVE_PATH,'ckpt_final')
if not os.path.exists(SAVE_CKPT_PATH):
    os.makedirs(SAVE_CKPT_PATH)
SAVE_PRED_PATH = os.path.join(SAVE_PATH,'prediction_final')
if not os.path.exists(SAVE_PRED_PATH):
    os.makedirs(SAVE_PRED_PATH)
TRAINED_BEST_PERFORMANCE_CKPT = os.path.join(SAVE_CKPT_PATH,'model_best.pth')
INIT_LEARNING_RATE = 1e-7
DECAY = 5e-5
MOMENTUM = 0.90
MAX_ITER = 40000
BATCH_SIZE = 1
THRESHS = [0.1,0.3,0.5]
THRESH = 0.1
LOSS_PARAM_CONV = 1
LOSS_PARAM_FC = 1
TRANSFROM_SCALES= (1024,224)
T0_MEAN_VALUE = (128.793,108.267,98.685)
T1_MEAN_VALUE = (166.814,136.916,122.396)

