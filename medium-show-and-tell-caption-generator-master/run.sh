#!/bin/bash
echo "Welcome"
read -p "Enter The Image name: "  username
#echo "Welcome $username!"

#echo "hello"
docker run -v $PWD:/opt/app -e PYTHONPATH=$PYTHONPATH:/opt/app -it manasa/medium-show-and-tell-caption-generator  python3 /opt/app/medium_show_and_tell_caption_generator/inference1.py --model_path /opt/app/etc/show-and-tell.pb --input_files /opt/app/imgs/$username --vocab_file /opt/app/etc/word_counts.txt >out1.txt


#echo "Hello"
python3 voice.py
