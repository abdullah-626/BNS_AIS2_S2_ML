def train_model(model_name , *datasets , **hyperparameters):
    print(f"training model: {model_name}")

    print("\ndatasets")
    for dataset in datasets :
        print("-",dataset)
    print("\nhyperparameters")
    for key,value in hyperparameters.items():
        print(f"{key} : {value}")

train_model(

    "fraud determination",
    "train.csv",
    "validation.csv",
    "test.csv",
    learning_rate = 100
)
