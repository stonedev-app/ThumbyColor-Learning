# Test

## ゲーム概要
学習用のテストプロジェクト

## デバイス上のパス
/Games/Test/

## ファイル構成
テンプレートそのまま

## 実装メモ
学習用にAPIドキュメントの内容を試してみる

## コマンド
- `/review` — コードレビューを手動実行

## よく使うスニペット

### engine_io — ボタン入力

```python
from engine_io import btn

# tick(self, dt) の中で使う
if btn.LEFT.is_pressed:        # 押し続けている間ずっと
    self.position.x -= speed * dt
if btn.A.is_just_pressed:      # 押した瞬間だけ（1フレーム）
    pass
if btn.A.is_just_released:     # 離した瞬間だけ
    pass
```

### engine_draw — 直接描画

```python
import engine_draw
from engine_draw import Color

engine_draw.clear(engine_draw.black)                            # 画面全体を塗りつぶす
engine_draw.rect(Color(255, 0, 0), 10, 10, 40, 20, False, 1.0) # 塗りつぶし矩形
engine_draw.rect(Color(255, 0, 0), 10, 10, 40, 20, True, 1.0)  # 枠線のみ
engine_draw.circle(engine_draw.white, 64, 64, 20, False, 1.0)  # 塗りつぶし円
engine_draw.line(engine_draw.yellow, 0, 0, 127, 127, 1.0)      # 直線
# text(font, text, color, x, y, letter_spacing, line_height, opacity)
engine_draw.text(font, "HELLO", engine_draw.white, 4, 4, 0, 0, 1.0)
```

### engine_nodes — Sprite2DNode / CameraNode

```python
from engine_nodes import Sprite2DNode, CameraNode
from engine_resources import TextureResource
from engine_math import Vector2, Vector3

class Player(Sprite2DNode):
    def __init__(self):
        super().__init__(self)
        self.texture = TextureResource("/Games/Test/img.bmp")
        self.position = Vector2(0, 0)

    def tick(self, dt):
        pass  # 毎フレーム呼ばれる

camera = CameraNode()
camera.position = Vector3(0, 0, 1)  # z=1 が標準

# 親子関係
parent.add_child(child)  # child は parent の座標系に従う
```

## 学習メモ

<!-- 試した内容・ハマりポイント・気づきをここに記録していく -->

