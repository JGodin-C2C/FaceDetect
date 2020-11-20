# I want a mustache. 

The script live.py allows to add a fancy mustache to all your faces available on
the webcam. You do not have to take care about this facial attribute anymore,
let your computer do it for you ! 

Get fancy on these zoom meetings ! 

# How-to.

Install and load v4l2loopback to create a virtual /dev/video2


```
apt-get install v4l2loopback-utils
modprobe v4l2loopback devices=1  exclusive_caps=1 video_nr=2 card_label="mustache-mustache"
```

⚠️ Warning ⚠️: on installation , `v4loopback` will modprobe at startup and the
exclusive_caps=1 may be lost.  you have to onload it first with:

```
modprobe -r v4l2loopback  
```

Python dependencies

```
pip install opencv-python pyfakewebcam
```

Run

```
python live.py
```

