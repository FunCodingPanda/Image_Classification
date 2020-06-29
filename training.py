import os

MUSHROOMS_FOLDER = '/Users/sophie/Desktop/test_image'
VALIDATION_PERCENT = 0.15
TEST_PERCENT = 0.15
TRAIN_PERCENT = 0.7

# all the mushrooms are already speerated into the poisonous and non poisonous folders 
# all the folders are already created such as Training, Validation and Test 
# each of the folders on line 9 also have a poisonous and non poisonous folder 
def create_train_test_validation_mapping():
    poisonous_folder = os.path.join(MUSHROOMS_FOLDER, 'poisonous')
    non_poisonous_folder = os.path.join(MUSHROOMS_FOLDER, 'non_poisonous')
    poisonous_files = []
    non_poisonous_files = []

    for filename in os.listdir(poisonous_folder):
        poisonous_files.append(os.path.join(poisonous_folder, filename))
    for filename in os.listdir(non_poisonous_folder):
        non_poisonous_files.append(
            os.path.join(non_poisonous_folder, filename))

    num_poisonous = len(poisonous_files)
    num_non_poisonous = len(non_poisonous_files)

    num_validation_poisonous = round(num_poisonous * VALIDATION_PERCENT)
    num_validation_non_poisonous = round(num_non_poisonous * VALIDATION_PERCENT)
    num_test_poisonous = round(num_poisonous * TEST_PERCENT)
    num_test_non_poisonous = round(num_non_poisonous * TEST_PERCENT)

    for filename in poisonous_files[:num_validation_poisonous]:
        basename = os.path.basename(filename)
        new_filename = os.path.join(
            MUSHROOMS_FOLDER, 'Validation/poisonous', basename)
        os.rename(filename, new_filename)
    poisonous_files = poisonous_files[num_validation_poisonous:]

    for filename in non_poisonous_files[:num_validation_non_poisonous]:
        basename = os.path.basename(filename)
        new_filename = os.path.join(
            MUSHROOMS_FOLDER, 'Validation/non_poisonous', basename)
        os.rename(filename, new_filename)
    non_poisonous_files = non_poisonous_files[num_validation_non_poisonous:]

    for filename in poisonous_files[:num_test_poisonous]:
        basename = os.path.basename(filename)
        new_filename = os.path.join(
            MUSHROOMS_FOLDER, 'Test/poisonous', basename)
        os.rename(filename, new_filename)
    poisonous_files = poisonous_files[num_test_poisonous:]

    for filename in non_poisonous_files[:num_test_non_poisonous]:
        basename = os.path.basename(filename)
        new_filename = os.path.join(
            MUSHROOMS_FOLDER, 'Test/non_poisonous', basename)
        os.rename(filename, new_filename)
    non_poisonous_files = non_poisonous_files[num_test_non_poisonous:]

    for filename in poisonous_files:
        basename = os.path.basename(filename)
        new_filename = os.path.join(
            MUSHROOMS_FOLDER, 'Training/poisonous', basename)
        os.rename(filename, new_filename)

    for filename in non_poisonous_files:
        basename = os.path.basename(filename)
        new_filename = os.path.join(
            MUSHROOMS_FOLDER, 'Training/non_poisonous', basename)
        os.rename(filename, new_filename)


create_train_test_validation_mapping()
