from __future__ import annotations

from tensorflow.keras.layers import (
    Activation,
    AveragePooling1D,
    BatchNormalization,
    Conv1D,
    Dense,
    Dropout,
    GlobalAveragePooling1D,
    Input,
    SpatialDropout1D,
)
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


def compile_classification_model(model: Model, learning_rate: float, decay: float = 1e-5) -> Model:
    model.compile(
        loss="categorical_crossentropy",
        optimizer=Adam(learning_rate=learning_rate, decay=decay),
        metrics=["accuracy"],
    )
    return model


def build_deap_baseline_model(input_shape: tuple[int, int], classes: int = 2) -> Model:
    x_input = Input(input_shape, name="Input")
    x = Conv1D(32, kernel_size=2, strides=1, padding="valid", activation="relu", name="C1")(x_input)
    x = AveragePooling1D(pool_size=2, name="AP1")(x)
    x = BatchNormalization(name="BN1")(x)

    x = Conv1D(64, kernel_size=2, strides=1, padding="valid", activation="relu", name="C2")(x)
    x = AveragePooling1D(pool_size=2, name="AP2")(x)
    x = BatchNormalization(name="BN2")(x)

    x = Conv1D(128, kernel_size=2, strides=1, padding="valid", activation="relu", name="C3")(x)
    x = GlobalAveragePooling1D(name="GAP")(x)
    x = BatchNormalization(name="BN3")(x)

    x = Dropout(0.2, name="D1")(x)
    x = Dense(256, activation="relu", name="FC1")(x)
    x = Dense(32, activation="relu", name="FC2")(x)
    x = Dropout(0.1, name="D2")(x)
    x = Dense(classes, name="Output")(x)
    output = Activation("softmax", name="Softmax")(x)
    return Model(inputs=x_input, outputs=output, name="CompactNet")


def build_deap_selected_model(input_shape: tuple[int, int], classes: int = 2) -> Model:
    x_input = Input(input_shape, name="Input")
    x = Conv1D(32, kernel_size=2, strides=1, padding="same", activation="relu", name="C1")(x_input)
    x = AveragePooling1D(pool_size=2, name="AP1")(x)
    x = BatchNormalization(name="BN1")(x)

    x = Conv1D(128, kernel_size=5, strides=1, padding="same", activation="relu", name="C2")(x)
    x = AveragePooling1D(pool_size=2, name="AP2")(x)
    x = BatchNormalization(name="BN2")(x)

    x = Conv1D(192, kernel_size=3, strides=2, padding="same", activation="relu", name="C3")(x)
    x = GlobalAveragePooling1D(name="GAP")(x)
    x = BatchNormalization(name="BN3")(x)

    x = Dropout(0.2, name="D1")(x)
    x = Dense(64, activation="tanh", name="FC1")(x)
    x = Dense(8, activation="tanh", name="FC2")(x)
    x = Dropout(0.1, name="D2")(x)
    x = Dense(classes, name="Output")(x)
    output = Activation("softmax", name="Softmax")(x)
    return Model(inputs=x_input, outputs=output, name="CompactNet")


def build_seed_model(input_shape: tuple[int, int] = (310, 1), classes: int = 3) -> Model:
    return build_deap_selected_model(input_shape=input_shape, classes=classes)


def build_deap_optuna_model(trial, input_shape: tuple[int, int], classes: int = 2) -> Model:
    x_input = Input(shape=input_shape, name="Input")

    x = Conv1D(
        filters=trial.suggest_categorical("filters", [32, 64, 128]),
        kernel_size=trial.suggest_categorical("kernel_size", [1, 2]),
        strides=trial.suggest_categorical("strides", [1, 2]),
        padding="same",
        activation="relu",
        name="C1",
    )(x_input)
    x = AveragePooling1D(pool_size=2, name="AP1")(x)
    x = BatchNormalization(name="BN1")(x)

    x = Conv1D(64, kernel_size=5, strides=2, padding="valid", activation="relu", name="C2")(x)
    x = AveragePooling1D(pool_size=2, name="AP2")(x)
    x = BatchNormalization(name="BN2")(x)

    x = Conv1D(128, kernel_size=3, strides=1, padding="valid", activation="relu", name="C3")(x)
    x = GlobalAveragePooling1D(name="GAP")(x)
    x = BatchNormalization(name="BN3")(x)

    x = Dropout(0.2, name="D1")(x)
    x = Dense(
        units=trial.suggest_categorical("units", [64, 128, 256]),
        activation=trial.suggest_categorical("activation", ["relu", "linear", "tanh"]),
        name="FC1",
    )(x)
    x = Dense(8, name="FC2")(x)
    x = Activation("tanh", name="FC2Activation")(x)
    x = Dropout(0.1, name="D2")(x)
    x = Dense(classes, name="Output")(x)
    output = Activation("softmax", name="Softmax")(x)
    return Model(inputs=x_input, outputs=output, name="CompactNet")

