import numpy as np
from tensorflow.keras.models import Sequential, load_model # type: ignore
from tensorflow.keras.layers import Conv2D, Flatten, Dense, LeakyReLU, BatchNormalization, Input, Reshape, LayerNormalization, Activation # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping # type: ignore

def load_data():
    puzzles = np.zeros((1000000, 81), np.int32)
    solutions = np.zeros((1000000, 81), np.int32)
    for i, line in enumerate(open('product/sudoku.csv', 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            puzzles[i, j] = q
            solutions[i, j] = s
    puzzles = puzzles / 9.0  # Normalize the input data
    solutions -=1
    # makes the solution values between 0-8 as this works best for the loss function

    # data is better normalised (valued between 1 and 0) as this helps to keep the optimization process more simplified and faster as well as reducing the chances of overfitting. also some activation functions require values in a specific range to improve effectiveness

    puzzles = puzzles.reshape(1000000, 9, 9, 1)  # Reshape to (num_samples, 9, 9, 1)
    solutions = solutions.reshape(1000000, 9, 9)  # Flatten the solutions to (num_samples, 81)

    # reshaping the numpy arrays are important as the data needs to be formatted as a 4 dimensional tensor, which will allow for the convolutional layers to perform filtering and pooling more effectively. also helps to fit the expected input of the CNN, only 1 channel as I am not working with RGB images which would require 3 chanels for each RGB value.

    return puzzles, solutions

def train_model():
    puzzles, solutions = load_data()

    model = Sequential([
        Input(shape=(9, 9, 1)), # takes in a 9x9 grid with only 1 channel
        Conv2D(162, (5, 5), padding='same'),
        LeakyReLU(negative_slope=0.1),
        BatchNormalization(),
        Conv2D(162, (5, 5), padding='same'),
        LeakyReLU(negative_slope=0.1),
        BatchNormalization(),
        Conv2D(162, (5, 5), padding='same'),
        LeakyReLU(negative_slope=0.1),
        BatchNormalization(),
        Conv2D(162, (5, 5), padding='same'),
        LeakyReLU(negative_slope=0.1),
        BatchNormalization(),
        Conv2D(162, (5, 5), padding='same'),
        LeakyReLU(negative_slope=0.1),
        # leaky relu activation in order to simplify learning by removing negative values to help focus on learning patterns
        # padding for controlling the size of feature maps, keeps the output size the same as the input
        Flatten(),
        Dense((9*9)*9),
        # denses the neurons output into 81 (no of cells in solution) 
        # ranges of values between 1-9 (constraint of the solution that 
        # cells are between 1 and 9)
        LayerNormalization(axis=-1),
        # normalisation to stabalise and reduce overfitting
        Reshape((9,9,9)),
        # reshapes the condensed layer into a set of 9 columns, 9 rows 
        # and an array sized 9 for each cell for the column and rows
        Activation('softmax')
        # this ensures that all output probability is normalised so that 
        # all probabilities add up to 1, so that it is perfect for 
        # classification
    ])

    model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # the job of the optimizer is to adjust the weights and biases of the network to minimise the loss function adn improve the models performance
    # loss measures how the models predictions match up to the target values, this is needed for the optimiser as this provides feedback that is used to adjust the weights and biases more effectively. 
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, min_lr=1e-6, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, verbose=1, restore_best_weights=True)
    # callbacks to try and reduce the probability of the CNN losing accuracy

    model.fit(puzzles, solutions, epochs=10, batch_size=32, validation_split=0.2, callbacks=[reduce_lr, early_stopping])
    # epochs are the no of times the network trains on the training data
    # batch size is the no of sudokus the model trains with at a time
    # Save the model
    model.save('product/sudoku_model.keras')
    return model

def solve_sudoku(puzzle):
    puzzle = np.array(puzzle) / 9.0  # Normalize the input puzzle
    puzzle = puzzle.reshape(1, 9, 9, 1)  # Reshape to (1, 9, 9, 1)
    # Load the model once trained
    model = load_model('product/sudoku_model.keras')
    # training model if model is not yet optimised
    #model = train_model()
    #print(model.predict(puzzle))
    prediction = np.argmax(model.predict(puzzle), -1)+1
    # retrieves the highest number from a range of probabilities where 
    # index of the highest probability will most likely be the correct 
    # value for the cell in the 9x9 solution. does this for all 81 cells.
    # +1 for loss functions working better for values between 0-8, but 
    # sudoku needs values between 1-9
    return prediction.reshape(-1, prediction.shape[-1])
    #reshapes the 9x9 solution into a 2d array from being a 3d array

def calc_mistakes_made(grid):
    return row_mistakes(grid)+col_mistakes(grid)

def row_mistakes(grid):
    count=0
    for row in range(0,9):
        count+=grid[row].__len__() - set(grid[row]).__len__()
    return count

def col_mistakes(grid):
    count=0
    for col in range(0,9):
        column = np.array(grid)[:,col]
        count+=column.__len__()-set(column).__len__()
    return count