## import 항목
from threading import Thread

## 생성자
Thread(target="Target function want to call", name="Thread name", args=("Parameter","Want","To Use"))

## daemon 설정 (Background thread)
Thread.daemon=True

## Thread start
Thread.start()

## Wait for Thread end
Thread.join()