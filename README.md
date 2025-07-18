# 🧠 Vision Transformer (ViT) on CIFAR-10 — From Scratch

This project implements a **Vision Transformer (ViT)** architecture from the ground up in **PyTorch**, inspired by the research paper  
> *"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"*  
> by Dosovitskiy et al. ([arXiv:2010.11929](https://arxiv.org/abs/2010.11929))

The model is trained and evaluated on the **CIFAR-10** dataset — chosen for its compact size and suitability for experimentation.  
This project was a hands-on exploration of the core ViT architecture, aimed at understanding transformer-based vision models without relying on pre-built modules or pre-trained weights.

---

## 📦 Features

- ✅ ViT architecture implemented **entirely from scratch**
- 🔲 **Patch embedding** via `Conv2d` with flattening and projection
- 📍 Learnable **positional encodings** with a `[CLS]` token
- 🧠 Transformer encoder blocks with:
  - Multi-head self-attention
  - MLP layers + GELU activation
- 🔎 **Classification head** operating on `[CLS]` token
- 📈 Custom **training and evaluation** loops
- 🎨 Grid-based **visualization** of predictions for qualitative insight

---

## 🛠️ Setup & Installation

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

## 📊 Dataset

* Uses **CIFAR-10** from `torchvision.datasets`
* Automatically downloads and normalizes the dataset
* 10 classes, 32×32 color images, ideal for quick transformer training experiments

---

## 🖼️ Output Visualization

After training, the model produces **color-coded grid plots** of predictions vs ground truth — useful for:

* Identifying common failure modes
* Visual confirmation of model confidence
* Quick debugging and qualitative evaluation

---

## 📄 License

MIT License — feel free to fork, modify, and build upon the code for personal or academic use.

---

## 👤 Author

Developed by [Hrishikesh Uchake](https://github.com/HrishikeshUchake)

---

## ✨ Coming Soon

* Support for larger datasets (e.g. CIFAR-100, TinyImageNet)
* Accuracy/loss logging with `TensorBoard`
* CLI training and evaluation wrapper

```

---

Let me know if you'd like a badge-styled header, deployment info, or GitHub actions integration. You can copy and paste this directly into a `README.md` file.
```
