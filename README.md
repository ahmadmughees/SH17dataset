# **SH17: A Dataset for Human Safety and Personal Protective Equipment Detection in Manufacturing Industry**
[![paper](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](Link here)
[![Weights](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/mugheesahmad/sh17-dataset-for-ppe-detection)

<img src="extras/readme/samples.gif" alt="Demo" width="840" align="middle"/>

---
## 📢 Latest Updates
- **2024-07-04**: The data is now available at [kaggle](https://www.kaggle.com/datasets/mugheesahmad/sh17-dataset-for-ppe-detection).
- **2024-07-04**: Paper is now available at [ArXiv](link here).
---

## **Table of Contents**
1. [Abstract](##abstract)
2. [Dataset](#dataset) ([download](https://www.kaggle.com/datasets/mugheesahmad/sh17-dataset-for-ppe-detection))
4. [Models](#models)
5. [Citation](#citation)
6. [License](#license)

---

## **Abstract**

Workplace accidents continue to pose significant risks for human safety, particularly in industries such as construction and manufacturing, and the necessity for effective Personal Protective Equipment (PPE) compliance has become increasingly paramount. Our research focuses on the development of non-invasive techniques based on the Object Detection (OD) and Convolutional Neural Network (CNN) to detect and verify the proper use of various types of PPE such as helmets, safety glasses, masks, and protective clothing. This study proposes the SH17 Dataset, consisting of 8,099 annotated images containing 75,994 instances of 17 classes collected from diverse industrial environments, to train and validate the OD models. We have trained state-of-the-art OD models for benchmarking, and initial results demonstrate promising accuracy levels with You Only Look Once (YOLO)v9-e model variant exceeding 70.9% in PPE detection. The performance of the model validation on cross-domain datasets suggests that integrating these technologies can significantly improve safety management systems, providing a scalable and efficient solution for industries striving to meet human safety regulations and protect their workforce.

---
## Download the dataset !!!

The images and annotated labels can be found in [Kaggle](https://www.kaggle.com/datasets/mugheesahmad/sh17-dataset-for-ppe-detection).

All images can be downloaded via list of URLs from the source using [download_from_pexels.py](data/download_from_pexels.py) script. 
```
cd data
python download_from_pexels.py
```
---

## Dataset

The SH17 dataset consists of:
- 8,099 annotated images 
- 75,994 object instances
- 17 classes of PPE items and body parts

---

### Key features
- Collected from diverse industrial environments globally
- High quality images (max resolution 8192x5462, min 1920x1002)
- Average of 9.38 instances per image
- Includes small objects like ears and earmuffs (39,764 annotations < 1% image area, 59,025 annotations < 5% area)

---

## Classes
1. Person
2. Head  
3. Face
4. Glasses
5. Face-mask-medical
6. Face-guard
7. Ear
8. Earmuffs
9. Hands
10. Gloves
11. Foot
12. Shoes  
13. Safety-vest
14. Tools
15. Helmet
16. Medical-suit
17. Safety-suit

---

## Class distribution

<img src="extras/readme/data_distribution.svg" alt="class distribution" width="600" align="middle"/>

---

## Models

We provide benchmark results and weights (will be added soon) for state-of-the-art object detection models trained on SH17 Models.

---

### YOLO v8, v9, v10 Results

| Model     | Params | Images | Instances | P        | R        | mAP50    | mAP50-95 |
|-----------|--------|--------|-----------|----------|----------|----------|----------|
| Yolo-8-n  | 3.2    | 1620   | 15358     | 67.5     | 53.6     | 58.0     | 36.6     |
| Yolo-8-s  | 11.2   | 1620   | 15358     | 81.5     | 55.7     | 63.7     | 41.7     |
| Yolo-8-m  | 25.9   | 1620   | 15358     | 77.1     | 60.5     | 66.6     | 45.7     |
| Yolo-8-l  | 43.7   | 1620   | 15358     | 76.7     | 62.9     | 68.0     | 47.0     |
| Yolo-8-x  | 68.2   | 1620   | 15358     | 77.1     | 63.1     | 69.3     | 47.2     |
| Yolo-9-t  | 2.0    | 1620   | 15358     | 75.0     | 52.6     | 58.5     | 37.5     |
| Yolo-9-s  | 7.2    | 1620   | 15358     | 73.6     | 60.2     | 65.3     | 42.9     |
| Yolo-9-m  | 20.1   | 1620   | 15358     | 77.4     | 62.0     | 68.6     | 46.5     |
| Yolo-9-c  | 25.5   | 1620   | 15358     | 79.6     | 60.8     | 67.7     | 46.5     |
| Yolo-9-e  | 58.1   | 1620   | 15358     | **81.0** | **65.0** | **70.9** | **48.7** |
| Yolo-10-n | 2.3    | 1620   | 15358     | 66.8     | 53.2     | 57.2     | 35.9     |
| Yolo-10-s | 7.2    | 1620   | 15358     | 75.8     | 57.0     | 62.7     | 40.9     |
| Yolo-10-m | 15.4   | 1620   | 15358     | 71.4     | 61.4     | 65.7     | 43.8     |
| Yolo-10-b | 19.1   | 1620   | 15358     | 77.7     | 59.1     | 65.8     | 45.1     |
| Yolo-10-l | 24.4   | 1620   | 15358     | 76.0     | 61.8     | 67.4     | 46.0     |
| Yolo-10-x | 29.5   | 1620   | 15358     | 76.8     | 62.8     | 67.8     | 46.7     |

---

## Usage
```python
from ultralytics import YOLO

model = YOLO('yolov9-e.pt')   # Load pretrained model 
results = model('image.jpg')  # Run inference

results.show()  # View results
```

---

## Evaluation

We provide evaluation code to reproduce our benchmark results on the SH17 test set.

```
python evaluate.py --model yolov9-e.pt --data sh17_test.yaml
```

---

## Citation

If you use this dataset or code in your research, please cite our paper:

```latex
@article{ahmad_2024_sh17,
  title={SH17: A Dataset for Human Safety and Personal Protective Equipment Detection in Manufacturing Industry},
  author={Ahmad, Hafiz Mughees and Rahimi, Afshin},
  journal={Arxiv},
  year={2024}
}
```

## License

The SH17 dataset is released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.


### Disclaimer and Responsible Use:
This dataset, scrapped through the Pexels website, is intended for educational, research, and analysis purposes only. You may be able to use the data for training of the Machine learning models only.  Users are urged to use this data responsibly, ethically, and within the bounds of legal stipulations.

### Users should adhere to [Copyright Notice of Pexels ](https://www.pexels.com/license/) when utilizing this dataset.

Legal Simplicity: All photos and videos on Pexels can be downloaded and used for free.

### Allowed 👌
- All photos and videos on Pexels are free to use.
- Attribution is not required. Giving credit to the photographer or Pexels is not necessary but always appreciated.
- You can modify the photos and videos from Pexels. Be creative and edit them as you like.
### Not allowed 👎
- Identifiable people may not appear in a bad light or in a way that is offensive.
- Don't sell unaltered copies of a photo or video, e.g. as a poster, print or on a physical product without modifying it first.
- Don't imply endorsement of your product by people or brands on the imagery.
- Don't redistribute or sell the photos and videos on other stock photo or wallpaper platforms.
- Don't use the photos or videos as part of your trade-mark, design-mark, trade-name, business name or service mark.


### No Warranty Disclaimer: 
The dataset is provided "as is," without warranty, and the creator disclaims any legal liability for its use by others.

### Ethical Use: 
Users are encouraged to consider the ethical implications of their analyses and the potential impact on broader community.

---
## Contact

For any questions or concerns, please open an issue in this repository or contact *mughees* at `ahmad54@uwindsor.ca`

## Acknowledgement

Training of all the models is done using [ultralytics](https://github.com/ultralytics/ultralytics) repository. Thanks for the great implementations!