import torch
import torch.nn as nn
import matplotlib.pyplot as plt

def trainer(model, train_dataloader, val_dataloader, num_epochs, path_to_save='/home/atharva',
          checkpoint_path='/home/atharva',
          checkpoint=100, train_batch=1, test_batch=1, device='cuda:0'): # 2 Marks. 
    """
    Everything by default gets shifted to the GPU. Select the device according to your system configuration
    If you do no have a GPU, change the device parameter to "device='cpu'"
    :param model: the Classification model..
    :param train_dataloader: train_dataloader
    :param val_dataloader: val_Dataloader
    :param num_epochs: num_epochs
    :param path_to_save: path to save model
    :param checkpoint_path: checkpointing path
    :param checkpoint: when to checkpoint
    :param train_batch: 1
    :param test_batch: 1
    :param device: Defaults on GPU, pass 'cpu' as parameter to run on CPU. 
    :return: None
    """
    #torch.backends.cudnn.benchmark = True #Comment this if you are not using a GPU...
    # set the network to training mode.
    model.cuda()  # if gpu available otherwise comment this line. 
    # your code goes here. 
    
    

    plt.plot(training_acc)
    plt.plot(val_acc)
    plt.plot(training_loss)
    plt.plot(val_loss)
    plt.show()

