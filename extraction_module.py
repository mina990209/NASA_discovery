import pandas as pd
import numpy as np

main(filepath):
    test = pd.read_csv(filepath)
    newtest = test.set_index("rows")
