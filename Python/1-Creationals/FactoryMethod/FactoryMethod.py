#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Feature(ABC):
    """
    Base class of the objects that have to be created using the factory method
    """
    def __init__(self):
        pass

    @abstractmethod
    def specifications(self):
        """
        Method used to customise the functionality of a particular item
        :return: None
        """
        pass


class DisplayFeatures(Feature):
    def specifications(self):
        print("5.5 inch, 1280 x 720 Pixels, TFT LCD IPS")


class ProcessorFeatures(Feature):
    def specifications(self):
        print("MediaTek MTK6737 1.3GHz, Quad Core, 1.3 GHz")


class StorageFeatures(Feature):
    def specifications(self):
        print("Internal Storage 32GB, RAM 3GB")


class CallFeatures(Feature):
    def specifications(self):
        print("Voice Call, Phonebook")


class Gadgets(ABC):
    """
    Base class of items that will contain one or more Features
    """
    def __init__(self):
        self.features = []
        self.feature_list()

    @abstractmethod
    def feature_list(self):
        """
        It will build the list of feature for a specific item
        :return: None
        """
        pass

    def get_features(self):
        return self.features

    def add_features(self, feature):
        self.features.append(feature)


class Mobile(Gadgets):
    def feature_list(self):
        """
        It builds the feature list for a Mobile device
        :return: None
        """
        self.add_features(DisplayFeatures())
        self.add_features(ProcessorFeatures())
        self.add_features(CallFeatures())
        self.add_features(StorageFeatures())


class Tablet(Gadgets):
    """
    It builds the feature list for a Tablet device
    :return: None
    """

    def feature_list(self):
        self.add_features(DisplayFeatures())
        self.add_features(StorageFeatures())
        self.add_features(ProcessorFeatures())


def main():
    print("##### MOBILE FEATURE LIST #####")
    gadget1 = Mobile()
    for x in gadget1.get_features():
        x.specifications()

    print('\n')
    print("##### TABLET FEATURE LIST #####")
    gadget2 = Tablet()
    for y in gadget2.get_features():
        y.specifications()


if __name__ == "__main__":
    main()


"""
Output:

##### MOBILE FEATURE LIST #####
5.5 inch, 1280 x 720 Pixels, TFT LCD IPS
MediaTek MTK6737 1.3GHz, Quad Core, 1.3 GHz
Voice Call, Phonebook
Internal Storage 32GB, RAM 3GB


##### TABLET FEATURE LIST #####
5.5 inch, 1280 x 720 Pixels, TFT LCD IPS
Internal Storage 32GB, RAM 3GB
MediaTek MTK6737 1.3GHz, Quad Core, 1.3 GHz

"""