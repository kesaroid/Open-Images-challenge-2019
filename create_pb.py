from object_detection.protos.string_int_label_map_pb2 import StringIntLabelMap, StringIntLabelMapItem
from google.protobuf.json_format import MessageToDict
from google.protobuf import text_format
import pandas as pd


def convert_classes(classes, start=1):
    msg = StringIntLabelMap()
    for id, name in enumerate(classes, start=start):
        msg.item.append(StringIntLabelMapItem(id=id, name=name))

    text = str(text_format.MessageToBytes(msg, as_utf8=True), 'utf-8')
    return text


def class_text_to_int(row_label):
    if row_label == "Piano":
        return 1
    elif row_label == "Beer":
        return 2
    elif row_label == "Chopsticks":
        return 3
    elif row_label == "Cat":
        return 4
    elif row_label == "Motorcycle":
        return 5
    elif row_label == "Tennis racket":
        return 6
    elif row_label == "Football":
        return 7
    elif row_label == "Mobile phone":
        return 8
    elif row_label == "Flute":
        return 9
    elif row_label == "Tennis ball":
        return 10
    elif row_label == "Chair":
        return 11
    elif row_label == "Woman":
        return 12
    elif row_label == "Boy":
        return 13
    elif row_label == "Coffee table":
        return 14
    elif row_label == "Handbag":
        return 15
    elif row_label == "Fork":
        return 16
    elif row_label == "Girl":
        return 17
    elif row_label == "Coffee cup":
        return 18
    elif row_label == "Violin":
        return 19
    elif row_label == "Backpack":
        return 20
    elif row_label == "Knife":
        return 21
    elif row_label == "Snowboard":
        return 22
    elif row_label == "Rugby ball":
        return 23
    elif row_label == "Snake":
        return 24
    elif row_label == "Oven":
        return 25
    elif row_label == "Microwave oven":
        return 26
    elif row_label == "Man":
        return 27
    elif row_label == "Bench":
        return 28
    elif row_label == "Desk":
        return 29
    elif row_label == "Suitcase":
        return 30
    elif row_label == "Sofa bed":
        return 31
    elif row_label == "Horse":
        return 32
    elif row_label == "Microphone":
        return 33
    elif row_label == "Table tennis racket":
        return 34
    elif row_label == "Monkey":
        return 35
    elif row_label == "Surfboard":
        return 36
    elif row_label == "Table":
        return 37
    elif row_label == "Bottle":
        return 38
    elif row_label == "Mug":
        return 39
    elif row_label == "Wine glass":
        return 40
    elif row_label == "Drum":
        return 41
    elif row_label == "Dog":
        return 42
    elif row_label == "Guitar":
        return 43
    elif row_label == "Ski":
        return 44
    elif row_label == "Bed":
        return 45
    elif row_label == "Spoon":
        return 46
    elif row_label == "Briefcase":
        return 47
    elif row_label == "Hamster":
        return 48
    elif row_label == "Car":
        return 49
    elif row_label == "Bicycle":
        return 50
    elif row_label == "Camera":
        return 51
    elif row_label == "Dolphin":
        return 52
    elif row_label == "Taxi":
        return 53
    elif row_label == "Van":
        return 54
    elif row_label == "Elephant":
        return 55
    elif row_label == "Racket":
        return 56
    elif row_label == "Pretzel":
        return 57
    elif row_label == "Transparent":
        return 58
    elif row_label == "Plastic":
        return 59
    elif row_label == "(made of)Textile":
        return 60
    elif row_label == "(made of)Leather":
        return 61
    elif row_label == "Wooden":
        return 62
    else:
        None


