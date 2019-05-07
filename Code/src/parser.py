import pandas as pd


class Parser():
    NAN_VALS =(pd.NaT, 'NA', '-', 'N/A', 'N\A','',' ')

    def __init__(self, fn):
        self._fn = fn
        self._set_df()
        self._df = self._untouched_df.copy()

    def _set_df(self):
        self._untouched_df = pd.read_csv(self._fn, sep=' ')

    def get_df(self):
        return self._df

    def clean_df(self):
        self._remove_nans()
        self._numerify()
        self._remove_corrupted()
        self._one_hotify()

    def _remove_nans(self):
        self._df.dropna(self.NAN_VALS, inplace=True)

    def _numerify(self):
        self._df = self._df[pd.to_numeric(self._df, errors='coerce')]

    def _remove_corrupted(self):
        pass

    def _one_hotify(self):
        pass
