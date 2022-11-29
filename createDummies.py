def createDummies(df, var_name):
    dummy = pd.get_dummies(df[var_name], prefix=var_name)
    df = data.drop(var_name, axis=1)
    df = pd.concat([df, dummy], axis=1)

    return df