def class_text_to_int2(row_label):
    if row_label == "Table is Wooden":
        return 1
    elif row_label == "Chair is Wooden":
        return 2
    elif row_label == "Coffee table is Wooden":
        return 3
    elif row_label == "Guitar is Wooden":
        return 4
    elif row_label == "Bed is Wooden":
        return 5
    elif row_label == "Chopsticks is Wooden":
        return 6
    elif row_label == "Desk is Wooden":
        return 7
    elif row_label == "Bench is Wooden":
        return 8
    elif row_label == "Violin is Wooden":
        return 9
    elif row_label == "Ski is Wooden":
        return 10
    elif row_label == "Piano is Wooden":
        return 11
    elif row_label == "Drum is Wooden":
        return 12
    elif row_label == "Mug is Wooden":
        return 13
    elif row_label == "Table is Plastic":
        return 14
    elif row_label == "Bottle is Plastic":
        return 15
    elif row_label == "Chair is Plastic":
        return 16
    elif row_label == "Coffee table is Plastic":
        return 17
    elif row_label == "Chopsticks is Plastic":
        return 18
    elif row_label == "Bench is Plastic":
        return 19
    elif row_label == "Piano is Plastic":
        return 20
    elif row_label == "Suitcase is Plastic":
        return 21
    elif row_label == "Coffee cup is Plastic":
        return 22
    elif row_label == "Spoon is Plastic":
        return 23
    elif row_label == "Fork is Plastic":
        return 24
    elif row_label == "Knife is Plastic":
        return 25
    elif row_label == "Mug is Plastic":
        return 26
    elif row_label == "Table is Transparent":
        return 27
    elif row_label == "Bottle is Transparent":
        return 28
    elif row_label == "Coffee table is Transparent":
        return 29
    elif row_label == "Coffee cup is Transparent":
        return 30
    elif row_label == "Mug is Transparent":
        return 31
    elif row_label == "Chair is (made of)Leather":
        return 32
    elif row_label == "Sofa bed is (made of)Leather":
        return 33
    elif row_label == "Backpack is (made of)Leather":
        return 34
    elif row_label == "Suitcase is (made of)Leather":
        return 35
    elif row_label == "Handbag is (made of)Leather":
        return 36
    elif row_label == "Briefcase is (made of)Leather":
        return 37
    elif row_label == "Sofa bed is (made of)Textile":
        return 38
    elif row_label == "Backpack is (made of)Textile":
        return 39
    elif row_label == "Suitcase is (made of)Textile":
        return 40
    elif row_label == "Handbag is (made of)Textile":
        return 41
    elif row_label == "Briefcase is (made of)Textile":
        return 42
    else:
        None


