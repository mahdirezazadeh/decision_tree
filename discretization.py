import pandas as pd


def discrete_buying_maint(df, buying, maint):
    df[buying].replace({'vhigh': 3, 'high': 2, 'med': 1, 'low': 0}, inplace=True)
    df[maint].replace({'vhigh': 3, 'high': 2, 'med': 1, 'low': 0}, inplace=True)


def discrete_doors(df, doors):
    df[doors].replace({'5more': 3, '4': 2, '3': 1, '2': 0}, inplace=True)
    # df[doors].replace({'5more': 5}, inplace=True)


def discrete_persons(df, persons):
    df[persons].replace({'more': 2, '4': 1, '2': 0}, inplace=True)
    # df[persons].replace({'more': 5}, inplace=True)


def discrete_lug_boot(df, lug_boot):
    df[lug_boot].replace({'big': 2, 'med': 1, 'small': 0}, inplace=True)


def discrete_safety(df, safety):
    df[safety].replace({'high': 2, 'med': 1, 'low': 0}, inplace=True)


def discrete(source_file, dest_file, col_names):
    df = pd.read_csv(source_file, header=None, names=col_names)
    print(df.head())

    discrete_buying_maint(df, col_names[0], col_names[1])
    discrete_doors(df, col_names[2])
    discrete_persons(df, col_names[3])
    discrete_lug_boot(df, col_names[4])
    discrete_safety(df, col_names[5])
    print(df.head())
    df.to_csv(dest_file, header=False)

