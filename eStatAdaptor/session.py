import pandas as pd
from .utils import fetch_stats_data, json_to_dataframe

class Session:
    """
    統計データ取得のためのセッションを管理するクラス。
    """

    def __init__(self, api_key):
        """
        インスタンスを初期化し、APIキーを保存します。

        :param api_key: e-Stat APIのアプリケーションID
        """
        if not api_key:
            raise ValueError("APIキーは必須です。")
        self.api_key = api_key

    def getData(self, stats_data_id):
        """
        統計データIDを使用してデータを取得します。

        :param stats_data_id: 統計表表示ID
        :return: Pandas DataFrame形式のデータ
        """
        if not stats_data_id:
            raise ValueError("統計データIDは必須です。")

        # APIを呼び出してJSONデータを取得
        try:
            json_data = fetch_stats_data(self.api_key, stats_data_id)
        except RuntimeError as e:
            raise RuntimeError(f"データ取得中にエラーが発生しました: {e}")

        # JSONデータをDataFrameに変換
        try:
            df = json_to_dataframe(json_data)
            return df
        except ValueError as e:
            raise ValueError(f"データフレーム変換中にエラーが発生しました: {e}")


