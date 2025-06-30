# Vision Transformer on CIFAR-10 (from scratch)

Just a small project where I implemented a Vision Transformer (ViT) from scratch using PyTorch — no pretrained weights, no shortcuts. It runs on CIFAR-10 because... it's small and easy to test on.

---

## Breakdown of the model

- ViT model built from the ground up
- Patch embedding with Conv2d
- Positional embeddings + CLS token
- Transformer encoder layers (multi-head self-attention + MLP)
- Classifier on the [CLS] token
- Training + evaluation code
- Plotting predictions in a grid (color-coded for fun)

---

## Setup

You’ll need:
- Clone this repo and make sure to:
```bash
pip install torch torchvision matplotlib
