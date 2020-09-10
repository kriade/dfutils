import pandas as pd
import os.path
from os import path
from typing import Dict, List
from pathlib import Path

class DfUtils():
    """Toolbox for pandas Dataframe
    """

    def __init__(self, dataf: pd.DataFrame):
        self.dataf = dataf

    def get_colum(self) -> List:
        """Return columns label of the data drame

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

    def df_to_file(self, outputfile: str) -> None:
        """Save dataframe to csv or xlsx file

        Args:
            outputfile (str): csv path file
        """
        ext_outpufile = Path(outputfile).suffix

        if ext_outpufile == ".csv":
            self.__create_directory(outputfile)
            self.dataf.to_csv(outputfile, index=False, header=True)
        if ext_outpufile == ".xlsx":
            self.__create_directory(outputfile)
            self.dataf.to_excel(outputfile, index=False, header=True)

    def __create_directory(self, pathfile: str) -> None:
        """Private method to create directory if not exist

        Args:
            pathfile (str): path directory with filename include
        """
        # absolute directory path
        dirpath = path.dirname(pathfile)
        # create path
        if not path.exists(dirpath):
            os.makedirs(dirpath)
