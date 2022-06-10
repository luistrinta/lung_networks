# This is a sample Python script.
import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def similarity_matrix(filename):
    df = pd.read_csv(filename, sep="\t")
    df


similarity_matrix("LUNG_Gene_Expression.txt")
