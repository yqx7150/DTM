# DTM
DTM: Diffusion Transformer Model Guided by Compact Prior in Low-dose PET Reconstruction
The Code is created based on the method described in the following paper:     
Diffusion Transformer Model Guided by Compact Prior in Low-dose PET Reconstruction    
B. Huang， X. Liu， L. Fang， Q. Liu，B. Li  
IEEE Journal of Biomedical and Health Informatics            

## Optional parameters:  
weight: Weight for forward loss.   
epoch: Specifies number of iterations.
 
## The training pipeline of DTM
 <div align="center"><img src="https://github.com/yqx7150/DTM/blob/main/figs/fig1.PNG"> </div>
 
## Two visualization pipeline of DTM
 <div align="center"><img src="https://github.com/yqx7150/DTM/blob/main/figs/fig2.PNG"> </div>
 
## The results of PET images
 <div align="center"><img src="https://github.com/yqx7150/DTM/blob/main/figs/fig3.PNG"> </div>


## Training

1. To pretrain DiffIR_S1, run
```
sh trainS1.sh
```

2. To train DiffIR_S2, run
```
#set the 'pretrain_network_g' and 'pretrain_network_S1' in ./options/train_DiffIRS2.yml to be the path of DiffIR_S1's pre-trained model

sh trainS2.sh

```

## Evaluation

#### Testing on GoPro dataset

- Download GoPro testset, run
```
python download_data.py --data test --dataset GoPro
```

- Testing
```
# modify the dataset path in ./options/test_DiffIRS2.yml

sh test.sh 
```

#### Testing on HIDE dataset

- Download HIDE testset, run
```
python download_data.py --data test --dataset HIDE
```

- Testing
```
# modify the dataset path in ./options/test_DiffIRS2.yml

sh test.sh
```
