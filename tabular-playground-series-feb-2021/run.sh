export TRAINING_DATA=input/train_folds.csv 
export TEST_DATA=input/test.csv 

# stage 1
MODEL=xgbm STAGE=1 SAVE_VALID=False TARGET_COL=target python3 -m src.train