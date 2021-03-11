import os

root_path ="./videos"
save_path = "./videos1"

if not os.path.exists(save_path):
    os.mkdir(save_path)
count = 1
for video_name in os.listdir(root_path):
    os.rename(os.path.join(root_path,video_name), os.path.join(save_path, "knife_"+ str(count)+".mp4"))
    count += 1