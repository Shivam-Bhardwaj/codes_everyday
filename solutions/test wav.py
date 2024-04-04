import eyed3

def encode_image(mp3_file_path, image_file_path):
    audiofile = eyed3.load(mp3_file_path)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.images.set(3, open(image_file_path,'rb').read(), 'image/jpeg')

    audiofile.tag.save()

def decode_image(mp3_file_path, image_output_path):
    audiofile = eyed3.load(mp3_file_path)
    image_data = audiofile.tag.images.get('').image_data

    with open(image_output_path, 'wb') as img_out:
        img_out.write(image_data)

# Test the functions
encode_image('test.mp3', '/home/shivam/PycharmProjects/codes_everyday/solutions/4778723-200.png')
decode_image('test.mp3', 'output.jpg')