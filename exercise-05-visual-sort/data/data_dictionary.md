# VisualSort data dictionary

`train_images.npz` and `test_images.npz` each contain:

- `images`: unsigned 8-bit array shaped `(n, 28, 28)`, values 0–255.
- `image_id`: randomized string identifiers aligned to the first dimension.

Training labels are one of: `top`, `trouser`, `pullover`, `dress`, `coat`, `sandal`, `shirt`, `sneaker`, `bag`, `ankle_boot`.

The images are low-resolution grayscale catalog-style silhouettes. They do not represent production photography, background variation, multiple products, or diverse camera conditions. A model trained here must not be represented as production-ready.
