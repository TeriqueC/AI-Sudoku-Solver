import numpy as np
from tensorflow.keras.models import Sequential, load_model # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, Input # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping # type: ignore
from tensorflow.keras.losses import MeanSquaredError # type: ignore

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
    solutions = solutions / 9.0  # Normalize the output data

    # data is better normalised (valued between 1 and 0) as this helps to keep the optimization process more simplified and faster as well as reducing the chances of overfitting. also some activation functions require values in a specific range to improve effectiveness

    puzzles = puzzles.reshape(1000000, 9, 9, 1)  # Reshape to (num_samples, 9, 9, 1)
    solutions = solutions.reshape(1000000, 81)  # Flatten the solutions to (num_samples, 81)

    # reshaping the numpy arrays are important as the data needs to be formatted as a 4 dimensional tensor, which will allow for the convolutional layers to perform filtering and pooling more effectively. also helps to fit the expected input of the CNN, only 1 channel as I am not working with RGB images which would require 3 chanels for each RGB value.

    return puzzles, solutions

def train_model():
    puzzles, solutions = load_data()

    model = Sequential([
        Input(shape=(9, 9, 1)), # takes in a 9x9 grid with only 1 channel
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.4),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.4),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.4),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Dropout(0.4),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(81, activation='linear')  # Output layer with 81 neurons
    ])

    # Conv2D is used to extract features, makes use of filters called kernels to produce feature maps, which aids in pattern recognition in the network. the use of filters allows for parameter sharing which means less parameters are needed for the network to generalise better as filters cover multiple parts of the input. currently uses varied filter sizes and kernel sizes 3x3.

    # BatchNormalisation aims to standardise the inputs so that the process of training becomes more stable and efficient. this allows for a higher rate of learning and quicker training processes, it also helps to prevent overfitting by adding on a bit on "noise" to the input of each layer. does this through working out the mean and variations of the inputs, then normalises based on the results.

    # MaxPooling2D works by reducing spacial dimensions of the input data in order to reduce complexity and memory consumption in computations. it does this by keeping the maximum value from the pooling window, which helps to highlight prominent features, which improves generalisation and reduce overfitting.

    # Dropout hopes to achieve a reduction in overfitting by randomly dropping out neurons (resetting to 0) so that the network is forced to learn redundant representations of the data, also allowing for better generalisation by preventing network from being too specialised to the training data. dropout can aid in reducting co-adaptation which is where neurons depend on other specific neurons, this means single neurons can learn more robust features independently. 

    # Flatten layer converts the multidimestional data into a singular dimension which is what is needed as input for the dense layers of the CNN so that they can process and learn from the test data.

    # Dense layers are fully connected layers as each neuron in this layer is connected to every neuron in the previous layer, so every input now has an impact of every output, which gives the model the ability to learn the patterns and complex relations of the training data.

    model.compile(optimizer=Adam(learning_rate=0.0001), loss=MeanSquaredError(), metrics=['accuracy'])
    # the job of the optimizer is to adjust the weights and biases of the network to minimise the loss function adn improve the models performance
    # loss measures how the models predictions match up to the target values, this is needed for the optimiser as this provides feedback that is used to adjust the weights and biases more effectively. 
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, min_lr=1e-6, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, verbose=1, restore_best_weights=True)
    # callbacks to try and reduce the probability of the CNN losing accuracy

    model.fit(puzzles, solutions, epochs=50, batch_size=128, validation_split=0.2, callbacks=[reduce_lr, early_stopping])
    # epochs are the no of times the network trains on the training data
    # batch size is the no of sudokus the model trains with at a time
    # Save the model
    model.save('product/sudoku_model.h5')
    return model

def solve_sudoku(puzzle):
    puzzle = puzzle / 9.0  # Normalize the input puzzle
    puzzle = puzzle.reshape(1, 9, 9, 1)  # Reshape to (1, 9, 9, 1)
    # Load the model once trained
    model = load_model('product/sudoku_model.h5')
    # training model if model is not yet optimised
    #model = train_model()
    prediction = model.predict(puzzle)
    prediction = np.round((prediction.reshape(9, 9) * 9).astype(int))  # Reshape and denormalize the output
    return prediction

new_puzzle = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                       [6, 0, 0, 1, 9, 5, 0, 0, 0],
                       [0, 9, 8, 0, 0, 0, 0, 6, 0],
                       [8, 0, 0, 0, 6, 0, 0, 0, 3],
                       [4, 0, 0, 8, 0, 3, 0, 0, 1],
                       [7, 0, 0, 0, 2, 0, 0, 0, 6],
                       [0, 6, 0, 0, 0, 0, 2, 8, 0],
                       [0, 0, 0, 4, 1, 9, 0, 0, 5],
                       [0, 0, 0, 0, 8, 0, 0, 7, 9]])

solved_puzzle = solve_sudoku(new_puzzle)
print(solved_puzzle)
#Sudoku.print_grid(solved_puzzle)