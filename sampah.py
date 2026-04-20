import os, shutil, random

SRC = "all"
DST = "dataset"

def get_all_images():
    data = {"plastic": [], "non_plastic": []}

    # plastic
    plastic_path = os.path.join(SRC, "plastic", "plastic")
    for f in os.listdir(plastic_path):
        if f.lower().endswith((".jpg",".png",".jpeg")):
            data["plastic"].append(os.path.join(plastic_path, f))

    # non-plastic (gabung semua subfolder)
    non_path = os.path.join(SRC, "non-plastic")
    for sub in os.listdir(non_path):
        subdir = os.path.join(non_path, sub)
        if not os.path.isdir(subdir): continue
        for f in os.listdir(subdir):
            if f.lower().endswith((".jpg",".png",".jpeg")):
                data["non_plastic"].append(os.path.join(subdir, f))

    return data

def split_and_copy(files, label):
    random.shuffle(files)
    n = len(files)
    t1 = int(n * 0.7)
    t2 = int(n * 0.85)

    splits = {
        "train": files[:t1],
        "val": files[t1:t2],
        "test": files[t2:]
    }

    for sp, flist in splits.items():
        outdir = os.path.join(DST, sp, label)
        os.makedirs(outdir, exist_ok=True)
        for f in flist:
            shutil.copy(f, outdir)

if __name__ == "__main__":
    data = get_all_images()
    for label, files in data.items():
        print(label, ":", len(files), "files")
        split_and_copy(files, label)
    print("Selesai split dataset.")
