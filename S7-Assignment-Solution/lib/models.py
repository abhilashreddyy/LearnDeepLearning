import torch.nn as nn
import torch.nn.functional as F

class Model1(nn.Module):
    def __init__(self):
      super(Model1, self).__init__()
      # CONV BLOCK 1
      self.convblock1 = nn.Sequential(
          nn.Conv2d(in_channels = 1, out_channels =  10, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
      )#26
      self.convblock2 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels =  10, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
      )#24
      self.convblock3 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels =  10, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
      )#22

      # TRANSITION BLOCK 1
      self.pool1 = nn.MaxPool2d(2,2)#11
      self.convblock4 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels =  10, kernel_size = (1, 1), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
      )#9
      # CONVOLUTION BLOCK 2
      self.convblock5 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels = 10, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
      )#7

      # OUTPUT BLOCK
      self.convblock6 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels =  10, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
      )#7
      self.convblock7 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels =  10, kernel_size = (1, 1), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
      )#7
      self.convblock8 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels =  10, kernel_size = (7, 7), padding = 0, bias = False),
      )#1


    def forward(self, x):
      x = self.convblock1(x)#3
      x = self.convblock2(x)#5
      x = self.convblock3(x)#7
      x = self.pool1(x)#8
      x = self.convblock4(x)####
      x = self.convblock5(x)#12
      x = self.convblock6(x)#16
      x = self.convblock7(x)####
      x = self.convblock8(x)#28
      x = x.view(-1, 10)
      return F.log_softmax(x, dim=-1)
    
    
    
class Model2(nn.Module):
    def __init__(self):
      dropout_value = 0.1
      super(Model2, self).__init__()
      # CONV BLOCK 1
      self.convblock1 = nn.Sequential(
          nn.Conv2d(in_channels = 1, out_channels =  10, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#26
      self.convblock2 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels =  12, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(12),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#24
      self.convblock3 = nn.Sequential(
          nn.Conv2d(in_channels = 12, out_channels =  14, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(14),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#22

      # TRANSITION BLOCK 1
      self.pool1 = nn.MaxPool2d(2,2)#11
      self.convblock4 = nn.Sequential(
          nn.Conv2d(in_channels = 14, out_channels =  10, kernel_size = (1, 1), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#9
      # CONVOLUTION BLOCK 2
      self.convblock5 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels = 16, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(16),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#7

      # OUTPUT BLOCK
      self.convblock6 = nn.Sequential(
          nn.Conv2d(in_channels = 16, out_channels = 20 , kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(20),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#7
      self.convblock7 = nn.Sequential(
          nn.Conv2d(in_channels = 20, out_channels =  20, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(20),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#7
      self.convblock8 = nn.Sequential(
          nn.Conv2d(in_channels = 20, out_channels =  10, kernel_size = (1, 1), padding = 0, bias = False),
      )#7
      self.gap = nn.Sequential(
          nn.AvgPool2d(kernel_size = 5)
      )
      # self.convblock8 = nn.Sequential(
      #     nn.Conv2d(in_channels = 10, out_channels =  10, kernel_size = (7, 7), padding = 0, bias = False),
      # )#1


    def forward(self, x):
      x = self.convblock1(x)#3
      x = self.convblock2(x)#5
      x = self.convblock3(x)#7
      x = self.pool1(x)# 8
      x = self.convblock4(x)#8####
      x = self.convblock5(x)# 12
      x = self.convblock6(x)# 16
      x = self.convblock7(x)# 20
      x = self.convblock8(x)# 20####
      # x = self.dropout(x)
      # x = self.convblock8(x)
      x = self.gap(x) # 28
      x = x.view(-1, 10)
      return F.log_softmax(x, dim=-1)


class Model3(nn.Module):
    def __init__(self):
      dropout_value = 0.05
      super(Model3, self).__init__()
      # CONV BLOCK 1
      self.convblock1 = nn.Sequential(
          nn.Conv2d(in_channels = 1, out_channels =  10, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(10),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#26, 3
      self.convblock2 = nn.Sequential(
          nn.Conv2d(in_channels = 10, out_channels =  12, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(12),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#24, 5

      # TRANSITION BLOCK 1
      self.convblock3 = nn.Sequential(
          nn.Conv2d(in_channels = 12, out_channels =  8, kernel_size = (1, 1), padding = 0, bias = False),
          nn.BatchNorm2d(8),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#12, 6
      self.pool1 = nn.MaxPool2d(2,2)#11




      # self.convblock4 = nn.Sequential(
      #     nn.Conv2d(in_channels = 14, out_channels =  10, kernel_size = (1, 1), padding = 0, bias = False),
      #     nn.BatchNorm2d(10),
      #     nn.ReLU(),
      #     nn.Dropout(dropout_value)
      # )#9
      # CONVOLUTION BLOCK 2
      self.convblock4 = nn.Sequential(
          nn.Conv2d(in_channels = 8, out_channels = 12, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(12),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#10, 10

      # OUTPUT BLOCK
      self.convblock5 = nn.Sequential(
          nn.Conv2d(in_channels = 12, out_channels = 14 , kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(14),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#8, 14
      self.convblock6 = nn.Sequential(
          nn.Conv2d(in_channels = 14, out_channels =  14, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(14),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#6, 18
      self.convblock7 = nn.Sequential(
          nn.Conv2d(in_channels = 14, out_channels =  17, kernel_size = (3, 3), padding = 0, bias = False),
          nn.BatchNorm2d(17),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )#6, 18

      self.gap = nn.Sequential(
          nn.AvgPool2d(kernel_size = 4)
      )
      self.convblock8 = nn.Sequential(
          nn.Conv2d(in_channels = 17, out_channels =  10, kernel_size = (1, 1), padding = 0, bias = False),
      )#7
      # self.convblock8 = nn.Sequential(
      #     nn.Conv2d(in_channels = 10, out_channels =  10, kernel_size = (7, 7), padding = 0, bias = False),
      # )#1


    def forward(self, x):
      x = self.convblock1(x) #3, 26
      x = self.convblock2(x)#5, 24
      x = self.convblock3(x)#5, 10
      x = self.pool1(x)#6, 12
      # x = self.convblock3(x)#10

      x = self.convblock4(x)# 10, 10
      x = self.convblock5(x)# 14, 8
      x = self.convblock6(x)# 18, 6
      x = self.convblock7(x)# 22, 4
      x = self.convblock8(x)# 22, 4
      x = self.gap(x)# 24, 1

      # x = self.dropout(x)
      # x = self.convblock8(x)

      x = x.view(-1, 10)
      return F.log_softmax(x, dim=-1)
