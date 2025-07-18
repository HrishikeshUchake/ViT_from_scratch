# Vision Transformer (ViT) on CIFAR-10 — From Scratch

This project implements a **Vision Transformer (ViT)** architecture from the ground up in **PyTorch**, inspired by the research paper  
> *"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"*  
> by Dosovitskiy et al. ([arXiv:2010.11929](https://arxiv.org/abs/2010.11929))

The model is trained and evaluated on the **CIFAR-10** dataset — chosen for its compact size and suitability for experimentation.  
This project was a hands-on exploration of the core ViT architecture, aimed at understanding transformer-based vision models without relying on pre-built modules or pre-trained weights.

---

## Features

-  ViT architecture implemented **entirely from scratch**
-  **Patch embedding** via `Conv2d` with flattening and projection
-  Learnable **positional encodings** with a `[CLS]` token
-  Transformer encoder blocks with:
    - Multi-head self-attention
    - MLP layers + GELU activation
-  **Classification head** operating on `[CLS]` token
-  Custom **training and evaluation** loops
-  Grid-based **visualization** of predictions for qualitative insight

---

##  Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/HrishikeshUchake/vit-from-scratch.git
cd vit-from-scratch
````

2. Install dependencies:

```bash
pip install torch torchvision matplotlib
```

---

##  Dataset

* Uses **CIFAR-10** from `torchvision.datasets`
* Automatically downloads and normalizes the dataset
* 10 classes, 32×32 color images, ideal for quick transformer training experiments

---

##  Output Visualization

After training, the model produces **color-coded grid plots** of predictions vs ground truth — useful for:

* Identifying common failure modes
* Visual confirmation of model confidence
* Quick debugging and qualitative evaluation

<img width="754" height="546" alt="Screenshot 2025-07-18 at 1 42 07 PM" src="https://github.com/user-attachments/assets/96fc4af3-9209-47a3-95a1-3ca37d4e9c93" />
<img width="775" height="784" alt="Screenshot 2025-07-18 at 1 41 55 PM" src="https://github.com/user-attachments/assets/1b8cee93-c3ae-434f-9523-e88ac126b681" />


---

##  License

MIT License — feel free to fork, modify, and build upon the code for personal or academic use.

---

##  Author

Developed by [Hrishikesh Uchake](https://github.com/HrishikeshUchake)

---

##  Coming Soon

* Support for larger datasets (e.g. CIFAR-100, TinyImageNet)
* Accuracy/loss logging with `TensorBoard`
* CLI training and evaluation wrapper