def class_text_to_int3(row_label):
    if row_label == "Chair at Desk":
        return 1
    elif row_label == "Man at Desk":
        return 2
    elif row_label == "Chair at Table":
        return 3
    elif row_label == "Man at Table":
        return 4
    elif row_label == "Man on Chair":
        return 5
    elif row_label == "Chair at Coffee table":
        return 6
    elif row_label == "Girl at Desk":
        return 7
    elif row_label == "Girl at Table":
        return 8
    elif row_label == "Girl on Chair":
        return 9
    elif row_label == "Woman at Desk":
        return 10
    elif row_label == "Woman at Table":
        return 11
    elif row_label == "Woman on Chair":
        return 12
    elif row_label == "Boy at Desk":
        return 13
    elif row_label == "Boy at Table":
        return 14
    elif row_label == "Boy on Chair":
        return 15
    elif row_label == "Woman at Coffee table":
        return 16
    elif row_label == "Man at Coffee table":
        return 17
    elif row_label == "Girl at Coffee table":
        return 18
    elif row_label == "Bottle on Desk":
        return 19
    elif row_label == "Bottle on Table":
        return 20
    elif row_label == "Coffee cup on Desk":
        return 21
    elif row_label == "Mug on Desk":
        return 22
    elif row_label == "Coffee cup on Table":
        return 23
    elif row_label == "Mug on Table":
        return 24
    elif row_label == "Coffee cup on Coffee table":
        return 25
    elif row_label == "Mug on Coffee table":
        return 26
    elif row_label == "Dog on Chair":
        return 27
    elif row_label == "Man interacts_with Dog":
        return 28
    elif row_label == "Dog under Desk":
        return 29
    elif row_label == "Dog under Table":
        return 30
    elif row_label == "Wine glass on Desk":
        return 31
    elif row_label == "Wine glass on Table":
        return 32
    elif row_label == "Man holds Microphone":
        return 33
    elif row_label == "Man holds Camera":
        return 34
    elif row_label == "Boy at Coffee table":
        return 35
    elif row_label == "Woman holds Microphone":
        return 36
    elif row_label == "Man holds Coffee cup":
        return 37
    elif row_label == "Man on Bench":
        return 38
    elif row_label == "Cat on Desk":
        return 39
    elif row_label == "Cat on Table":
        return 40
    elif row_label == "Man on Sofa bed":
        return 41
    elif row_label == "Man holds Table tennis racket":
        return 42
    elif row_label == "Woman holds Table tennis racket":
        return 43
    elif row_label == "Man holds Bottle":
        return 44
    elif row_label == "Woman on Bed":
        return 45
    elif row_label == "Woman interacts_with Dog":
        return 46
    elif row_label == "Woman holds Camera":
        return 47
    elif row_label == "Woman wears Handbag":
        return 48
    elif row_label == "Boy holds Guitar":
        return 49
    elif row_label == "Boy plays Guitar":
        return 50
    elif row_label == "Beer on Desk":
        return 51
    elif row_label == "Beer on Table":
        return 52
    elif row_label == "Dog on Desk":
        return 53
    elif row_label == "Dog on Table":
        return 54
    elif row_label == "Boy interacts_with Dog":
        return 55
    elif row_label == "Man holds Handbag":
        return 56
    elif row_label == "Cat under Chair":
        return 57
    elif row_label == "Woman holds Bottle":
        return 58
    elif row_label == "Cat on Chair":
        return 59
    elif row_label == "Fork on Table":
        return 60
    elif row_label == "Woman interacts_with Horse":
        return 61
    elif row_label == "Woman on Bench":
        return 62
    elif row_label == "Boy on Bicycle":
        return 63
    elif row_label == "Man holds Guitar":
        return 64
    elif row_label == "Man plays Guitar":
        return 65
    elif row_label == "Spoon on Table":
        return 66
    elif row_label == "Woman holds Guitar":
        return 67
    elif row_label == "Woman plays Guitar":
        return 68
    elif row_label == "Girl holds Coffee cup":
        return 69
    elif row_label == "Woman on Sofa bed":
        return 70
    elif row_label == "Girl wears Handbag":
        return 71
    elif row_label == "Man holds Beer":
        return 72
    elif row_label == "Man interacts_with Cat":
        return 73
    elif row_label == "Man holds Wine glass":
        return 74
    elif row_label == "Man holds Racket":
        return 75
    elif row_label == "Man holds Mobile phone":
        return 76
    elif row_label == "Man on Bicycle":
        return 77
    elif row_label == "Man on Bed":
        return 78
    elif row_label == "Girl on Bicycle":
        return 79
    elif row_label == "Man plays Drum":
        return 80
    elif row_label == "Woman holds Wine glass":
        return 81
    elif row_label == "Dog on Bench":
        return 82
    elif row_label == "Man holds Drum":
        return 83
    elif row_label == "Chopsticks on Table":
        return 84
    elif row_label == "Man holds Chopsticks":
        return 85
    elif row_label == "Woman holds Chopsticks":
        return 86
    elif row_label == "Boy on Bench":
        return 87
    elif row_label == "Woman holds Beer":
        return 88
    elif row_label == "Man holds Violin":
        return 89
    elif row_label == "Man plays Violin":
        return 90
    elif row_label == "Man plays Piano":
        return 91
    elif row_label == "Woman wears Backpack":
        return 92
    elif row_label == "Girl holds Wine glass":
        return 93
    elif row_label == "Woman holds Coffee cup":
        return 94
    elif row_label == "Man holds Mug":
        return 95
    elif row_label == "Man holds Surfboard":
        return 96
    elif row_label == "Woman holds Mobile phone":
        return 97
    elif row_label == "Boy holds Coffee cup":
        return 98
    elif row_label == "Girl on Bench":
        return 99
    elif row_label == "Girl holds Camera":
        return 100
    elif row_label == "Girl holds Beer":
        return 101
    elif row_label == "Boy holds Table tennis racket":
        return 102
    elif row_label == "Girl holds Racket":
        return 103
    elif row_label == "Girl holds Table tennis racket":
        return 104
    elif row_label == "Girl on Bed":
        return 105
    elif row_label == "Girl holds Bottle":
        return 106
    elif row_label == "Girl on Sofa bed":
        return 107
    elif row_label == "Woman holds Handbag":
        return 108
    elif row_label == "Girl holds Violin":
        return 109
    elif row_label == "Girl plays Violin":
        return 110
    elif row_label == "Girl holds Microphone":
        return 111
    elif row_label == "Girl interacts_with Dog":
        return 112
    elif row_label == "Boy holds Bottle":
        return 113
    elif row_label == "Boy plays Drum":
        return 114
    elif row_label == "Boy holds Wine glass":
        return 115
    elif row_label == "Boy on Bed":
        return 116
    elif row_label == "Knife on Table":
        return 117
    elif row_label == "Girl holds Mug":
        return 118
    elif row_label == "Cat under Table":
        return 119
    elif row_label == "Wine glass on Coffee table":
        return 120
    elif row_label == "Dog under Coffee table":
        return 121
    elif row_label == "Cat on Coffee table":
        return 122
    elif row_label == "Bottle on Coffee table":
        return 123
    elif row_label == "Beer on Coffee table":
        return 124
    elif row_label == "Woman on Bicycle":
        return 125
    elif row_label == "Man inside_of Car":
        return 126
    elif row_label == "Man wears Backpack":
        return 127
    elif row_label == "Man on Motorcycle":
        return 128
    elif row_label == "Man inside_of Van":
        return 129
    elif row_label == "Man holds Suitcase":
        return 130
    elif row_label == "Dog on Bicycle":
        return 131
    elif row_label == "Woman on Motorcycle":
        return 132
    elif row_label == "Boy holds Microphone":
        return 133
    elif row_label == "Man interacts_with Horse":
        return 134
    elif row_label == "Man on Horse":
        return 135
    elif row_label == "Woman holds Violin":
        return 136
    elif row_label == "Woman plays Drum":
        return 137
    elif row_label == "Girl holds Guitar":
        return 138
    elif row_label == "Girl plays Guitar":
        return 139
    elif row_label == "Girl plays Drum":
        return 140
    elif row_label == "Woman plays Violin":
        return 141
    elif row_label == "Woman inside_of Car":
        return 142
    elif row_label == "Man inside_of Taxi":
        return 143
    elif row_label == "Girl inside_of Car":
        return 144
    elif row_label == "Boy inside_of Car":
        return 145
    elif row_label == "Dog inside_of Car":
        return 146
    elif row_label == "Woman inside_of Taxi":
        return 147
    elif row_label == "Boy inside_of Taxi":
        return 148
    elif row_label == "Cat inside_of Car":
        return 149
    elif row_label == "Cat under Car":
        return 150
    elif row_label == "Boy holds Camera":
        return 151
    elif row_label == "Girl wears Backpack":
        return 152
    elif row_label == "Girl holds Backpack":
        return 153
    elif row_label == "Girl holds Mobile phone":
        return 154
    elif row_label == "Woman plays Piano":
        return 155
    elif row_label == "Dog under Chair":
        return 156
    elif row_label == "Boy holds Violin":
        return 157
    elif row_label == "Boy plays Violin":
        return 158
    elif row_label == "Woman holds Flute":
        return 159
    elif row_label == "Boy holds Flute":
        return 160
    elif row_label == "Boy plays Flute":
        return 161
    elif row_label == "Man holds Football":
        return 162
    elif row_label == "Man hits Football":
        return 163
    elif row_label == "Boy hits Football":
        return 164
    elif row_label == "Woman hits Football":
        return 165
    elif row_label == "Man holds Rugby ball":
        return 166
    elif row_label == "Man hits Rugby ball":
        return 167
    elif row_label == "Woman holds Football":
        return 168
    elif row_label == "Girl holds Football":
        return 169
    elif row_label == "Boy holds Football":
        return 170
    elif row_label == "Boy holds Rugby ball":
        return 171
    elif row_label == "Girl hits Football":
        return 172
    elif row_label == "Woman holds Rugby ball":
        return 173
    elif row_label == "Girl holds Rugby ball":
        return 174
    elif row_label == "Boy holds Mobile phone":
        return 175
    elif row_label == "Man interacts_with Snake":
        return 176
    elif row_label == "Dog under Bench":
        return 177
    elif row_label == "Cat on Bench":
        return 178
    elif row_label == "Boy on Motorcycle":
        return 179
    elif row_label == "Girl on Motorcycle":
        return 180
    elif row_label == "Dog on Motorcycle":
        return 181
    elif row_label == "Cat on Motorcycle":
        return 182
    elif row_label == "Hamster on Motorcycle":
        return 183
    elif row_label == "Boy holds Beer":
        return 184
    elif row_label == "Man holds Pretzel":
        return 185
    elif row_label == "Dog on Bed":
        return 186
    elif row_label == "Woman interacts_with Cat":
        return 187
    elif row_label == "Dog on Sofa bed":
        return 188
    elif row_label == "Girl interacts_with Cat":
        return 189
    elif row_label == "Woman holds Drum":
        return 190
    elif row_label == "Boy holds Drum":
        return 191
    elif row_label == "Girl holds Drum":
        return 192
    elif row_label == "Boy on Sofa bed":
        return 193
    elif row_label == "Cat on Sofa bed":
        return 194
    elif row_label == "Boy interacts_with Horse":
        return 195
    elif row_label == "Boy on Horse":
        return 196
    elif row_label == "Girl interacts_with Horse":
        return 197
    elif row_label == "Girl on Horse":
        return 198
    elif row_label == "Woman on Horse":
        return 199
    elif row_label == "Man plays Flute":
        return 200
    elif row_label == "Man holds Flute":
        return 201
    elif row_label == "Man holds Tennis racket":
        return 202
    elif row_label == "Woman holds Tennis racket":
        return 203
    elif row_label == "Boy holds Tennis racket":
        return 204
    elif row_label == "Man hits Tennis ball":
        return 205
    elif row_label == "Girl holds Tennis racket":
        return 206
    elif row_label == "Girl hits Tennis ball":
        return 207
    elif row_label == "Man holds Tennis ball":
        return 208
    elif row_label == "Woman holds Tennis ball":
        return 209
    elif row_label == "Woman hits Tennis ball":
        return 210
    elif row_label == "Man wears Ski":
        return 211
    elif row_label == "Man holds Ski":
        return 212
    elif row_label == "Man wears Snowboard":
        return 213
    elif row_label == "Man holds Snowboard":
        return 214
    elif row_label == "Woman holds Ski":
        return 215
    elif row_label == "Woman wears Ski":
        return 216
    elif row_label == "Girl wears Ski":
        return 217
    elif row_label == "Girl holds Ski":
        return 218
    elif row_label == "Girl holds Snowboard":
        return 219
    elif row_label == "Boy wears Ski":
        return 220
    elif row_label == "Man holds Backpack":
        return 221
    elif row_label == "Woman holds Backpack":
        return 222
    elif row_label == "Boy wears Backpack":
        return 223
    elif row_label == "Cat inside_of Backpack":
        return 224
    elif row_label == "Woman holds Mug":
        return 225
    elif row_label == "Boy holds Mug":
        return 226
    elif row_label == "Woman holds Snowboard":
        return 227
    elif row_label == "Girl plays Piano":
        return 228
    elif row_label == "Boy plays Piano":
        return 229
    elif row_label == "Boy interacts_with Cat":
        return 230
    elif row_label == "Cat on Bed":
        return 231
    elif row_label == "Woman holds Surfboard":
        return 232
    elif row_label == "Girl holds Surfboard":
        return 233
    elif row_label == "Boy holds Surfboard":
        return 234
    elif row_label == "Man interacts_with Elephant":
        return 235
    elif row_label == "Woman interacts_with Elephant":
        return 236
    elif row_label == "Girl interacts_with Elephant":
        return 237
    elif row_label == "Boy interacts_with Elephant":
        return 238
    elif row_label == "Woman inside_of Van":
        return 239
    elif row_label == "Girl inside_of Van":
        return 240
    elif row_label == "Boy inside_of Van":
        return 241
    elif row_label == "Dog inside_of Van":
        return 242
    elif row_label == "Girl holds Flute":
        return 243
    elif row_label == "Girl plays Flute":
        return 244
    elif row_label == "Woman plays Flute":
        return 245
    elif row_label == "Man wears Handbag":
        return 246
    elif row_label == "Girl holds Handbag":
        return 247
    elif row_label == "Man wears Briefcase":
        return 248
    elif row_label == "Boy holds Handbag":
        return 249
    elif row_label == "Cat inside_of Handbag":
        return 250
    elif row_label == "Woman holds Racket":
        return 251
    elif row_label == "Boy holds Racket":
        return 252
    elif row_label == "Man interacts_with Monkey":
        return 253
    elif row_label == "Woman interacts_with Monkey":
        return 254
    elif row_label == "Girl interacts_with Monkey":
        return 255
    elif row_label == "Boy interacts_with Monkey":
        return 256
    elif row_label == "Woman holds Suitcase":
        return 257
    elif row_label == "Girl holds Suitcase":
        return 258
    elif row_label == "Girl wears Suitcase":
        return 259
    elif row_label == "Boy holds Suitcase":
        return 260
    elif row_label == "Boy wears Suitcase":
        return 261
    elif row_label == "Cat inside_of Suitcase":
        return 262
    elif row_label == "Man holds Briefcase":
        return 263
    elif row_label == "Man interacts_with Dolphin":
        return 264
    elif row_label == "Boy interacts_with Dolphin":
        return 265
    elif row_label == "Woman interacts_with Dolphin":
        return 266
    elif row_label == "Girl interacts_with Dolphin":
        return 267
    elif row_label == "Girl interacts_with Snake":
        return 268
    elif row_label == "Boy interacts_with Snake":
        return 269
    elif row_label == "Woman interacts_with Snake":
        return 270
    elif row_label == "Man holds Knife":
        return 271
    elif row_label == "Woman holds Knife":
        return 272
    elif row_label == "Boy holds Knife":
        return 273
    elif row_label == "Man holds Spoon":
        return 274
    elif row_label == "Woman holds Spoon":
        return 275
    elif row_label == "Girl holds Spoon":
        return 276
    elif row_label == "Boy holds Spoon":
        return 277
    elif row_label == "Girl holds Chopsticks":
        return 278
    elif row_label == "Boy holds Chopsticks":
        return 279
    elif row_label == "Man holds Fork":
        return 280
    elif row_label == "Boy holds Fork":
        return 281
    elif row_label == "Woman holds Fork":
        return 282
    elif row_label == "Girl holds Fork":
        return 283
    elif row_label == "Woman interacts_with Hamster":
        return 284
    elif row_label == "Girl interacts_with Hamster":
        return 285
    elif row_label == "Cat on Oven":
        return 286
    elif row_label == "Cat on Microwave oven":
        return 287
    else:
        None


