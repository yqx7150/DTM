## Training

1. To pretrain DTM_S1, run
```
sh trainS1.sh
```

4. To train DTM_S2, run
```
#set the 'pretrain_network_g' and 'pretrain_network_S1' in ./options/train_DTMS2.yml to be the path of DTM_S1's pre-trained model

sh trainS2.sh
```

**Note:** The above training script uses 8 GPUs by default. 



#### Testing 


- Testing
```
# modify the dataset path in ./options/test_DTMS2.yml

sh test.sh 
```


