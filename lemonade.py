
import pandas as pd
import tensorflow as tf
import numpy as np


#1 파일에서 데이터 읽어와서 독립,종속변수 분리하기
filePath = "https://raw.githubusercontent.com/OldBegin/Exec1_Tensorflow/master/data/lemonade.csv"
lemonAde = pd.read_csv(filePath)
xTemperature = lemonAde[['온도']]
ySalesAmount = lemonAde[['판매량']]

#2 모델의 구조를 만들기
X = tf.keras.layers.Input(shape=[1]) # [1] 독립변수의 수
Y = tf.keras.layers.Dense(1)(X) # (1) 종속변수의 수
model.complie = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

#3 데이터로 모델을 학습(FIT)
model.fit(xTemperature, ySalesAmount, epoch=100)


#4 사용하기
