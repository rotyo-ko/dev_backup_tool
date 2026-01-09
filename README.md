## 使い方

この `backup.py` は、複数のプロジェクトをまとめて管理している
フォルダに置いて使います。

```
Dev/
├─ project_a/
├─ project_b/
└─ backup.py
```

このように配置すれば、`Dev`ディレクトリの1階層上に`Back_up_Django`が作成され、日付のディレクトリに`project_a`, `project_b`がバックアップされます。

仮想環境ディレクトリは `venv` として除外しています。

## 実行方法
```bash
python backup.py
```
