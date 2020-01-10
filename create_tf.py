"""
Usage:

# Create train data:
python create_tf.py --csv_input=train_is.csv  --output_path=train_is.record

# Create test data:
python create_tf.py --csv_input=validation_is2.csv  --output_path=val_is2.record 
"""

import pandas as pd
import os
import io
import tensorflow as tf
import sys
from create_pb import class_text_to_int, class_text_to_int2, class_text_to_int3
from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict
import matplotlib.pyplot as plt
import matplotlib.patches as patches

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
flags.DEFINE_string('label', '', 'Name of class label')

flags.DEFINE_string('img_path', '', 'Path to images')
FLAGS = flags.FLAGS


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    # check if the image format is matching with your images.
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int3(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    path = os.path.join(train_path, FLAGS.img_path)
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))

def show_sample(image_id):
    df = pd.read_csv('validation_is2.csv')
    image_list = sorted(list(set(df['filename'].tolist())))
    frame_df = df[df['filename'] == image_list[image_id]]
    
    image = Image.open(dataset + '/' + image_list[image_id])
    f, ax = plt.subplots(figsize=(7, 7))
    
    for index, row in frame_df.iterrows():
        w = row['xmax'] - row['xmin']
        h = row['ymax'] - row['ymin']
        print(w, h)
        rect = patches.Rectangle((row['xmin'], row['ymin']), w, h, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
    
    ax.imshow(image)
    ax.set_title(set(list(frame_df['class'])) , fontsize=20)
    # plt.axis('off')
    plt.show()


if __name__ == '__main__':
    
    dataset = 'validation'
    # train_path = '/lustre/fs0/groups/course.cap6614/Data/OpenImages2019_ONLYVisualRelationship/' + dataset +'/'
    train_path = dataset + '/'
    show_sample(20)

    # tf.app.run()
    '''
    ################################### Test 1 non-is ############################################
    df = pd.read_csv('challenge-2019-'+ dataset +'-vrd.csv')
    class_df = pd.read_csv('challenge-2019-classes-vrd.csv', names=['class_id1', 'Classes'])
    class_id = list(class_df.index)
    attr_df = pd.read_csv('challenge-2019-attributes-description.csv', names=['class_id2', 'Attributes'])
    is_df = df[df['RelationshipLabel'] != 'is']
    
    is_df = is_df.merge(class_df, left_on='LabelName1', right_on='class_id1')
    is_df = is_df.merge(class_df, left_on='LabelName2', right_on='class_id1')
    
    dim_df = pd.DataFrame(columns=['ImageID', 'width', 'height'])
    for image in is_df['ImageID']:
        image_name = image + '.jpg'
        if image_name in os.listdir(train_path):
            img = Image.open(train_path + image_name)
            width, height = img.size
            dim_df = dim_df.append({'ImageID': image, 'width': width, 'height': height}, ignore_index=True)

    is_df = is_df.merge(dim_df, left_on='ImageID', right_on='ImageID')
    is_df1 = is_df.filter(items=['ImageID', 'width', 'height', 'Classes_x', 'XMin1', 'XMax1', 'YMin1', 'YMax1'])
    is_df1 = is_df1.rename(columns={"ImageID":"filename", "Classes_x":"class", "XMin1": "xmin", "XMax1": "xmax", 
                                    "YMin1": "ymin", "YMax1": "ymax"})
    is_df2 = is_df.filter(items=['ImageID', 'width', 'height', 'Classes_y', 'XMin2', 'XMax2', 'YMin2', 'YMax2'])
    is_df2 = is_df2.rename(columns={"ImageID":"filename", "Classes_y":"class", "XMin2": "xmin", "XMax2": "xmax", 
                                    "YMin2": "ymin", "YMax2": "ymax"})
    
    result = is_df1.append(is_df2)
    result['filename'] = result['filename'].astype(str) + '.jpg'
    # result = result.sort_values(by=['filename'])
    
    result['xmin'] = (result['xmin'] * result['width']).astype(int)
    result['xmax'] = (result['xmax'] * result['width']).astype(int)
    result['ymin'] = (result['ymin'] * result['height']).astype(int)
    result['ymax'] = (result['ymax'] * result['height']).astype(int)
    
    # result.to_csv(dataset + '_nonis2.csv')
    '''
    '''
    ################################### Test 2 ############################################
    df = pd.read_csv('challenge-2019-'+ dataset +'-vrd.csv')
    class_df = pd.read_csv('challenge-2019-classes-vrd.csv', names=['class_id1', 'Classes'])
    class_id = list(class_df.index)
    attr_df = pd.read_csv('challenge-2019-attributes-description.csv', names=['class_id2', 'Attributes'])
    is_df = df[df['RelationshipLabel'] != 'is']
    
    is_df = is_df.merge(class_df, left_on='LabelName1', right_on='class_id1')
    is_df = is_df.merge(attr_df, left_on='LabelName2', right_on='class_id2')  # Change to attr_df and class_id1
    
    is_df['Classes'] = is_df['Classes'] + ' is ' + is_df['Attributes']
    
    print('Total Number of classes: ', len(is_df.Classes.unique()))
    print(is_df.Classes.unique())

    dim_df = pd.DataFrame(columns=['ImageID', 'width', 'height'])
    for image in is_df['ImageID']:
        image_name = image + '.jpg'
        if image_name in os.listdir(train_path):
            img = Image.open(train_path + image_name)
            width, height = img.size
            dim_df = dim_df.append({'ImageID': image, 'width': width, 'height': height}, ignore_index=True)

    is_df = is_df.merge(dim_df, left_on='ImageID', right_on='ImageID')
    is_df = is_df.filter(items=['ImageID', 'width', 'height', 'Classes', 'XMin1', 'XMax1', 'YMin1', 'YMax1'])
    result = is_df.rename(columns={"ImageID":"filename", "Classes":"class", "XMin1": "xmin", "XMax1": "xmax", 
                                    "YMin1": "ymin", "YMax1": "ymax"})

    result['filename'] = result['filename'].astype(str) + '.jpg'
    # result = result.sort_values(by=['filename'])
    
    result['xmin'] = (result['xmin'] * result['width']).astype(int)
    result['xmax'] = (result['xmax'] * result['width']).astype(int)
    result['ymin'] = (result['ymin'] * result['height']).astype(int)
    result['ymax'] = (result['ymax'] * result['height']).astype(int)
    
    # result.to_csv(dataset + '_is2.csv')
    '''
    '''
    ################################### Test 3 Relational nonis ############################################
    df = pd.read_csv('challenge-2019-'+ dataset +'-vrd.csv')
    class_df = pd.read_csv('challenge-2019-classes-vrd.csv', names=['class_id1', 'Classes'])
    class_id = list(class_df.index)
    attr_df = pd.read_csv('challenge-2019-attributes-description.csv', names=['class_id2', 'Attributes'])
    is_df = df[df['RelationshipLabel'] != 'is']
    
    is_df = is_df.merge(class_df, left_on='LabelName1', right_on='class_id1')
    is_df = is_df.merge(class_df, left_on='LabelName2', right_on='class_id1')

    dim_df = pd.DataFrame(columns=['ImageID', 'width', 'height'])
    for image in is_df['ImageID']:
        image_name = image + '.jpg'
        if image_name in os.listdir(train_path):
            img = Image.open(train_path + image_name)
            width, height = img.size
            dim_df = dim_df.append({'ImageID': image, 'width': width, 'height': height}, ignore_index=True)
    
    is_df = is_df.merge(dim_df, left_on='ImageID', right_on='ImageID')
    is_df['Classes'] = is_df['Classes_x'] + ' ' + is_df['RelationshipLabel'] + ' ' + is_df['Classes_y']
    print(len(is_df['Classes'].unique()))

    is_df['xmin'] = is_df[['XMin1', 'XMin2']].min(axis=1)
    is_df['ymin'] = is_df[['YMin1', 'YMin2']].min(axis=1)
    is_df['xmax'] = is_df[['XMax1', 'XMax2']].max(axis=1)
    is_df['ymax'] = is_df[['YMax1', 'YMax2']].max(axis=1)
    is_df = is_df.filter(items=['ImageID', 'width', 'height', 'Classes', 'xmin', 'xmax', 'ymin', 'ymax'])
    result = is_df.rename(columns={"ImageID":"filename", "Classes":"class"})
    
    result['filename'] = result['filename'].astype(str) + '.jpg'
    # # result = result.sort_values(by=['filename'])

    result['xmin'] = (result['xmin'] * result['width']).astype(int)
    result['xmax'] = (result['xmax'] * result['width']).astype(int)
    result['ymin'] = (result['ymin'] * result['height']).astype(int)
    result['ymax'] = (result['ymax'] * result['height']).astype(int)
    
    result.to_csv(dataset + '_nonis2.csv')
    
    '''