# Vision Transformer on CIFAR-10 (from scratch)

A lightweight project where I implemented a Vision Transformer (ViT) from scratch using PyTorch, inspired by the paper [*An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*](https://arxiv.org/abs/2010.11929).

The model is trained and tested on the CIFAR-10 dataset — chosen for its small size and ease of experimentation. This project was a hands-on dive into the ViT architecture, focusing on core components of Machine Learning.


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
