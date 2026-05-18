# ThumbyColor 学習テーマリスト

## Phase 1: 基本（初級）

テンプレートを拡張しながら、ゲームの土台となる機能を習得する。

- [ ] **1. ゲームループと時間** — `engine` — `tick()`, `start()`, `fps_limit()`, `dt` の使い方
- [ ] **2. 直接描画（図形・色）** — `engine_draw` — 矩形・円・直線・ピクセル・`Color` 定数
- [ ] **3. テキスト描画** — `engine_draw` + `engine_resources` — フォントロード、`text()` でテキスト表示
- [ ] **4. ボタン入力** — `engine_io` — `is_pressed` / `is_just_pressed` / `is_just_released`
- [ ] **5. 位置と移動** — `engine_math` — `Vector2` / `Vector3` で座標管理、dt を使った移動
- [ ] **6. ノードと継承** — `engine_nodes` — `Sprite2DNode` 継承、`tick()` コールバック、`CameraNode`
- [ ] **7. 親子関係** — `engine_nodes` — `add_child()` で親子ノード構築

**ゴール**: ボタンで動くキャラクター（矩形 or テキスト）を画面に表示できる

---

## Phase 2: 発展（中級）

素材を扱い、ゲームらしい表現を追加する。

- [ ] **8. 画像スプライト** — `engine_resources` + `engine_nodes` — `TextureResource`、`Sprite2DNode` にテクスチャ設定
- [ ] **9. アニメーション** — `engine_animation` — `Tween` でプロパティ補間、`ONE_SHOT` / `LOOP` / `PING_PONG`
- [ ] **10. サウンド** — `engine_audio` + `engine_resources` — `ToneSoundResource` / `RTTTLSoundResource`、`play()`
- [ ] **11. セーブ・ロード** — `engine_save` — スコアや状態の永続化
- [ ] **12. バイブレーション** — `engine_io` — `rumble()` でフィードバック

**ゴール**: 画像スプライト・音・アニメーションを使った簡単なミニゲームが作れる

---

## Phase 3: 応用（中上級）

物理演算とデバッグで本格的なアクションゲームへ。

- [ ] **13. 物理演算（基本）** — `engine_physics` — `set_gravity()`、`PhysicsRectangle2DNode` の基本
- [ ] **14. 衝突検知** — `engine_physics` — `collision()` コールバック、動的/静的オブジェクト
- [ ] **15. デバッグ技法** — `engine_debug` — 出力制御、パフォーマンス計測

**ゴール**: 重力・衝突を使ったプラットフォーマーの基礎が作れる

---

## Phase 4: 特殊機能（必要に応じて）

- [ ] **16. デバイス間通信** — `engine_link` — 2台のThumby Color間でデータ送受信
- [ ] **17. 日時・RTC** — `engine_time` — 現在日時の取得、タイムトラッキング