if __name__ == '__main__':

    # class_df = pd.read_csv('challenge-2019-classes-vrd.csv', names=['class_id1', 'Classes'])
    # attr_df = pd.read_csv('challenge-2019-attributes-description.csv', names=['class_id2', 'Attributes'])
    # classes = list(class_df['Classes'])
    # classes.extend(list(attr_df['Attributes']))
    # print(classes)
    
    ############################ Iter 2 ##################################
    dataset = 'train'
    df = pd.read_csv('challenge-2019-'+ dataset +'-vrd.csv')
    class_df = pd.read_csv('challenge-2019-classes-vrd.csv', names=['class_id1', 'Classes'])
    class_id = list(class_df.index)
    attr_df = pd.read_csv('challenge-2019-attributes-description.csv', names=['class_id2', 'Attributes'])
    is_df = df[df['RelationshipLabel'] != 'is']

    is_df = is_df.merge(class_df, left_on='LabelName1', right_on='class_id1')
    is_df = is_df.merge(class_df, left_on='LabelName2', right_on='class_id1')  # Change to attr_df and class_id1

    is_df['Classes'] = is_df['Classes_x'] + ' ' + is_df['RelationshipLabel'] + ' ' + is_df['Classes_y']

    txt = convert_classes(is_df.Classes.unique())
    print(txt)
    with open('label_map_nonis2.pbtxt', 'w') as f:
        f.write(txt)

    # pass

    '''
    classes = ['Chair at Desk', 'Man at Desk', 'Chair at Table', 'Man at Table',
               'Man on Chair', 'Chair at Coffee table', 'Girl at Desk', 'Girl at Table',
               'Girl on Chair', 'Woman at Desk', 'Woman at Table', 'Woman on Chair',
               'Boy at Desk', 'Boy at Table', 'Boy on Chair', 'Woman at Coffee table',
               'Man at Coffee table', 'Girl at Coffee table', 'Bottle on Desk',
               'Bottle on Table', 'Coffee cup on Desk', 'Mug on Desk',
               'Coffee cup on Table', 'Mug on Table', 'Coffee cup on Coffee table',
               'Mug on Coffee table', 'Dog on Chair', 'Man interacts_with Dog',
               'Dog under Desk', 'Dog under Table', 'Wine glass on Desk',
               'Wine glass on Table', 'Man holds Microphone', 'Man holds Camera',
               'Boy at Coffee table', 'Woman holds Microphone', 'Man holds Coffee cup',
               'Man on Bench', 'Cat on Desk', 'Cat on Table', 'Man on Sofa bed',
               'Man holds Table tennis racket', 'Woman holds Table tennis racket',
               'Man holds Bottle', 'Woman on Bed', 'Woman interacts_with Dog',
               'Woman holds Camera', 'Woman wears Handbag', 'Boy holds Guitar',
               'Boy plays Guitar', 'Beer on Desk', 'Beer on Table', 'Dog on Desk',
               'Dog on Table', 'Boy interacts_with Dog', 'Man holds Handbag',
               'Cat under Chair', 'Woman holds Bottle', 'Cat on Chair', 'Fork on Table',
               'Woman interacts_with Horse', 'Woman on Bench', 'Boy on Bicycle',
               'Man holds Guitar', 'Man plays Guitar', 'Spoon on Table',
               'Woman holds Guitar', 'Woman plays Guitar', 'Girl holds Coffee cup',
               'Woman on Sofa bed', 'Girl wears Handbag', 'Man holds Beer',
               'Man interacts_with Cat', 'Man holds Wine glass', 'Man holds Racket',
               'Man holds Mobile phone', 'Man on Bicycle', 'Man on Bed', 'Girl on Bicycle',
               'Man plays Drum', 'Woman holds Wine glass', 'Dog on Bench', 'Man holds Drum',
               'Chopsticks on Table', 'Man holds Chopsticks', 'Woman holds Chopsticks',
               'Boy on Bench', 'Woman holds Beer', 'Man holds Violin', 'Man plays Violin',
               'Man plays Piano', 'Woman wears Backpack', 'Girl holds Wine glass',
               'Woman holds Coffee cup', 'Man holds Mug', 'Man holds Surfboard',
               'Woman holds Mobile phone', 'Boy holds Coffee cup', 'Girl on Bench',
               'Girl holds Camera', 'Girl holds Beer', 'Boy holds Table tennis racket',
               'Girl holds Racket', 'Girl holds Table tennis racket', 'Girl on Bed',
               'Girl holds Bottle', 'Girl on Sofa bed', 'Woman holds Handbag',
               'Girl holds Violin', 'Girl plays Violin', 'Girl holds Microphone',
               'Girl interacts_with Dog', 'Boy holds Bottle', 'Boy plays Drum',
               'Boy holds Wine glass', 'Boy on Bed', 'Knife on Table', 'Girl holds Mug',
               'Cat under Table', 'Wine glass on Coffee table', 'Dog under Coffee table',
               'Cat on Coffee table', 'Bottle on Coffee table', 'Beer on Coffee table',
               'Woman on Bicycle', 'Man inside_of Car', 'Man wears Backpack',
               'Man on Motorcycle', 'Man inside_of Van', 'Man holds Suitcase',
               'Dog on Bicycle', 'Woman on Motorcycle', 'Boy holds Microphone',
               'Man interacts_with Horse', 'Man on Horse', 'Woman holds Violin',
               'Woman plays Drum', 'Girl holds Guitar', 'Girl plays Guitar',
               'Girl plays Drum', 'Woman plays Violin', 'Woman inside_of Car',
               'Man inside_of Taxi', 'Girl inside_of Car', 'Boy inside_of Car',
               'Dog inside_of Car', 'Woman inside_of Taxi', 'Boy inside_of Taxi',
               'Cat inside_of Car', 'Cat under Car', 'Boy holds Camera',
               'Girl wears Backpack', 'Girl holds Backpack', 'Girl holds Mobile phone',
               'Woman plays Piano', 'Dog under Chair', 'Boy holds Violin',
               'Boy plays Violin', 'Woman holds Flute', 'Boy holds Flute',
               'Boy plays Flute', 'Man holds Football', 'Man hits Football',
               'Boy hits Football', 'Woman hits Football', 'Man holds Rugby ball',
               'Man hits Rugby ball', 'Woman holds Football', 'Girl holds Football',
               'Boy holds Football', 'Boy holds Rugby ball', 'Girl hits Football',
               'Woman holds Rugby ball', 'Girl holds Rugby ball', 'Boy holds Mobile phone',
               'Man interacts_with Snake', 'Dog under Bench', 'Cat on Bench',
               'Boy on Motorcycle', 'Girl on Motorcycle', 'Dog on Motorcycle',
               'Cat on Motorcycle', 'Hamster on Motorcycle', 'Boy holds Beer',
               'Man holds Pretzel', 'Dog on Bed', 'Woman interacts_with Cat',
               'Dog on Sofa bed', 'Girl interacts_with Cat', 'Woman holds Drum',
               'Boy holds Drum', 'Girl holds Drum', 'Boy on Sofa bed', 'Cat on Sofa bed',
               'Boy interacts_with Horse', 'Boy on Horse', 'Girl interacts_with Horse',
               'Girl on Horse', 'Woman on Horse', 'Man plays Flute', 'Man holds Flute',
               'Man holds Tennis racket', 'Woman holds Tennis racket',
               'Boy holds Tennis racket', 'Man hits Tennis ball',
               'Girl holds Tennis racket', 'Girl hits Tennis ball',
               'Man holds Tennis ball', 'Woman holds Tennis ball',
               'Woman hits Tennis ball', 'Man wears Ski', 'Man holds Ski',
               'Man wears Snowboard', 'Man holds Snowboard', 'Woman holds Ski',
               'Woman wears Ski', 'Girl wears Ski', 'Girl holds Ski',
               'Girl holds Snowboard', 'Boy wears Ski', 'Man holds Backpack',
               'Woman holds Backpack', 'Boy wears Backpack', 'Cat inside_of Backpack',
               'Woman holds Mug', 'Boy holds Mug', 'Woman holds Snowboard',
               'Girl plays Piano', 'Boy plays Piano', 'Boy interacts_with Cat',
               'Cat on Bed', 'Woman holds Surfboard', 'Girl holds Surfboard',
               'Boy holds Surfboard', 'Man interacts_with Elephant',
               'Woman interacts_with Elephant', 'Girl interacts_with Elephant',
               'Boy interacts_with Elephant', 'Woman inside_of Van', 'Girl inside_of Van',
               'Boy inside_of Van', 'Dog inside_of Van', 'Girl holds Flute',
               'Girl plays Flute', 'Woman plays Flute', 'Man wears Handbag',
               'Girl holds Handbag', 'Man wears Briefcase', 'Boy holds Handbag',
               'Cat inside_of Handbag', 'Woman holds Racket', 'Boy holds Racket',
               'Man interacts_with Monkey', 'Woman interacts_with Monkey',
               'Girl interacts_with Monkey', 'Boy interacts_with Monkey',
               'Woman holds Suitcase', 'Girl holds Suitcase', 'Girl wears Suitcase',
               'Boy holds Suitcase', 'Boy wears Suitcase', 'Cat inside_of Suitcase',
               'Man holds Briefcase', 'Man interacts_with Dolphin',
               'Boy interacts_with Dolphin', 'Woman interacts_with Dolphin',
               'Girl interacts_with Dolphin', 'Girl interacts_with Snake',
               'Boy interacts_with Snake', 'Woman interacts_with Snake', 'Man holds Knife',
               'Woman holds Knife', 'Boy holds Knife', 'Man holds Spoon',
               'Woman holds Spoon', 'Girl holds Spoon', 'Boy holds Spoon',
               'Girl holds Chopsticks', 'Boy holds Chopsticks', 'Man holds Fork',
               'Boy holds Fork', 'Woman holds Fork', 'Girl holds Fork',
               'Woman interacts_with Hamster', 'Girl interacts_with Hamster',
               'Cat on Oven', 'Cat on Microwave oven']

    for i, val in enumerate(classes):
        print('elif row_label == "' + val + '": return ' + str(i + 1))
    '''