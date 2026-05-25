# monitoring-infra
ラズパイで温湿度を測定し、Grafanaでリッチに可視化する監視基盤

## 概要
このプロジェクトでは、Raspberry Pi 4Bに接続したDHT11から温度・湿度を取得し、将来的にPrometheusやGrafanaと連携して可視化することを目指します。

## 使用機材

### ハードウェア
| ハードウェア | 用途 |
| --- | --- |
| Raspberry Pi 4 Model B 8GB | センサー読み取り・スクリプト実行 |
| DHT11 | 温湿度計測 |

### ソフトウェア
| ソフトウェア / ライブラリ | 用途 |
| --- | --- |
| Python 3 | センサー読み取りスクリプト |
| adafruit-circuitpython-dht | DHT11制御 |

## 環境構築

### いつもの
```sh
sudo apt update && sudo apt upgrade -y
```

### 必要なパッケージのインストール
```sh
sudo apt install -y python3 python3-venv python3-pip git
```

### リポジトリのクローン
```sh
git clone https://github.com/sumyka/monitoring-infra.git
cd monitoring-infra
```

### 仮想環境
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 必要ライブラリのインストール
```sh
pip install --upgrade pip
pip install adafruit-circuitpython-dht
```

## 実行方法
```sh
python3 read_dht11.py
```
