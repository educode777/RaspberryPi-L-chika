# coding: utf-8
# 1.ライブラリのインポート
import RPi.GPIO as GPIO
import time

# 2.ピン番号の割り当て設定
GPIO.setmode(GPIO.BOARD)

# 3.ピン番号を変数LEDにセット
LED = 26#40

# 4.出力設定
GPIO.setup(LED, GPIO.OUT)

# 5.点滅/点灯を3回繰り返す
for i in range(3):

    print 'Count=' + str(i)

    # ハイレベルを出力し、5秒待機
    GPIO.output(LED, GPIO.HIGH)
    print 'LED High'
    time.sleep(5)

    # ローレベルを出力し、5秒待機
    GPIO.output(LED, GPIO.LOW)
    print 'LED Low'
    time.sleep(5)

# 6.GPIOの解放
GPIO.cleanup()