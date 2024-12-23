from setuptools import setup, find_packages

setup(
    name="eStatAdaptor",  # ライブラリ名
    version="0.1.0",      # バージョン番号
    description="eStartのapiで取得可能なデータをpandas-dataframeとして読み取るためのライブラリ。利用にはeStartで払い出されるAPIキーが必要です。",  # 簡単な説明
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zaiwa-linus/e-stat-adaptor.git",  # GitHubリポジトリURL
    packages=find_packages(),  # パッケージ自動検出
    install_requires=[         # 必要な依存ライブラリ
        "pandas",
        "requests"
    ],
    classifiers=[              # メタデータ
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",   # 必要なPythonのバージョン
)