import math

#SIZE_HEIGHT = 28
#SIZE_WIDTH = 28

class Digit_Classifier(object):

    def __init__(self):
        self.size_height = 28
        self.size_width = 28
        self.training_size = 500
        self.testing_size = 100
        self.count = 0

    def features(self, data):
        """
        returns whether pixel features are foreground or background
        """
        a = self.get_pixels()

        features = self.count()
        for i in range(self.size_width):
            for j in range(self.size_height):
                if self.get_pixel(i, j) > 0:
                    features = [(i, j)] = 1
                else:
                    features = [(i, j)] = 0
        return features

    def train(self, train_images, train_labels):
        open_train_images = open(train_images, 'r')
        open_train_labels = open(train_labels, 'r')
        counter = 0
        for k in range(0.1, 10.0, 0.1):
            for i in open_train_labels:
                counter += 1
                data_labels = data_labels.rstrip('\n')
                sample = []
                for row in range(self.size_width):
                    line = open_train_images.readline()


    def test(self, test_images, test_labels):
        open_test_images = open(test_images, 'r')
        open_test_labels = open(test_labels, 'r')

    def get_pixel(self, column, row):
        return self.pixels[column][row]

    def get_pixels(self):
        return self.pixels