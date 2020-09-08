import pandas as pd
import os.path
from os import path
from typing import Dict, List

class DfUtils():
    """Toolbox for pandas Dataframe
    """

    def __init__(self, dataf: pd.DataFrame):
        self.dataf = dataf

    def get_colum(self) -> List:
        """Return columns label of the dataframe

        Returns:
            List: array of columns label
        """

        return self.dataf.columns.values

    def dict_to_df(self, ddata: Dict) -> pd.DataFrame:
        """Create dataframe with a dictionnary

        Args:
            ddata (Dict): simple dictionnary

        Returns:
            pd.DataFrame: Dataframe with dict data
        """

        self.dataf = pd.DataFrame(ddata)
        return self.dataf

    def column_to_list(self, n: int) -> List:
        """Generate list from a dataframe colum

        Args:
            n (int): position of column dataframe

        Returns:
            List: Array of element in column dataframe
        """

        return self.dataf.iloc[:, n].values.tolist()

    def df_to_xlsx(self, outputfile: str) -> None:
        """Save dataframe to xlsx

        Args:
            outputfile (str): xlsx path file
        """

        # absolute directory path
        dirpath = path.dirname(outputfile)

        if not path.exists(dirpath):
            # create path
            os.makedirs(dirpath)

        self.dataf.to_excel(outputfile, index=False, header=True)
