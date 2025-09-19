# DTM
DTM: Diffusion Transformer Model Guided by Compact Prior in Low-dose PET Reconstruction    
The Code is created based on the method described in the following paper:          
Diffusion Transformer Model Guided by Compact Prior in Low-dose PET Reconstruction         
B. Huang，X. Liu，L. Fang，Q. Liu, B. Li        
Phys Med Biol. https://iopscience.iop.org/article/10.1088/1361-6560/adac25          


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

## Other Related Projects
* ALL-PET: A Low-resource and Low-shot PET Foundation Model in Projection Domain  [<font size=5>**[Paper]**</font>](https://github.com/yqx7150/RAYSOLUTION_PETdata/blob/main/Paper/ALL_PET_Finalx.pdf)   [<font size=5>**[Code]**</font>](https://github.com/yqx7150/ALL-PET)

* PET Tracer Separation using Conditional Diffusion Transformer with Multi-latent Space Learning [<font size=5>**[Paper]**</font>](https://arxiv.org/abs/2506.16934#:~:text=In%20this%20study%2C%20a%20multi-latent%20space%20guided%20texture,model%20%28MS-CDT%29%20is%20proposed%20for%20PET%20tracer%20separation.)

* Diffusion Transformer Meets Random Masks: An Advanced PET Reconstruction Framework [<font size=5>**[Paper]**</font>](https://arxiv.org/abs/2503.08339)  [<font size=5>**[Code]**</font>](https://github.com/yqx7150/DREAM)

* Synthetic CT Generation via Variant Invertible Network for Brain PET Attenuation Correction [<font size=5>**[Paper]**</font>](https://ieeexplore.ieee.org/document/10666843) [<font size=5>**[Code]**</font>](https://github.com/yqx7150/PET_AC_sCT)

* Raysolution_PET_Data [<font size=5>**[Data]**</font>](https://github.com/yqx7150/Raysolution_PET_Data)   

* Spatial-Temporal Guided Diffusion Transformer Probabilistic Model for Delayed Scan PET Image Prediction [<font size=5>**[Paper]**</font>](https://ieeexplore.ieee.org/abstract/document/10980366)   [<font size=5>**[Code]**</font>](https://github.com/yqx7150/st-DTPM)    
